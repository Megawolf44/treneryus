# Copilot Instructions for Avtokliker

## Purpose
A small Windows-focused automation demo that demonstrates how to use Python with AutoHotkey (AHK) via the `ahk` PyPI package. The repo is intentionally minimal — the canonical examples are `klicer.py` (mouse movement demo) and `.venv/example.py` (hotkey demo).

---

## Architecture & Big Picture 🔧
- **Single-file examples**: This repository is not a packaged library — automation examples live at the repository root (`klicer.py`, `example.py` inside `.venv/`).
- **Runtime model**: Scripts instantiate an `AHK()` client and call imperative AHK methods (e.g., `mouse_move`, `add_hotkey`, `start_hotkeys`, `block_forever`). Actions execute against the OS input device.
- **Why this shape**: The goal is a minimal, easy-to-run demo for Windows automation. Keep logic small and observable (short functions, direct AHK calls) so behaviors are easy to test manually.

---

## Quick setup & run (Windows) ✅
1. Create and activate a venv:
   - python -m venv .venv
   - .venv\Scripts\activate
2. Install dependencies (use `ahk[binary]` if you don't have AutoHotkey installed):
   - pip install ahk
   - pip install "ahk[binary]"
3. Run the demo:
   - python klicer.py
   - Or: & C:/path/to/.venv/Scripts/python.exe ./klicer.py

---

## Key developer workflows 🛠️
- Debugging in VS Code: set the Python interpreter to `.venv` and run `klicer.py` directly. Automation will move your mouse — keep a quick abort strategy (move mouse to corner / have an Escape hotkey in a separate process).
- Hotkeys & long-running processes: review `.venv/example.py` to see `ahk.add_hotkey` and `ahk.block_forever()` usage.
- Tests: none currently. If adding tests, use `pytest` and put tests under `tests/`. Mark/pin tests that require real input as skipped by default (use pytest markers like `@pytest.mark.skipif(os.name != 'nt', reason='Windows only')`).

---

## Project-specific patterns & conventions 📐
- Keep automation logic small and explicit: prefer short functions that call AHK methods directly so it's obvious when UI input will occur.
- Use **`blocking=True`** for AHK calls when order matters:

  ```python
  ahk.mouse_move(x=150, y=150, blocking=True)
  ahk.mouse_move(x=300, y=300, speed=100, blocking=True)
  ```

- Hotkey example:

  ```python
  def my_callback():
      print(os.system("taskkill /im autohotkey.exe"))

  ahk.add_hotkey('^n', callback=my_callback)
  ahk.start_hotkeys()
  ahk.block_forever()
  ```

- Safety note: the repo intentionally warns about dangerous uses of `taskkill`. **Do not** kill arbitrary processes. The example shows `taskkill /im autohotkey.exe` only as a way to terminate local AHK instances — avoid general `taskkill` usage in contributions.
- Code comments: existing comments in `klicer.py` are written in Russian — preserve locale and any non-ASCII comments when editing.

---

## Integration points & gotchas ⚠️
- AHK interacts with OS input: automation can steal focus and move the cursor. When adding code, keep side effects small and provide opt-out flags or simulation modes where possible.
- Admin rights: some AHK/system interactions may require elevated privileges. Document required elevation in the PR or commit message.
- Binary vs client: the project works with either an installed AutoHotkey binary or the `ahk[binary]` wheel — confirm both workflows in any changes.

---

## Files to inspect (quick list) 📁
- `klicer.py` — canonical mouse-moving demo, demonstrates `AHK()` usage and `mouse_move`.
- `.venv/example.py` — hotkey demo and `taskkill` warning.

---

## When contributing 👇
- Keep changes small and reversible. Add tests for logic that doesn't rely on moving the cursor. For any automation that performs input, add an explicit `--dry-run` or `--simulate` mode.
- Document changes in PR: list any new permissions or external dependencies (e.g., requiring AHK binary vs `ahk[binary]`).

---

If you want, I can add a short `README.md` and a template `tests/test_smoke.py` that includes a skip marker for Windows-only, or expand the `copilot-instructions` with example PR templates. Feedback welcome! 👋

