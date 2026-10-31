# Quant Entry — public certificate exam repo (pedagogy outline)

**Live repo:** https://github.com/superickywong106/meridian-academy-quant-entry-exam  
**Status:** Soft Packaging scaffold · synthetic [SIM] only · no broker keys · not a licence  
**Owner (pedagogy + keys):** course / assessments bot  
**Owner (Git layout wiring):** Website manager

Educational only. Figures illustrative. Not investment advice. Not a credential.

## Layout (keep existing folders; extend)

```
exam-repo-quant-entry/
  README.md                 ← this file
  Makefile                  ← targets below (Website manager scaffolds)
  data/
    synthetic/
      gt_market_seed42.parquet          # OHLCV + planted delists + same-bar trap labels
      fundamentals_pit_trap.parquet     # available_date in the future for some rows
      three_sleeves_seed7.parquet       # three high-corr “diverse” sleeves
      cost_stress_grid.json             # bps grid mirroring E7.3 teaching [SIM]
      golden_stamp_seed3.json           # expected Sharpes for primary seed
      golden_stamp_seed4_canary.json    # must differ — sticky stamp fails
  exam/
    tasks/
      01_leakage_lag.py                 # same-bar vs T+1
      02_pit_join.py                    # available_date filter
      03_tearsheet_honesty.py           # 1×/2× costs + baseline columns
      04_survivorship.py                # survivors-only vs PIT universe
      05_walkforward.py                 # freeze params per fold
      06_cost_stress.py                 # turnover × bps scenarios
      07_scaler_leak.py                 # train-only vs full-panel scaler
      08_golden_canary.py               # stamp + canary seed
      09_correlation_sleeves.py         # one-bet warning
    outputs/                            # gitignored JSON summaries
  tests/
    test_exam_leakage.py
    test_exam_pit.py
    test_exam_tearsheet.py
    test_exam_survivorship.py
    test_exam_walkforward.py
    test_exam_costs.py
    test_exam_scaler_leak.py
    test_exam_golden.py
    test_exam_corr.py
```

## Makefile targets (suggested)

| Target | What it checks pedagogically | Cert questions |
|--------|------------------------------|----------------|
| `make exam-leakage` | Same-bar vs T+1 on planted reversal/momentum | CERT-Q21 |
| `make exam-pit` | `available_date <= decision_date` coverage drop | CERT-Q22 |
| `make exam-tearsheet` | Net 1×/2× + baseline columns present | CERT-Q23 |
| `make exam-survivorship` | Survivors-only inflation vs PIT | CERT-Q24 |
| `make exam-walkforward` | Frozen params; fail if refit in test window | CERT-Q25 |
| `make exam-costs` | Stress grid; negative net near ~15 bp drag [SIM] | CERT-Q26 |
| `make exam-scaler-leak` | Train-only scaler passes; full-panel fails | CERT-Q27 |
| `make exam-golden` | Seed3 within tol; seed4 canary moves | CERT-Q28 |
| `make exam-corr` | Report corr + one-bet warning | CERT-Q29 |
| `make exam` / `pytest` | Full suite green | CERT-Q30 |

## Synthetic dataset notes

- All data **generated**, not vendor tapes. Tag outputs `[SIM]`.
- Plant **known** edges and **known** traps so tests are deterministic.
- Never require real broker credentials, paid vendor keys, or live orders.
- `gt_market_seed42.parquet`: columns at least `date, symbol, open, high, low, close, volume, is_delisted_future, ret_next_open`.
- `fundamentals_pit_trap.parquet`: `symbol, period_end, available_date, field, value` with some `available_date` after decision dates used in tasks.

## Candidate flow

1. Clone public repo  
2. `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`  
3. `make exam` (or `pytest -q`)  
4. Use printed/JSON summaries to answer repo-gated MC items on the site  
5. Site grades MC; repo green is a prerequisite honour system / optional CI badge — Website manager wires UX

## Keys & contested

Answer keys live in site file `quizzes/quant-entry-cert-exam.json` (server-side).  
`contested: []` at initial ship.

## Related

- Module quizzes: `../quizzes/E1.json` … `E10.json`
- Thresholds: `../quizzes/THRESHOLDS.md`
- Course mirror: `/workspace/aiesg-course/assessments/quant-entry/site/`

## Question bank pointer

See `QUESTIONS.md` for the delivered topic map; keys remain in `../quizzes/quant-entry-cert-exam.json` (server-side).
