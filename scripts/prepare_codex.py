#!/usr/bin/env python3
"""Regenerate, validate and install Replica Codex Agent Skills.

Derived skills preserve source instructions and helper scripts. No third-party
dependencies. The upstream root folders remain unmodified.
"""
from __future__ import annotations
import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "replica-recon", "replica-architect", "replica-design", "replica-build",
    "replica-backend", "replica-test", "replica-diff", "replica-entrepreneur",
    "replica-brand", "replica-launch", "replica-deploy",
)
GUIDANCE = "<!-- Replica Codex adapter: generated from the original MIT-licensed skill. -->\n\n## OpenAI Codex guidance\n\n- Invoke as `$SKILL_NAME` in Codex CLI or the VS Code extension.\n- Follow the target project's `AGENTS.md` and write artifacts into its `replica/` directory.\n- Locate companion scripts relative to this skill directory; do not assume a current working directory.\n- Use only tools actually available; never fabricate browser observations, API responses, test results or deployments.\n- Respect copyright, licenses, trademarks, privacy, authorized access, and site terms. Never copy proprietary source or assets.\n- Ask for explicit permission before purchases, deployment, publication or destructive changes.\n"

def adapt_skill(text: str, name: str) -> str:
    """Transform slash-commands and Claude paths into Codex Agent Skills."""
    if not text.startswith("---\n"):
        raise ValueError(f"Invalid YAML frontmatter in {name}")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise ValueError(f"Unclosed YAML frontmatter in {name}")
    head, body = text[:boundary + 5], text[boundary + 5:]
    if not re.search(r"(?m)^name:\s*" + re.escape(name) + r"\s*$", head):
        raise ValueError(f"Skill name mismatch: {name}")
    if not re.search(r"(?m)^description:\s*", head):
        raise ValueError(f"Missing skill description: {name}")
    body = body.replace("~/.claude/skills/", "~/.agents/skills/")
    body = body.replace(".claude/skills/", ".agents/skills/")
    body = re.sub(r"\bClaude\b", "Codex", body)
    body = re.sub(r"(?<![\w/])/(replica-[a-z-]+)", lambda m: "$" + m.group(1), body)
    return head + "\n" + GUIDANCE.replace("SKILL_NAME", name) + "\n" + body.lstrip()

def check() -> None:
    """Verify all generated content is in sync with original source."""
    base = ROOT / ".agents" / "skills"
    for name in SKILLS:
        source = ROOT / name
        target = base / name
        original = source / "SKILL.md"
        adapted = target / "SKILL.md"
        if not original.is_file() or not adapted.is_file():
            raise FileNotFoundError(f"Missing source/target skill: {name}")
        expected = adapt_skill(original.read_text(encoding="utf-8"), name)
        if adapted.read_text(encoding="utf-8") != expected:
            raise ValueError(f"Codex skill out of sync: {name}")
        for f in source.rglob("*"):
            if f.is_file() and f.name != "SKILL.md" and "__pycache__" not in f.parts and f.suffix != ".pyc":
                copy = target / f.relative_to(source)
                if not copy.exists() or copy.read_bytes() != f.read_bytes():
                    raise ValueError(f"Missing or differing helper: {name}/{f.name}")
    print("OK: 11 Codex skills and helpers verified")

def prepare(force: bool = False) -> None:
    """Regenerate skill copies after reviewing upstream source changes."""
    base = ROOT / ".agents" / "skills"
    for name in SKILLS:
        original = ROOT / name
        dest = base / name
        if not (original / "SKILL.md").is_file():
            raise FileNotFoundError(f"Missing source skill: {name}")
        transformed = adapt_skill((original / "SKILL.md").read_text(encoding="utf-8"), name)
        if dest.exists() and not force:
            if (dest / "SKILL.md").read_text(encoding="utf-8") == transformed:
                print("unchanged", name)
                continue
            raise FileExistsError(f"Generated skill has changed; use --force: {name}")
        if dest.exists():
            shutil.rmtree(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(original, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        (dest / "SKILL.md").write_text(transformed, encoding="utf-8")
        print("prepared", name)

def install(destination: Path, force: bool = False) -> None:
    """Install generated skills globally or into a designated directory."""
    check()
    destination = destination.expanduser().resolve()
    for name in SKILLS:
        source = ROOT / ".agents" / "skills" / name
        target = destination / name
        if target.exists() and not force:
            if (target / "SKILL.md").read_bytes() == (source / "SKILL.md").read_bytes():
                print("already installed", name)
                continue
            raise FileExistsError(f"Different installed version; review and pass --force: {name}")
        if target.exists():
            shutil.rmtree(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target)
        print("installed", name)

def main() -> int:
    parser = argparse.ArgumentParser(description="Replica Codex skill installer and validator")
    parser.add_argument("command", choices=("prepare", "check", "install"))
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills")
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            prepare(force=args.force)
        elif args.command == "install":
            install(args.dest, force=args.force)
        else:
            check()
        return 0
    except (ValueError, FileNotFoundError, FileExistsError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
