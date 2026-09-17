"""Teste de integração local da demonstração, sem acesso ao Jira."""
import hashlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DemoTests(unittest.TestCase):
    def test_cli_preserva_base_e_relata_candidatos(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory) / "src"
            shutil.copytree(ROOT / "examples" / "demo" / "src", base)
            before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in base.glob("*.py")}
            report = Path(directory) / "report.md"
            run = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "analisar_repositorio.py"),
                 str(base), "--saida", str(report)],
                capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in base.glob("*.py")}
            self.assertEqual(before, after)
            text = report.read_text(encoding="utf-8")
            exact = text.split("## 1.")[1].split("## 2.")[0]
            self.assertIn("pricing_rules.py", exact)
            self.assertIn("pricing_backup.py", exact)
            partial = text.split("## 2.")[1].split("## 3.")[0]
            self.assertNotIn(" <-> ", partial)
            candidates = text.split("## 4.")[1].split("## Próximos passos")[0]
            self.assertIn("pricing_backup.py", candidates)
            self.assertIn("checkout_entry.py", candidates)
            self.assertNotIn("pricing_rules.py", candidates)


if __name__ == "__main__":
    unittest.main()
