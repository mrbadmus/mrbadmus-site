"""launch_config.py — the consumer (B2C) launch decision, as committed config.

⊕ 1 Oct 2026. Replaces the old contract where the launch decision lived ONLY
in the environment variable `CONSUMER_SIGNUP_ENABLED`, read fresh by every
build with no memory between runs. That worked right up until a build ran
without the variable set — `64a0cb303` on 1 Oct 2026, a Design-port commit
with no reason to think about B2C at all — and silently un-launched
production: `mrbadmus_site/parents/*.html` grew back a `noindex` tag,
`sitemap.xml` and `robots.txt` disappeared, the consumer 404/error pages
disappeared, and `git status` showed it as a pile of deletions with nothing
in the commit message explaining why. The launch had been decided once, on
30 Sep 2026 (`37284388a`), and the next build that forgot to repeat the
incantation un-did it.

The fix: **the launch decision is COMMITTED CONFIG, not a build argument.**
It lives in `launch.json`, next to this file, and a plain
`python3 build_all.py` — no environment variable, no flag, nothing typed —
now reproduces the committed decision every time. The environment variable
still works, but it is now an EXPLICIT OVERRIDE for one build only, and it
says so loudly when it disagrees with what is committed, because a build
that silently overrides committed config is exactly the failure mode this
file exists to close.

── THE TWO FUNCTIONS ───────────────────────────────────────────────────────

`committed()`                — the decision `launch.json` carries, and
                                nothing else. Fails loudly, never silently
                                defaults, if the file is missing, unreadable,
                                missing the key, or the key is not literally
                                `true`/`false`.
`consumer_signup_enabled()`  — the EFFECTIVE decision for this process: the
                                committed value, unless `CONSUMER_SIGNUP_ENABLED`
                                is set in the environment to exactly "true" or
                                exactly "false", in which case that wins for
                                this one build and a banner says so.

Fail-closed spirit, kept from the old docstring this replaces: **there is
exactly one spelling of each value.** Not `1`, not `yes`, not `TRUE ` with a
trailing space — `true` or `false`, byte for byte, or the build stops rather
than guess.
"""

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
LAUNCH_JSON_PATH = os.path.join(_HERE, "launch.json")

_ENV_VAR = "CONSUMER_SIGNUP_ENABLED"


def committed():
    """The launch decision as COMMITTED in launch.json. Fail-closed.

    Any way this can go wrong — the file is missing, the JSON is malformed,
    the key is absent, or the key holds anything other than a real bool —
    raises SystemExit with a message that says exactly what is wrong. A
    missing or broken launch.json must never quietly mean "off": that is
    precisely the silent-default failure this file replaces.
    """
    if not os.path.exists(LAUNCH_JSON_PATH):
        raise SystemExit(
            "launch_config.py: launch.json is missing at %s — the consumer "
            "launch decision has nowhere to read from. Restore it; it is "
            "committed config, not an optional file." % LAUNCH_JSON_PATH)

    try:
        with open(LAUNCH_JSON_PATH, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(
            "launch_config.py: launch.json at %s is not readable/valid JSON "
            "(%s) — fix it before building. A broken launch.json must stop "
            "the build, not silently mean 'off'." % (LAUNCH_JSON_PATH, exc))

    if "consumer_signup_enabled" not in data:
        raise SystemExit(
            "launch_config.py: launch.json at %s has no "
            "\"consumer_signup_enabled\" key — the launch decision is "
            "undefined. Add it; do not guess." % LAUNCH_JSON_PATH)

    value = data["consumer_signup_enabled"]
    if not isinstance(value, bool):
        raise SystemExit(
            "launch_config.py: launch.json's \"consumer_signup_enabled\" is "
            "%r (a %s), not a real true/false — fix it. A non-bool value "
            "must stop the build, not be coerced." % (value, type(value).__name__))

    return value


def _env_override():
    """The raw environment override, or None if there isn't one.

    Exactly one spelling of each value, same contract as the committed
    config: the literal strings "true" and "false", nothing else. Unset or
    empty means "no override" — defer to committed(). Anything else (a
    typo, "1", "True", a trailing space) is ambiguous and must stop the
    build rather than be guessed at.
    """
    raw = os.environ.get(_ENV_VAR, "")
    if raw == "":
        return None
    if raw == "true":
        return True
    if raw == "false":
        return False
    raise SystemExit(
        "launch_config.py: %s=%r is not \"true\" or \"false\" — an "
        "ambiguous override must not build. Unset it to use the committed "
        "launch.json decision, or set it to exactly \"true\" or \"false\"."
        % (_ENV_VAR, raw))


def _override_banner(env_value, committed_value):
    print(
        "\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        "!!!!\n"
        "!!!!  %s=%s OVERRIDES THE COMMITTED LAUNCH DECISION.\n"
        "!!!!\n"
        "!!!!  launch.json says consumer_signup_enabled=%s for THIS build.\n"
        "!!!!  The environment variable is forcing %s instead, for this\n"
        "!!!!  build only — launch.json on disk is UNCHANGED.\n"
        "!!!!\n"
        "!!!!  DO NOT PUSH THIS OUTPUT TO main UNLESS THIS IS A DELIBERATE\n"
        "!!!!  LAUNCH OR UN-LAUNCH. An overridden build that lands on main\n"
        "!!!!  by accident un-launches (or re-launches) production with\n"
        "!!!!  nothing in the commit message explaining why — that is the\n"
        "!!!!  exact regression this file exists to stop.\n"
        "!!!!\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        % (_ENV_VAR, str(env_value).lower(), str(committed_value).lower(),
           str(env_value).lower()),
        file=sys.stderr,
    )


def consumer_signup_enabled():
    """The EFFECTIVE launch decision for this process.

    Unset or empty `CONSUMER_SIGNUP_ENABLED` → the committed decision,
    `launch.json`, unchanged. A set, valid override wins for this build only,
    and prints a loud banner to stderr when it disagrees with what is
    committed — silence would mean nothing on the terminal says "this output
    must not be pushed as-is".
    """
    committed_value = committed()
    env_value = _env_override()

    if env_value is None:
        return committed_value

    if env_value != committed_value:
        _override_banner(env_value, committed_value)

    return env_value


def describe():
    """One-line human string for a build's own header output."""
    committed_value = committed()
    try:
        env_value = _env_override()
    except SystemExit:
        # describe() is used for a readable header even when the override
        # itself is bad; let the real call that matters (consumer_signup_enabled)
        # be the one that stops the build.
        raw = os.environ.get(_ENV_VAR, "")
        return "consumer launch: UNKNOWN (env override %r is invalid)" % raw

    on_off = lambda b: "ON" if b else "OFF"

    if env_value is None:
        return "consumer launch: %s (launch.json)" % on_off(committed_value)

    if env_value == committed_value:
        return "consumer launch: %s (launch.json, env confirms)" % on_off(committed_value)

    return ("consumer launch: %s (env override; launch.json says %s)"
            % (on_off(env_value), on_off(committed_value)))
