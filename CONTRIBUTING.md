# Contributing to Replica Codex

This is a community-maintained Codex distribution derived from [Jake Schincariol's Replica Skill](https://github.com/Jakeschincariol/replica-skill), licensed under MIT. Contributions are centralized through **Issues and Pull Requests to this repository's main branch**. Public GitHub forks cannot be disabled; please propose improvements upstream to this project's canonical repository rather than maintaining divergent releases.

## Before opening a PR

- Check existing Issues; include your Codex CLI or VS Code extension version and OS in bug reports.
- Create a branch from `main`; name it `feat/`, `fix/`, `docs/` or `test/`.
- Edit `scripts/prepare_codex.py`, not generated `.agents/skills` files, for adapter changes. Regenerate with `python scripts/prepare_codex.py prepare --force`.
- Run `python scripts/prepare_codex.py check` and `python -m unittest discover -s tests -v`.
- Include a focused test and a description of how the fix was validated.

## Original project updates

This is a standalone repository, not a GitHub fork. Proposed synchronization changes should separately cite the original MIT-licensed commit, preserve copyrights, include the original license, and regenerate all skills. Avoid silently replacing community fixes.

## Security and rights

Never include tokens, credentials, private customer data, proprietary code, images, or trademarks. Observe authorization and terms when researching third-party apps. Deploy only with user approval. By contributing you agree that your contribution may be distributed under the repository's MIT license.