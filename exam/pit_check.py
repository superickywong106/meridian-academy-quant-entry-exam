"""Task 3: Point-in-time (PIT) availability check.

Given as-of timestamps for a feature release vs decision time, flag rows
where the feature was not yet published (classic PIT violation).
"""
from __future__ import annotations

from datetime import date


def is_available(decision_date: date, feature_available_on: date) -> bool:
    """Feature may be used only if available_on <= decision_date."""
    return feature_available_on <= decision_date


def flag_pit_violations(
    decisions: list[tuple[date, date]],
) -> list[int]:
    """decisions: list of (decision_date, feature_available_on).

    Returns indices where the feature was NOT yet available.
    """
    bad: list[int] = []
    for i, (dec, avail) in enumerate(decisions):
        if not is_available(dec, avail):
            bad.append(i)
    return bad
