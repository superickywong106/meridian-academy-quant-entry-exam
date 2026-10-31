from datetime import date

from exam.pit_check import flag_pit_violations, is_available


def test_available_same_day():
    assert is_available(date(2024, 3, 15), date(2024, 3, 15)) is True


def test_not_available_future_release():
    assert is_available(date(2024, 3, 15), date(2024, 3, 16)) is False


def test_flag_indices():
    decisions = [
        (date(2024, 1, 10), date(2024, 1, 9)),   # ok
        (date(2024, 1, 10), date(2024, 1, 11)),  # violation
        (date(2024, 2, 1), date(2024, 2, 1)),    # ok
    ]
    assert flag_pit_violations(decisions) == [1]
