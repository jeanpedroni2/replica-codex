# Replica Codex

**Eleven MIT-licensed Agent Skills for OpenAI Codex** to research, plan, develop, test and ship original applications.

This independent community distribution adapts [The Replica Skill](https://github.com/Jakeschincariol/replica-skill), created by **Jake Schincariol**. It is **not** an official OpenAI product and is **not registered as a GitHub fork**. The original copyright and MIT license are retained in [docs/UPSTREAM_LICENSE.txt](docs/UPSTREAM_LICENSE.txt), and [NOTICE.md](NOTICE.md) attributes the original work.

**Release status: v0.1.0 (preview).** Codex compatibility is implemented; an end-to-end evaluation of all 11 skills in live Codex sessions remains open for community validation.

## Install (Windows, macOS, Linux)

Requires Python 3.10+ and Git.

```bash
git clone https://github.com/jeanpedroni2/replica-codex.git
cd replica-codex
python scripts/prepare_codex.py check
python scripts/prepare_codex.py install
```

This installs the Codex-ready skills into `~/.agents/skills/`. Restart Codex if they are not visible. To install to another directory: `python scripts/prepare_codex.py install --dest /target/skills`. Use `--force` only after reviewing local changes.

## Start using a skill

In Codex CLI or the VS Code extension, ask:

> Use `$replica-recon` to document the permitted public flows of this scheduling app, then `$replica-architect` to plan a new Ruby on Rails + PostgreSQL + React implementation. Use only authorized material; do not copy source code or proprietary assets.

| Skill | What it does |
| --- | --- |
| `$replica-recon` | Map publicly inspectable user journeys and features |
| `$replica-architect` | Design the stack, API and database |
| `$replica-design` | Document original design tokens and UI components |
| `$replica-build` | Implement screens and flows |
| `$replica-backend` | Implement backend systems and integrations |
| `$replica-test` | Validate functionality and report bugs |
| `$replica-diff` | Measure feature and layout parity |
| `$replica-entrepreneur` | Research sourced user feedback and product differentiation |
| `$replica-brand` | Create original branding and detect source identifiers |
| `$replica-launch` | Prepare landing pages and store listings |
| `$replica-deploy` | Evaluate readiness and deploy with approval |

Typical flow: recon → architect → design → build → backend → test → diff → entrepreneur → brand → launch → deploy. Skills can be used separately.

## Development and verification

- Root folders `replica-*/` are copies of the upstream MIT-licensed source, including the original helper scripts.
- The generated Codex versions live in `.agents/skills/replica-*/`.
- `scripts/prepare_codex.py` regenerates the Codex versions and installs them globally.

```bash
python scripts/prepare_codex.py prepare --force
python scripts/prepare_codex.py check
python -m unittest discover -s tests -v
```

Python helper tools use the standard library. Do not modify source attribution.

## Community and ownership

Please use this repository's Issues and Pull Requests as the canonical development channel. See [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) and [NOTICE.md](NOTICE.md).

Public GitHub repositories **can be forked**; GitHub does not offer a switch to prohibit forks while keeping a normal repository public.

## Responsible use

Only study resources you may legally access, such as public documentation or your own authorized account. Recreate behavior with new code, branding and assets; do not copy proprietary code or circumvent access restrictions. Do not claim unverified tests or deploy without explicit authorization.
