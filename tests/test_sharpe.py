from exam.sharpe_honesty import audited_sharpe, haircut, load_pnl, reported_sharpe


def test_audited_below_reported():
    rows = load_pnl()
    rep = reported_sharpe(rows)
    aud = audited_sharpe(rows)
    assert rep > aud
    assert haircut(rows) > 0
