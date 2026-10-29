"""Tests of generated Codex skill structure and installation."""
from __future__ import annotations
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("codex_adapter", ROOT / "scripts" / "prepare_codex.py")
assert SPEC is not None and SPEC.loader is not None
adapter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(adapter)

class CodexTests(unittest.TestCase):
    def test_all_skills_available(self):
        self.assertEqual(len(adapter.SKILLS), 11)
        adapter.check()
        for name in adapter.SKILLS:
            path = ROOT / ".agents" / "skills" / name / "SKILL.md"
            self.assertIn("$" + name, path.read_text(encoding="utf-8"))

    def test_runtime_adaptation(self):
        source = "---\nname: replica-recon\ndescription: example\n---\n\nClaude /replica-recon ~/.claude/skills/\n"
        output = adapter.adapt_skill(source, "replica-recon")
        self.assertIn("$replica-recon", output)
        self.assertIn("~/.agents/skills/", output)
        self.assertIn("Codex ", output)

    def test_global_install_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "skills"
            adapter.install(destination)
            adapter.install(destination)
            self.assertTrue((destination / "replica-design" / "SKILL.md").exists())

    def test_license_attribution(self):
        license_text = (ROOT / "docs" / "UPSTREAM_LICENSE.txt").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Jake Schincariol", license_text)
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
