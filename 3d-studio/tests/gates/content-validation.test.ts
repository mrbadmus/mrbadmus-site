// @vitest-environment node
// Gate 4 — Stage 0's content validation still passes. The validator is the
// build gate from MRB-185: presence, assets, lesson URLs, hotspot coordinate
// parity, single-name binding, naming discipline. Exit code 0 or this fails.

import { describe, expect, it } from 'vitest'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'

const STUDIO_DIR = fileURLToPath(new URL('../..', import.meta.url))

describe('gate 4 — Stage 0 content validation', () => {
  it('validate_content.py exits 0', () => {
    const result = spawnSync('python3', ['validate_content.py'], {
      cwd: STUDIO_DIR,
      encoding: 'utf8',
      timeout: 15000,
    })
    expect(result.error).toBeUndefined()
    expect(
      result.status,
      `validator failed:\n${result.stdout}\n${result.stderr}`,
    ).toBe(0)
    expect(result.stdout).toContain('all records valid')
  })
})
