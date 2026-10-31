from exam.detect_lookahead import find_leaky_columns, load_rows, safe_feature_columns


def test_finds_leaky_feature():
    rows = load_rows()
    leaky = find_leaky_columns(rows)
    assert "feature_t_plus_1_LEAK" in leaky


def test_safe_features_exclude_leak():
    rows = load_rows()
    safe = safe_feature_columns(rows)
    assert "feature_t_plus_1_LEAK" not in safe
    assert "feature_t" in safe
