#!/usr/bin/env python3
"""cdp.py — a reusable headless-Chrome harness built on the Python standard library only.

No pip installs. No puppeteer, no selenium, no `websockets`, no `requests`. Everything
here is `socket`, `ssl`-free plain HTTP, `urllib.request`, `base64`, `struct`, `json`,
`subprocess`, `tempfile`, `threading` and `http.server`.

Usage
-----

    import cdp

    with cdp.Browser() as b:                          # launches headless chrome on a free port
        p = b.page("http://localhost:8000/x.html")    # navigate, wait for load + settle
        v = p.eval("document.title")                  # evaluate JS, get the JSON value back
        p.screenshot("/tmp/out.png", width=1280)      # full-page PNG at a layout width
        errs = p.console_errors()                     # console errors + uncaught exceptions

Serving a directory of static files (for testing local HTML):

    server, port = cdp.serve("/path/to/dir")          # silent ThreadingHTTPServer, daemon thread
    ...
    server.shutdown()

Narrow / mobile viewports
-------------------------
IMPORTANT: the layout width comes from `Emulation.setDeviceMetricsOverride`, **never** from
a `--window-size` launch flag. Headless Chrome floors its window width at roughly 500px, so
a `--window-size=390,900` run silently produces a ~500px-wide layout and then crops the
image — you get a screenshot that is 390px wide but shows a 500px-wide layout, which is the
wrong layout entirely. Overriding device metrics reflows the page at the true CSS width, so
media queries at 390px fire exactly as they do on a real phone.

This is verified by the self-test at the bottom of this file, which asserts that a
`width=390` screenshot has an IHDR width of exactly 390 (not floored to ~500) *and* that the
page's own `innerWidth` reads 390 while the shot is taken.

Screenshot geometry
-------------------
`screenshot()` sets device metrics to the requested width/height at deviceScaleFactor 1, then
reads `Page.getLayoutMetrics().cssContentSize` to learn the full document height, and passes
an explicit `clip` to `Page.captureScreenshot` with `captureBeyondViewport: True`.

The clip *width* is pinned to the requested `width` rather than to `cssContentSize.width`, so
the produced PNG is always exactly `width` pixels across — deterministic, and matching what a
real browser viewport of that width shows. A page that overflows horizontally is cropped at
the viewport edge, which is the same thing the user would see. The clip *height* comes from
`cssContentSize` and is capped at 30000px so a pathologically long page cannot blow up memory.

Console errors
--------------
`console_errors()` accumulates, since the last navigation: `Log.entryAdded` entries at level
`error`, `Runtime.exceptionThrown`, `Console.messageAdded` at level `error`, and (belt and
braces, because modern Chrome routes `console.error` through Runtime rather than Log)
`Runtime.consoleAPICalled` of type `error`/`assert`. Duplicates across those four sources are
collapsed by message text. Events are buffered as they arrive during any `send()` call, so
nothing is lost between calls.

Each string is prefixed with its source, e.g.:

    [Console] BOOM 42
    [exception] TypeError: KABOOM deliberate ...
    [Log] Failed to load resource: ... 404 ... http://host/favicon.ico

Note that failed subresource loads count as errors, which includes the `favicon.ico` 404 that
a bare local page always produces. Filter on the caller's side if that noise is unwanted:

    real = [e for e in p.console_errors() if "favicon.ico" not in e]

`console.warn` is deliberately NOT reported — errors and exceptions only.

Design notes
------------
* One page target per Browser. `page(url)` reuses (re-navigates) the browser's single page
  target rather than spawning new ones — that keeps the WebSocket plumbing to a single
  connection with no `Target.attachToTarget` / flat-session bookkeeping.
* CDP ids are a monotonic integer. `send()` reads frames until it sees the reply with the
  matching id, stashing every event it passes on the way into `self._events`.
"""

from __future__ import annotations

import atexit
import base64
import json
import math
import os
import random
import select
import shutil
import signal
import socket
import struct
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

DEFAULT_SETTLE = 0.6
MAX_CLIP_HEIGHT = 30000


# --------------------------------------------------------------------------------------
# gate scratch root
# --------------------------------------------------------------------------------------
#
# ⊕ MRB-270. Chrome profiles used to land wherever `$TMPDIR` pointed, which on
# this machine is the SAME VOLUME as `/private/tmp` — the directory the Bash
# tool writes its own output files into. So when a leaked profile filled the
# disk on 19 Aug 2026 it did not merely fail the gate: it took the shell down
# with `ENOSPC` mid-run, and a session that cannot write cannot even report why.
#
# Two changes keep that from recurring.
#
# 1. Profiles go under a NAMED, dedicated root — `$KS3_GATE_TMP`, or
#    `~/tmp/ks3-gates` — so debris is identifiable as ours, sweepable without
#    guessing, and not sharing a directory with the harness's lifeline.
#
# 2. `close()` and the `atexit` hook both remove a profile, but neither runs on
#    SIGKILL, and SIGKILL is EXACTLY what a full disk produces. So the root is
#    swept on import: every `cdp-profile-*` records the PID that made it, and
#    any whose maker is gone is removed before this run adds more. A crash now
#    costs one run's profiles, not an unbounded pile.

GATE_TMP = os.environ.get("KS3_GATE_TMP") or os.path.join(
    os.path.expanduser("~"), "tmp", "ks3-gates")

_PROFILE_PREFIX = "cdp-profile-"
_OWNER_FILE = ".owner-pid"


def gate_tmp() -> str:
    """The scratch root for headless gates. Created on first use."""
    os.makedirs(GATE_TMP, exist_ok=True)
    return GATE_TMP


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def sweep_orphan_profiles(root: str | None = None) -> list[str]:
    """Remove profile dirs whose creating process is gone. Returns what it removed.

    Never raises: a sweep that fails must not fail the gate that called it.
    """
    removed: list[str] = []
    try:
        base = root or gate_tmp()
        for name in sorted(os.listdir(base)):
            if not name.startswith(_PROFILE_PREFIX):
                continue
            path = os.path.join(base, name)
            if not os.path.isdir(path):
                continue
            owner = os.path.join(path, _OWNER_FILE)
            try:
                pid = int(open(owner, encoding="utf-8").read().strip())
            except (OSError, ValueError):
                # No owner stamp — written by a build before this change, or a
                # profile that died between mkdtemp and the stamp. Either way
                # nothing living claims it.
                pid = -1
            if pid == os.getpid() or (pid > 0 and _pid_alive(pid)):
                continue
            shutil.rmtree(path, ignore_errors=True)
            removed.append(path)
    except OSError:
        pass
    return removed


_SWEPT_AT_IMPORT = sweep_orphan_profiles()


class CDPError(RuntimeError):
    """Raised when Chrome returns an `error` for a CDP command, or the protocol misbehaves."""


class JSError(RuntimeError):
    """Raised when an evaluated expression throws."""


# --------------------------------------------------------------------------------------
# hand-rolled WebSocket client
# --------------------------------------------------------------------------------------

_OP_CONT = 0x0
_OP_TEXT = 0x1
_OP_BIN = 0x2
_OP_CLOSE = 0x8
_OP_PING = 0x9
_OP_PONG = 0xA


class WSClient:
    """The smallest WebSocket client that can carry CDP: text frames, masked outbound."""

    def __init__(self, url: str, timeout: float = 60.0):
        if not url.startswith("ws://"):
            raise CDPError("only ws:// is supported, got %r" % (url,))
        rest = url[len("ws://"):]
        netloc, _, path = rest.partition("/")
        path = "/" + path
        host, _, port_s = netloc.partition(":")
        port = int(port_s or 80)

        self.closed = False
        self._buf = b""
        self.sock = socket.create_connection((host, port), timeout=timeout)
        self.sock.settimeout(timeout)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        key = base64.b64encode(bytes(random.getrandbits(8) for _ in range(16))).decode()
        req = (
            "GET %s HTTP/1.1\r\n"
            "Host: %s\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            "Sec-WebSocket-Key: %s\r\n"
            "Sec-WebSocket-Version: 13\r\n"
            "\r\n" % (path, netloc, key)
        )
        self.sock.sendall(req.encode())

        # Read past the end of the response headers. We deliberately validate nothing:
        # if the upgrade failed, the first frame parse will fail loudly instead.
        while b"\r\n\r\n" not in self._buf:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise CDPError("connection closed during websocket handshake")
            self._buf += chunk
        head, _, tail = self._buf.partition(b"\r\n\r\n")
        if b"101" not in head.split(b"\r\n", 1)[0]:
            raise CDPError("websocket upgrade rejected: %r" % (head[:200],))
        self._buf = tail

    # -- low level reads ---------------------------------------------------------------

    def _recv_exact(self, n: int) -> bytes:
        """Return exactly n bytes, looping recv() until the buffer is satisfied.

        Screenshot payloads run to several megabytes and arrive across many TCP segments,
        so every frame read goes through here rather than a single recv().
        """
        while len(self._buf) < n:
            try:
                chunk = self.sock.recv(1 << 16)
            except socket.timeout:
                raise CDPError("timed out waiting for %d bytes from chrome" % n)
            if not chunk:
                self.closed = True
                raise CDPError("chrome closed the websocket mid-frame")
            self._buf += chunk
        out, self._buf = self._buf[:n], self._buf[n:]
        return out

    def _read_frame(self) -> tuple[int, bytes, bool]:
        """Read one raw frame. Returns (opcode, payload, fin). Server frames are unmasked,
        but the mask bit is honoured anyway so a masking peer would not corrupt us."""
        b0, b1 = self._recv_exact(2)
        fin = bool(b0 & 0x80)
        opcode = b0 & 0x0F
        masked = bool(b1 & 0x80)
        length = b1 & 0x7F
        if length == 126:
            (length,) = struct.unpack("!H", self._recv_exact(2))
        elif length == 127:
            (length,) = struct.unpack("!Q", self._recv_exact(8))
        mask = self._recv_exact(4) if masked else None
        payload = self._recv_exact(length) if length else b""
        if mask:
            payload = bytes(c ^ mask[i % 4] for i, c in enumerate(payload))
        return opcode, payload, fin

    # -- message level -----------------------------------------------------------------

    def recv(self) -> str:
        """Return the next complete text message, transparently handling control frames
        and multi-frame (continuation) messages."""
        while True:
            opcode, payload, fin = self._read_frame()

            if opcode == _OP_PING:
                self._send_frame(_OP_PONG, payload)
                continue
            if opcode == _OP_PONG:
                continue
            if opcode == _OP_CLOSE:
                self.closed = True
                raise CDPError("chrome sent websocket close")

            if opcode in (_OP_TEXT, _OP_BIN):
                data = payload
                while not fin:
                    op2, more, fin = self._read_frame()
                    if op2 == _OP_PING:
                        self._send_frame(_OP_PONG, more)
                        fin = False
                        continue
                    if op2 == _OP_PONG:
                        fin = False
                        continue
                    if op2 == _OP_CLOSE:
                        self.closed = True
                        raise CDPError("chrome sent websocket close mid-message")
                    if op2 != _OP_CONT:
                        raise CDPError("expected continuation frame, got opcode %d" % op2)
                    data += more
                return data.decode("utf-8", "replace")

            # Unknown opcode: skip it rather than dying.

    def _send_frame(self, opcode: int, payload: bytes) -> None:
        header = bytearray()
        header.append(0x80 | opcode)  # FIN set, single-frame messages only
        n = len(payload)
        if n < 126:
            header.append(0x80 | n)  # mask bit is mandatory for client->server
        elif n < (1 << 16):
            header.append(0x80 | 126)
            header += struct.pack("!H", n)
        else:
            header.append(0x80 | 127)
            header += struct.pack("!Q", n)
        mask = bytes(random.getrandbits(8) for _ in range(4))
        header += mask
        masked = bytes(c ^ mask[i % 4] for i, c in enumerate(payload))
        self.sock.sendall(bytes(header) + masked)

    def send_text(self, text: str) -> None:
        self._send_frame(_OP_TEXT, text.encode("utf-8"))

    def readable(self, timeout: float = 0.0) -> bool:
        """True if a frame is (at least partly) waiting to be read."""
        if self._buf:
            return True
        r, _, _ = select.select([self.sock], [], [], timeout)
        return bool(r)

    def close(self) -> None:
        if self.closed:
            return
        self.closed = True
        try:
            self._send_frame(_OP_CLOSE, b"")
        except OSError:
            pass
        try:
            self.sock.close()
        except OSError:
            pass


# --------------------------------------------------------------------------------------
# CDP session + page
# --------------------------------------------------------------------------------------


class Page:
    """A single Chrome page target, driven over one CDP WebSocket."""

    def __init__(self, ws: WSClient, settle: float = DEFAULT_SETTLE):
        self._ws = ws
        self._id = 0
        self._events: list[dict] = []
        self._errors: list[tuple[str, str]] = []
        self.settle = settle
        self._domains_enabled = False

    # -- protocol ----------------------------------------------------------------------

    def send(self, method: str, params: dict | None = None, timeout: float = 60.0) -> dict:
        """Issue a CDP command and return its `result` dict.

        Any event messages that arrive before the reply are buffered (and error-bearing
        ones harvested) rather than dropped.
        """
        self._id += 1
        want = self._id
        self._ws.send_text(json.dumps({"id": want, "method": method, "params": params or {}}))

        deadline = time.time() + timeout
        while True:
            if time.time() > deadline:
                raise CDPError("timed out waiting for reply to %s" % method)
            msg = json.loads(self._ws.recv())
            if msg.get("id") == want:
                if "error" in msg:
                    err = msg["error"]
                    raise CDPError(
                        "%s failed: %s (code %s)"
                        % (method, err.get("message"), err.get("code"))
                    )
                return msg.get("result", {})
            if "id" in msg:
                continue  # a reply to something we already gave up on
            self._on_event(msg)

    def _on_event(self, msg: dict) -> None:
        self._events.append(msg)
        self._harvest(msg)

    def drain(self, timeout: float = 0.05) -> None:
        """Pull any events already sitting on the socket, without blocking meaningfully."""
        while self._ws.readable(timeout):
            msg = json.loads(self._ws.recv())
            if "id" in msg:
                continue
            self._on_event(msg)

    def _wait_event(self, method: str, timeout: float = 30.0) -> dict | None:
        for ev in self._events:
            if ev.get("method") == method:
                return ev
        deadline = time.time() + timeout
        while time.time() < deadline:
            if not self._ws.readable(0.05):
                continue
            msg = json.loads(self._ws.recv())
            if "id" in msg:
                continue
            self._on_event(msg)
            if msg.get("method") == method:
                return msg
        return None

    # -- error harvesting --------------------------------------------------------------

    def _harvest(self, msg: dict) -> None:
        method = msg.get("method")
        p = msg.get("params", {}) or {}

        if method == "Log.entryAdded":
            entry = p.get("entry", {}) or {}
            if entry.get("level") == "error":
                where = entry.get("url") or entry.get("source") or ""
                self._errors.append(
                    ("Log", ("%s %s" % (entry.get("text", ""), where)).strip())
                )

        elif method == "Console.messageAdded":
            m = p.get("message", {}) or {}
            if m.get("level") == "error":
                self._errors.append(("Console", str(m.get("text", ""))))

        elif method == "Runtime.consoleAPICalled":
            if p.get("type") in ("error", "assert"):
                parts = []
                for a in p.get("args", []) or []:
                    if "value" in a:
                        parts.append(str(a["value"]))
                    elif a.get("description"):
                        parts.append(str(a["description"]))
                    else:
                        parts.append(str(a.get("type", "?")))
                self._errors.append(("console.%s" % p.get("type"), " ".join(parts)))

        elif method == "Runtime.exceptionThrown":
            d = (p.get("exceptionDetails") or {})
            exc = d.get("exception") or {}
            text = exc.get("description") or d.get("text") or "uncaught exception"
            url = d.get("url") or ""
            line = d.get("lineNumber")
            loc = (" (%s:%s)" % (url, line)) if url else ""
            self._errors.append(("exception", "%s%s" % (text, loc)))

    def console_errors(self) -> list[str]:
        """Console errors + uncaught exceptions seen since the last navigation."""
        # Round-trip a trivial command so anything Chrome has queued is flushed to us
        # ahead of the reply, then sweep whatever is left on the socket.
        try:
            self.send("Runtime.evaluate", {"expression": "1", "returnByValue": True})
        except CDPError:
            pass
        self.drain(0.05)

        out: list[str] = []
        seen: set[str] = set()
        for source, text in self._errors:
            key = text.strip()
            if key in seen:
                continue
            seen.add(key)
            out.append("[%s] %s" % (source, key))
        return out

    # -- navigation --------------------------------------------------------------------

    def _enable_domains(self) -> None:
        if self._domains_enabled:
            return
        self.send("Page.enable")
        self.send("Runtime.enable")
        self.send("Log.enable")
        try:
            self.send("Console.enable")  # deprecated domain; absent in some builds
        except CDPError:
            pass
        self._domains_enabled = True

    def goto(self, url: str, settle: float | None = None, timeout: float = 30.0) -> "Page":
        self._enable_domains()
        self._events.clear()
        self._errors.clear()

        self.send("Page.navigate", {"url": url})
        if self._wait_event("Page.loadEventFired", timeout=timeout) is None:
            raise CDPError("no Page.loadEventFired for %s within %.0fs" % (url, timeout))

        time.sleep(self.settle if settle is None else settle)

        # Let webfonts finish before anyone measures or screenshots.
        try:
            self.eval("document.fonts.ready.then(function(){return true;})")
        except (CDPError, JSError):
            pass

        self.drain(0.05)
        return self

    # -- evaluation --------------------------------------------------------------------

    def eval(self, expr: str, timeout: float = 30.0):
        res = self.send(
            "Runtime.evaluate",
            {
                "expression": expr,
                "returnByValue": True,
                "awaitPromise": True,
                "userGesture": True,
            },
            timeout=timeout,
        )
        if "exceptionDetails" in res:
            d = res["exceptionDetails"]
            exc = d.get("exception") or {}
            raise JSError(exc.get("description") or d.get("text") or "JS exception")
        return (res.get("result") or {}).get("value")

    # -- viewport + screenshots --------------------------------------------------------

    def set_viewport(self, width: int, height: int, settle: float = 0.15) -> None:
        """Force a CSS layout width/height. This — not --window-size — is what makes a
        genuine 390px mobile layout possible in headless Chrome."""
        self.send(
            "Emulation.setDeviceMetricsOverride",
            {
                "width": int(width),
                "height": int(height),
                "deviceScaleFactor": 1,
                "mobile": False,
            },
        )
        if settle:
            time.sleep(settle)

    def screenshot(
        self,
        path: str,
        width: int = 1280,
        height: int = 900,
        full_page: bool = True,
        settle: float = 0.15,
    ) -> str:
        self.set_viewport(width, height, settle=settle)

        clip_h = int(height)
        if full_page:
            # ⚠️ MEASURE UNTIL IT STOPS MOVING, then clip.
            #
            # Reading cssContentSize once, straight after the viewport
            # override, is a race: the override triggers a re-layout, and a
            # long page can report an intermediate height. Observed on a KS4
            # bonding page — 5840 on one capture and 6354 on the next, from the
            # same bytes, which made every full-page screenshot of it useless
            # for comparison and looked exactly like a real rendering
            # difference. The page was innocent; the measurement was early.
            #
            # So poll until two consecutive reads agree, then capture. Cheap,
            # and it turns a flaky screenshot into a deterministic one.
            last = None
            for _ in range(20):
                metrics = self.send("Page.getLayoutMetrics")
                css = (metrics.get("cssContentSize")
                       or metrics.get("contentSize") or {})
                h = int(math.ceil(css.get("height") or height))
                if h == last:
                    break
                last = h
                time.sleep(0.1)
            clip_h = max(1, min(last or int(height), MAX_CLIP_HEIGHT))

        res = self.send(
            "Page.captureScreenshot",
            {
                "format": "png",
                "captureBeyondViewport": True,
                "fromSurface": True,
                "clip": {
                    "x": 0,
                    "y": 0,
                    "width": int(width),
                    "height": clip_h,
                    "scale": 1,
                },
            },
        )
        data = base64.b64decode(res["data"])
        d = os.path.dirname(os.path.abspath(path))
        if d:
            os.makedirs(d, exist_ok=True)
        with open(path, "wb") as fh:
            fh.write(data)
        return path


# ⊕ MRB-245 — every started, not-yet-closed Browser.
#
# The harness contract asks for a FRESH BROWSER PER PAGE, so a run opens dozens.
# Any path that skips `close()` — an assertion inside a `with`, a gate that
# raises, a caller that simply forgets — used to leak a whole Chrome process
# group and its profile directory each time. At roughly 60 MB apiece that filled
# a 228 GB volume during a single verify run on 17 Aug 2026 and took two
# sessions' Bash down with `ENOSPC`.
#
# A plain `set` and not a `WeakSet`: a Browser nobody references any more is
# exactly the one whose Chrome is still running with nobody left to stop it, and
# letting it be collected is how the leak stayed invisible. `close()` discards
# its own entry, so a well-behaved caller leaves nothing here.
_LIVE: set["Browser"] = set()


@atexit.register
def _close_live_browsers() -> None:
    """Last resort at interpreter shutdown. Never raises."""
    for b in list(_LIVE):
        try:
            b.close()
        except Exception:
            pass


class Browser:
    """Launch, own, and tear down a headless Chrome instance."""

    def __init__(self, chrome: str = CHROME, settle: float = DEFAULT_SETTLE,
                 launch_timeout: float = 20.0, extra_args: list[str] | None = None):
        self.chrome = chrome
        self.settle = settle
        self.launch_timeout = launch_timeout
        self.extra_args = list(extra_args or [])
        self.port: int | None = None
        self.proc: subprocess.Popen | None = None
        self.user_data_dir: str | None = None
        self._ws: WSClient | None = None
        self._page: Page | None = None

    # -- lifecycle ---------------------------------------------------------------------

    @staticmethod
    def _free_port() -> int:
        s = socket.socket()
        try:
            s.bind(("127.0.0.1", 0))
            return s.getsockname()[1]
        finally:
            s.close()

    def start(self) -> "Browser":
        if not os.path.exists(self.chrome):
            raise CDPError("chrome not found at %s" % self.chrome)
        self.port = self._free_port()
        self.user_data_dir = tempfile.mkdtemp(
            prefix=_PROFILE_PREFIX, dir=gate_tmp())
        # Stamp the owner so `sweep_orphan_profiles()` can tell a live
        # profile from the wreckage of a killed run.
        try:
            with open(os.path.join(self.user_data_dir, _OWNER_FILE), "w",
                      encoding="utf-8") as fh:
                fh.write(str(os.getpid()))
        except OSError:
            pass
        args = [
            self.chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            "--remote-debugging-port=%d" % self.port,
            "--user-data-dir=%s" % self.user_data_dir,
            # ⊕ MRB-270. `--user-data-dir` does NOT move Chrome's HTTP cache.
            # That goes to `~/Library/Caches/Google/Chrome-headless`, one
            # `scoped_dir*` per launch, and it is never cleaned by anything —
            # 129 of them were sitting there from the runs that preceded this
            # fix. Pointing it INSIDE the profile means the existing teardown
            # already removes it and no new path can accumulate behind us.
            "--disk-cache-dir=%s" % os.path.join(self.user_data_dir, "hcache"),
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
        ] + self.extra_args + ["about:blank"]
        # ⊕ MRB-245 — `start_new_session` puts Chrome in its OWN process group,
        # so `close()` can signal the group and take the helper and renderer
        # processes with it. Without it, `terminate()` reaches only the parent
        # and every helper reparents to init still holding the profile
        # directory open. See `close()`.
        self.proc = subprocess.Popen(
            args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        # A Browser that is never closed — an exception between `start()` and
        # `close()`, or a caller that simply forgets — used to leak both the
        # process group and the profile directory until the volume filled.
        _LIVE.add(self)
        self._await_devtools()
        return self

    def _http_json(self, path: str, timeout: float = 3.0):
        url = "http://127.0.0.1:%d%s" % (self.port, path)
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))

    def _await_devtools(self) -> None:
        deadline = time.time() + self.launch_timeout
        last = None
        while time.time() < deadline:
            if self.proc.poll() is not None:
                raise CDPError("chrome exited with code %s during launch" % self.proc.returncode)
            try:
                self._http_json("/json/version")
                return
            except (urllib.error.URLError, OSError, ValueError) as e:
                last = e
                time.sleep(0.1)
        raise CDPError("devtools endpoint never came up on port %s (%s)" % (self.port, last))

    def _page_ws_url(self, timeout: float = 10.0) -> str:
        deadline = time.time() + timeout
        while time.time() < deadline:
            for t in self._http_json("/json/list"):
                if t.get("type") == "page" and t.get("webSocketDebuggerUrl"):
                    return t["webSocketDebuggerUrl"]
            # No page target (rare): ask for one. Newer Chrome wants PUT for /json/new.
            try:
                req = urllib.request.Request(
                    "http://127.0.0.1:%d/json/new?about:blank" % self.port, method="PUT"
                )
                with urllib.request.urlopen(req, timeout=3.0) as r:
                    t = json.loads(r.read().decode("utf-8"))
                if t.get("webSocketDebuggerUrl"):
                    return t["webSocketDebuggerUrl"]
            except (urllib.error.URLError, OSError, ValueError):
                pass
            time.sleep(0.2)
        raise CDPError("no page target with a webSocketDebuggerUrl appeared")

    def attach(self) -> Page:
        """Connect to (or reuse the connection to) the single page target."""
        if self._page is not None:
            return self._page
        if self.proc is None:
            self.start()
        self._ws = WSClient(self._page_ws_url())
        self._page = Page(self._ws, settle=self.settle)
        return self._page

    def page(self, url: str, settle: float | None = None) -> Page:
        """Navigate the browser's page target to `url` and return it, loaded and settled."""
        return self.attach().goto(url, settle=settle)

    def _signal_group(self, sig) -> bool:
        """Signal Chrome's whole process group. False if it is already gone.

        The group is ours alone — `start_new_session=True` made this child a
        session leader, so its pgid IS its pid and nothing else can be in it.
        That is what makes this safe: it can never reach a Chrome the user is
        running themselves.
        """
        try:
            os.killpg(os.getpgid(self.proc.pid), sig)
            return True
        except (ProcessLookupError, PermissionError, OSError):
            # Already reaped, or we never got our own group. Fall back to the
            # single process rather than giving up on the teardown.
            try:
                self.proc.send_signal(sig)
                return True
            except (ProcessLookupError, OSError):
                return False

    def close(self) -> None:
        """Tear down Chrome AND its helpers, then the profile directory.

        ⊕ MRB-245. This used to `terminate()` only `self.proc`. Chrome's helper
        and renderer processes are its children, so SIGTERM to the parent alone
        left them orphaned to init with the profile directory still open —
        roughly 60 MB a page, and the harness contract asks for a FRESH BROWSER
        PER PAGE. Across a full `verify_ks3.py` run that filled a 228 GB volume
        to 100% and took the machine's Bash down with it, in this session and in
        another running beside it. The profile dirs then could not be removed
        either, because their owners were still alive.

        Signalling the process group fixes both halves: the helpers die with the
        parent, and `rmtree` then succeeds because nothing holds the directory.
        """
        if self._ws is not None:
            try:
                self._ws.close()
            except OSError:
                pass
            self._ws = None
        self._page = None
        if self.proc is not None:
            if self.proc.poll() is None:
                self._signal_group(signal.SIGTERM)
                deadline = time.time() + 5.0
                while time.time() < deadline and self.proc.poll() is None:
                    time.sleep(0.05)
                if self.proc.poll() is None:
                    self._signal_group(signal.SIGKILL)
                    try:
                        self.proc.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        pass
            else:
                # The parent exited on its own, which is the case that leaked
                # most quietly: `poll()` reports it gone while the helpers it
                # spawned are still running. Sweep the group regardless.
                self._signal_group(signal.SIGKILL)
            self.proc = None
        if self.user_data_dir:
            shutil.rmtree(self.user_data_dir, ignore_errors=True)
            self.user_data_dir = None
        _LIVE.discard(self)

    def __enter__(self) -> "Browser":
        return self.start()

    def __exit__(self, *exc) -> bool:
        self.close()
        return False


# --------------------------------------------------------------------------------------
# static file server
# --------------------------------------------------------------------------------------


def serve(directory: str, port: int = 0):
    """Serve `directory` over HTTP on a background daemon thread. Returns (server, port)."""
    import http.server

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=directory, **kw)

        def log_message(self, fmt, *args):  # silence
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, server.server_address[1]


# --------------------------------------------------------------------------------------
# helpers usable by callers (and by the self-test)
# --------------------------------------------------------------------------------------


def png_size(path: str) -> tuple[int, int]:
    """(width, height) straight out of the PNG IHDR chunk. Stdlib only, no PIL."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:4] != b"\x89PNG":
        raise ValueError("%s is not a PNG (magic %r)" % (path, head[:4]))
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


# --------------------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------------------

_SELF_TEST_HTML = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>cdp self test</title>
<style>
  /* no webfonts anywhere: system stack only, so layout is deterministic */
  html, body { margin: 0; padding: 0; font-family: -apple-system, sans-serif; }
  body { background: rgb(250, 247, 240); }
  #t { color: rgb(1, 2, 3); padding: 24px; font-size: 20px; }
  #tall { height: 1400px; background: rgb(200, 90, 30); }
  #probe { padding: 8px; }
</style>
</head>
<body>
  <div id="t">known colour probe</div>
  <div id="probe">w=<span id="w"></span></div>
  <div id="tall"></div>
  <script>
    document.getElementById('w').textContent = String(window.innerWidth);
    window.addEventListener('resize', function () {
      document.getElementById('w').textContent = String(window.innerWidth);
    });
    console.error("BOOM");
  </script>
  <script>
    throw new Error("KABOOM deliberate");
  </script>
</body>
</html>
"""


def _self_test() -> int:
    failures: list[str] = []
    tmp = tempfile.mkdtemp(prefix="cdp-selftest-")
    server = None
    try:
        with open(os.path.join(tmp, "x.html"), "w") as fh:
            fh.write(_SELF_TEST_HTML)

        server, port = serve(tmp)
        url = "http://127.0.0.1:%d/x.html" % port
        shot_wide = os.path.join(tmp, "wide.png")
        shot_narrow = os.path.join(tmp, "narrow.png")

        with Browser() as b:
            p = b.page(url)

            # 1. computed style round-trip
            colour = p.eval("getComputedStyle(document.getElementById('t')).color")
            if colour != "rgb(1, 2, 3)":
                failures.append("computed colour: expected 'rgb(1, 2, 3)', got %r" % (colour,))

            title = p.eval("document.title")
            if title != "cdp self test":
                failures.append("document.title: expected 'cdp self test', got %r" % (title,))

            # 2. desktop screenshot: exists, is a PNG, IHDR width == 1280
            p.screenshot(shot_wide, width=1280)
            if not os.path.exists(shot_wide) or os.path.getsize(shot_wide) == 0:
                failures.append("1280 screenshot was not written")
            else:
                with open(shot_wide, "rb") as fh:
                    magic = fh.read(4)
                if magic != b"\x89PNG":
                    failures.append("1280 screenshot magic bytes: expected b'\\x89PNG', got %r"
                                    % (magic,))
                else:
                    w, h = png_size(shot_wide)
                    if w != 1280:
                        failures.append("1280 screenshot IHDR width: expected 1280, got %d" % w)
                    if h <= 900:
                        failures.append("full-page capture looks cropped: IHDR height %d, "
                                        "expected > 900 for a 1400px-tall block" % h)

            # 3. narrow screenshot: IHDR width EXACTLY 390 (not floored to ~500), and the
            #    page itself must agree it is laid out at 390 CSS px.
            p.screenshot(shot_narrow, width=390, height=844)
            inner = p.eval("window.innerWidth")
            if inner != 390:
                failures.append("narrow layout width: window.innerWidth is %r, expected 390 "
                                "(a window-size floor would report ~500)" % (inner,))
            if not os.path.exists(shot_narrow):
                failures.append("390 screenshot was not written")
            else:
                w390, h390 = png_size(shot_narrow)
                if w390 != 390:
                    failures.append("390 screenshot IHDR width: expected exactly 390, got %d "
                                    "(headless window floor not bypassed)" % w390)

            # 4. console errors
            errs = p.console_errors()
            if not any("BOOM" in e for e in errs):
                failures.append("console_errors() has no BOOM; got %r" % (errs,))
            if not any("KABOOM" in e for e in errs):
                failures.append("console_errors() has no thrown error; got %r" % (errs,))
    except Exception as e:  # noqa: BLE001 - the self-test reports, it does not propagate
        import traceback
        failures.append("harness raised %s: %s" % (type(e).__name__, e))
        traceback.print_exc()
    finally:
        if server is not None:
            server.shutdown()
            server.server_close()
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        for f in failures:
            print("FAIL: %s" % f)
        return 1
    print("SELF-TEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(_self_test())
