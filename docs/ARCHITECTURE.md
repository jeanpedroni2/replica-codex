# Architecture

- `replica-*/`: upstream source skills, templates and Python helpers (MIT license).
- `.agents/skills/replica-*/`: generated Codex-compatible Agent Skills.
- `scripts/prepare_codex.py`: deterministic source-to-Codex adapter, validation and global installer.
- `tests/`: original helper tests and adapter tests.
- `.github/workflows/ci.yml`: automated checks for Python 3.10 and 3.12.

The original skills and helper tools stay intact at the root to simplify tracking upstream improvements. Codex adaptations replace Claude-specific paths and slash command references while retaining instructions about ethical reuse and rights.
