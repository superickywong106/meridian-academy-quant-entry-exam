"""CLI: print task status for the Quant Entry exam scaffold."""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Meridian Quant Entry exam scaffold [SIM]")
    p.add_argument("--list-tasks", action="store_true", help="List starter tasks")
    args = p.parse_args(argv)
    print("Meridian Academy · Quant Entry exam repo (prototype scaffold)")
    print("Data root:", ROOT / "data")
    print("All market figures are educational [SIM] synthetic data.")
    if args.list_tasks or True:
        print()
        print("Starter tasks (see exam/*.py and tests/):")
        print("  1. detect_lookahead — find look-ahead join / leaky feature")
        print("  2. sharpe_honesty  — recompute Sharpe with costs")
        print("  3. pit_check       — point-in-time availability check")
        print()
        print("Run: pytest -q")
        print("MC bank: see QUESTIONS.md (stub — AIESGcourse maker)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
