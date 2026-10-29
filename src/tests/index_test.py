import contextlib
import io
import runpy
import unittest
from pathlib import Path

from index import main


class TestIndex(unittest.TestCase):
    def test_main_prints_warehouse_operations(self):
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            main()

        printed = output.getvalue()
        self.assertIn("Luonnin jälkeen:", printed)
        self.assertIn("Olutvarasto: saldo = 20.2, vielä tilaa 79.8", printed)
        self.assertIn("Mehuvarasto: saldo = 50.7, vielä tilaa 49.3", printed)
        self.assertIn("saatiin 100.0", printed)
        self.assertIn("saatiin 0.0", printed)

    def test_script_entry_point_runs_demo(self):
        script = Path(__file__).resolve().parents[1] / "index.py"
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            runpy.run_path(str(script), run_name="__main__")

        self.assertIn("Virhetilanteita:", output.getvalue())
        self.assertIn("mehua.otaVarastosta(-32.9)", output.getvalue())
