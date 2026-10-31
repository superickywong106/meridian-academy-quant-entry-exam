"""Task 2: Recompute Sharpe honestly with costs.

`data/sim_strategy_pnl.csv` has optimistic gross returns and a cost in bps.
Reported Sharpe uses gross only; audited Sharpe subtracts costs first.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "sim_strategy_pnl.csv"


def load_pnl(path: Path = DATA) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def _ann_sharpe(rets: list[float], periods_per_year: float = 252.0) -> float:
    if len(rets) < 2:
        return float("nan")
    mean = sum(rets) / len(rets)
    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
    sd = math.sqrt(var)
    if sd == 0:
        return float("nan")
    return (mean / sd) * math.sqrt(periods_per_year)


def reported_sharpe(rows: list[dict[str, str]]) -> float:
    """Naive Sharpe on gross returns only (the lie)."""
    rets = [float(r["gross_ret"]) for r in rows]
    return _ann_sharpe(rets)


def audited_sharpe(rows: list[dict[str, str]]) -> float:
    """Sharpe after subtracting cost_bps / 1e4 from each period return."""
    rets = []
    for r in rows:
        g = float(r["gross_ret"])
        cost = float(r["cost_bps"]) / 10_000.0
        rets.append(g - cost)
    return _ann_sharpe(rets)


def haircut(rows: list[dict[str, str]]) -> float:
    """reported - audited (positive when costs hurt)."""
    return reported_sharpe(rows) - audited_sharpe(rows)
