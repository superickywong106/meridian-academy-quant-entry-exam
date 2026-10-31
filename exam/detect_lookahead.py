"""Task 1: Detect look-ahead in a feature column.

The CSV `data/sim_returns_leaky.csv` includes `feature_t_plus_1_LEAK`, which
equals next-period return — information not available at decision time.
Learners should identify leaky columns and refuse to train on them.
"""
from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "sim_returns_leaky.csv"


def load_rows(path: Path = DATA) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def find_leaky_columns(rows: list[dict[str, str]]) -> list[str]:
    """Return names of columns that match next-period return (look-ahead)."""
    if not rows:
        return []
    label_key = "label_next_ret"
    leaky: list[str] = []
    sample = rows[:20]
    for key in sample[0].keys():
        if key in ("date", "ret", label_key):
            continue
        matches = 0
        for row in sample:
            try:
                if abs(float(row[key]) - float(row[label_key])) < 1e-12:
                    matches += 1
            except (KeyError, ValueError):
                matches = 0
                break
        if matches == len(sample):
            leaky.append(key)
    return leaky


def safe_feature_columns(rows: list[dict[str, str]]) -> list[str]:
    leaky = set(find_leaky_columns(rows))
    keys = [k for k in rows[0].keys() if k not in ("date", "label_next_ret")]
    return [k for k in keys if k not in leaky]
