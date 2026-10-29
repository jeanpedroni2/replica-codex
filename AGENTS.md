# Replica Codex - repository instructions

This repository is a standalone MIT-licensed Codex distribution derived from [Jake Schincariol's Replica Skill](https://github.com/Jakeschincariol/replica-skill). Do not remove the original copyright or MIT LICENSE.

## Organization

- `replica-*` root directories hold original MIT-licensed skill source.
- `.agents/skills/replica-*` directories are generated Codex copies. Regenerate via `python scripts/prepare_codex.py prepare --force` after source updates.
- `scripts/prepare_codex.py` owns compatibility transformations and must be tested.
- `tests/test_codex_adapter.py` covers adaptation; other tests cover source helpers.
- The target application's outputs belong in that target project's `replica/` directory, not the framework repository.

## Workflow

1. Pick the relevant `$replica-*` skill and read its `SKILL.md`; reuse existing output from earlier steps.
2. Do not invent browsing, screenshot inspection, deployment, access to APIs, or test results.
3. Observe third-party copyright and trademarks; recreate workflows and features with original code, assets and branding.
4. Require explicit approval for external publishing, production deployment, purchases or destructive modifications.
5. Run `python scripts/prepare_codex.py check` and `python -m unittest discover -s tests -v` after code changes.

## Contributions

- Keep MIT notices and original author attribution intact.
- Avoid committing credentials, private data, or copyrighted third-party materials.
- Use reviewable feature branches and Pull Requests against the canonical `main` branch.