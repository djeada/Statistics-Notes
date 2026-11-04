"""Lesson 23 - Exponential smoothing models (SES, Holt, Holt-Winters additive) as row-by-row recursions."""
import math
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import INPUT_FILL, Book, Dash, md, write_csv  # noqa: E402
from _orders_story import orders_series, DAYNAMES  # noqa: E402

SLUG = "23-exponential-smoothing-models"
TITLE = "Exponential smoothing models"
MODULE = "Forecasting and model evaluation"
DATASET = "168 days of shop orders (2025-03-03 .. 2025-08-17), 140 training days + 28 holdout days"

N, TR, H = 168, 140, 28
LAST = TR + 1          # last training row in Excel (row = index + 2)
R7 = 8                 # row of t = 7, where the states are initialised
G = np.round(np.arange(0.01, 1.0, 0.01), 2)


def make_data() -> pd.DataFrame:
    # a campaign on 2025-05-26 (index 84) lifts the level by ~32 orders/day for good; weekday pattern 1.3x stronger than usual
    return orders_series("2025-03-03", N, 2309, base=140, lin=0.25, ar=0.2, sd=6, weekday_scale=1.3, shift_at=84,
                         shift_size=32)


# --------------------------------------------------------------------------- reference implementations (numpy)
def init(y):
    l0 = y[:7].mean()
    return l0, (y[7:14].mean() - l0) / 7.0, y[:7] - l0


def run_ses(y, a):
    l0, _, _ = init(y)
    lev, fc = np.full(N, np.nan), np.full(N, np.nan)
    l = l0
    lev[6] = l
    for t in range(7, TR):
        fc[t] = l
        l = a * y[t] + (1 - a) * l
        lev[t] = l
    fc[TR:] = l
    return lev, fc


def run_holt(y, a, bt):
    l, b, _ = init(y)
    lev, tr, fc = np.full(N, np.nan), np.full(N, np.nan), np.full(N, np.nan)
    lev[6], tr[6] = l, b
    for t in range(7, TR):
        fc[t] = l + b
        ln = a * y[t] + (1 - a) * (l + b)
        b = bt * (ln - l) + (1 - bt) * b
        l = ln
        lev[t], tr[t] = l, b
    fc[TR:] = [l + h * b for h in range(1, H + 1)]
    return lev, tr, fc


def run_hw(y, a, bt, g):
    l, b, s0 = init(y)
    lev, tr, se, fc = (np.full(N, np.nan) for _ in range(4))
    lev[6], tr[6] = l, b
    se[:7] = s0
    for t in range(7, TR):
        fc[t] = l + b + se[t - 7]
        ln = a * (y[t] - se[t - 7]) + (1 - a) * (l + b)
        se[t] = g * (y[t] - l - b) + (1 - g) * se[t - 7]
        b = bt * (ln - l) + (1 - bt) * b
        l = ln
        lev[t], tr[t] = l, b
    fc[TR:] = [l + h * b + se[TR - 7 + (h - 1) % 7] for h in range(1, H + 1)]
    return lev, tr, se, fc


def sse_of(y, fc):
    e = y[7:TR] - fc[7:TR]
    return float(np.sum(e ** 2))


# --------------------------------------------------------------------------- vectorised grid search (step 0.01)
def grid_ses(y):
    l0, _, _ = init(y)
    a = G
    l = np.full(a.shape, l0)
    sse = np.zeros(a.shape)
    for t in range(7, TR):
        sse += (y[t] - l) ** 2
        l = a * y[t] + (1 - a) * l
    i = int(sse.argmin())
    return float(sse[i]), (float(a[i]),)


def grid_holt(y):
    l0, b0, _ = init(y)
    A, B = (m.ravel() for m in np.meshgrid(G, G, indexing="ij"))
    l, b, sse = np.full(A.shape, l0), np.full(A.shape, b0), np.zeros(A.shape)
    for t in range(7, TR):
        f = l + b
        sse += (y[t] - f) ** 2
        ln = A * y[t] + (1 - A) * f
        b = B * (ln - l) + (1 - B) * b
        l = ln
    i = int(sse.argmin())
    return float(sse[i]), (float(A[i]), float(B[i]))


def grid_hw(y):
    l0, b0, s0 = init(y)
    A, B, C = (m.ravel() for m in np.meshgrid(G, G, G, indexing="ij"))
    l, b, sse = np.full(A.shape, l0), np.full(A.shape, b0), np.zeros(A.shape)
    s = [np.full(A.shape, v) for v in s0]
    for t in range(7, TR):
        st = s[t - 7]
        sse += (y[t] - (l + b + st)) ** 2
        ln = A * (y[t] - st) + (1 - A) * (l + b)
        s.append(C * (y[t] - l - b) + (1 - C) * st)
        b = B * (ln - l) + (1 - B) * b
        l = ln
    i = int(sse.argmin())
    return float(sse[i]), (float(A[i]), float(B[i]), float(C[i]))


def cross_check_statsmodels(y, pa, ph, pw):
    """Independent confirmation of the recursions against statsmodels (known initial states, fixed parameters)."""
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    warnings.filterwarnings("ignore")
    l0, b0, s0 = init(y)
    ys = y[7:TR]
    m1 = ExponentialSmoothing(ys, initialization_method="known", initial_level=l0).fit(smoothing_level=pa[0], optimized=False)
    m2 = ExponentialSmoothing(ys, trend="add", initialization_method="known", initial_level=l0, initial_trend=b0).fit(
        smoothing_level=ph[0], smoothing_trend=ph[1], optimized=False)
    m3 = ExponentialSmoothing(ys, trend="add", seasonal="add", seasonal_periods=7, initialization_method="known",
                              initial_level=l0, initial_trend=b0, initial_seasonal=s0).fit(
        smoothing_level=pw[0], smoothing_trend=pw[1], smoothing_seasonal=pw[2], optimized=False)
    return m1.sse, m2.sse, m3.sse


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    y = df["orders"].to_numpy(float)
    a_grid = grid_ses(y)
    h_grid = grid_holt(y)
    w_grid = grid_hw(y)
    (sse_s, (a_s,)), (sse_h, (a_h, b_h)), (sse_w, (a_w, b_w, g_w)) = a_grid, h_grid, w_grid

    ses_l, ses_f = run_ses(y, a_s)
    holt_l, holt_t, holt_f = run_holt(y, a_h, b_h)
    hw_l, hw_t, hw_s, hw_f = run_hw(y, a_w, b_w, g_w)
    sn_f = np.full(N, np.nan)
    sn_f[7:TR] = y[:TR - 7]
    sn_f[TR:] = [y[TR + h - 1 - 7 * math.ceil(h / 7)] for h in range(1, H + 1)]
    sm = cross_check_statsmodels(y, (a_s,), (a_h, b_h), (a_w, b_w, g_w))
    for mine, ref in zip((sse_of(y, ses_f), sse_of(y, holt_f), sse_of(y, hw_f)), sm):
        assert abs(mine - ref) < 1e-6 * ref, (mine, ref)
    for mine, ref in zip((sse_of(y, ses_f), sse_of(y, holt_f), sse_of(y, hw_f)), (sse_s, sse_h, sse_w)):
        assert abs(mine - ref) < 1e-6 * ref, (mine, ref)

    a_all = y[TR:]
    def hold(fc):
        e = a_all - fc[TR:]
        return dict(rmse=float(np.sqrt(np.mean(e ** 2))), mae=float(np.mean(np.abs(e))), bias=float(np.mean(e)))
    HOLD = {"Seasonal naive": hold(sn_f), "SES": hold(ses_f), "Holt": hold(holt_f), "Holt-Winters": hold(hw_f)}
    FC = {"Seasonal naive": sn_f, "SES": ses_f, "Holt": holt_f, "Holt-Winters": hw_f}
    sse_sn = sse_of(y, sn_f)
    n_fit = TR - 7

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 23 - Exponential smoothing models",
             f"Recursions run row by row on Data (rows {R7}-{LAST} = training one-step forecasts, rows {LAST + 1}-{N + 1} = holdout "
             "multi-step forecasts). Yellow cells hold the smoothing parameters.")
    b.add_column("t", lambda r: "=ROW()-1", np.arange(1, N + 1), "0")
    b.add_column("h", lambda r: f"=Data!{b.col('t')}{r}-{TR}", np.r_[np.full(TR, np.nan), np.arange(1, H + 1)], "0", first_row=LAST + 1)

    b.section("1. Smoothing parameters (yellow = edit me; defaults = grid-search optimum from Python, step 0.01)")
    pa = b.row("SES alpha", float(a_s), None, "0.00", "level weight", is_input=True)
    ph_a = b.row("Holt alpha", float(a_h), None, "0.00", "level weight", is_input=True)
    ph_b = b.row("Holt beta", float(b_h), None, "0.00", "trend weight", is_input=True)
    pw_a = b.row("Holt-Winters alpha", float(a_w), None, "0.00", "level weight", is_input=True)
    pw_b = b.row("Holt-Winters beta", float(b_w), None, "0.00", "trend weight", is_input=True)
    pw_g = b.row("Holt-Winters gamma", float(g_w), None, "0.00", "seasonal weight", is_input=True)

    Yr = lambda r0, r1: f"Data!$B${r0}:$B${r1}"
    b.section("2. Initial states from the first two weeks (t = 7)")
    l0, b0, s0 = init(y)
    L0 = b.row("Initial level l7 = mean of week 1", f"=AVERAGE({Yr(2, 8)})", l0, "0.00")
    B0 = b.row("Initial trend b7 = (mean week 2 - mean week 1) / 7", f"=(AVERAGE({Yr(9, 15)})-AVERAGE({Yr(2, 8)}))/7", b0, "0.000",
               "orders per day; noisy because it comes from two weekly means")

    # state columns -------------------------------------------------------------------
    def col(nm):
        return b.col(nm)
    ex = lambda arr, lo: np.where(np.arange(N) >= lo, arr, np.nan)  # blank before index lo

    # SES
    def ses_level(r):
        return f"={L0}" if r == R7 else f"={pa}*Data!B{r}+(1-{pa})*Data!{col('ses_level')}{r - 1}"
    b.add_column("ses_level", ses_level, ex(np.where(np.arange(N) < TR, ses_l, np.nan), 6), "0.00", first_row=R7)
    b.add_column("ses_forecast", lambda r: f"=Data!{col('ses_level')}{r - 1}" if r <= LAST else f"=Data!{col('ses_level')}${LAST}",
                 ses_f, "0.00", first_row=R7 + 1)
    # Holt
    def holt_level(r):
        return f"={L0}" if r == R7 else f"={ph_a}*Data!B{r}+(1-{ph_a})*(Data!{col('holt_level')}{r - 1}+Data!{col('holt_trend')}{r - 1})"
    def holt_trend(r):
        return f"={B0}" if r == R7 else f"={ph_b}*(Data!{col('holt_level')}{r}-Data!{col('holt_level')}{r - 1})+(1-{ph_b})*Data!{col('holt_trend')}{r - 1}"
    # the trend column is referenced by the level column, so reserve its letter first
    from openpyxl.utils import get_column_letter
    base_j = b.data.max_column
    b._cols["holt_level"] = get_column_letter(base_j + 1)
    b._cols["holt_trend"] = get_column_letter(base_j + 2)
    b.add_column("holt_level", holt_level, ex(np.where(np.arange(N) < TR, holt_l, np.nan), 6), "0.00", first_row=R7)
    b.add_column("holt_trend", holt_trend, ex(np.where(np.arange(N) < TR, holt_t, np.nan), 6), "0.000", first_row=R7)
    assert b.col("holt_level") == get_column_letter(base_j + 1) and b.col("holt_trend") == get_column_letter(base_j + 2)
    b.add_column("holt_forecast",
                 lambda r: (f"=Data!{col('holt_level')}{r - 1}+Data!{col('holt_trend')}{r - 1}" if r <= LAST else
                            f"=Data!{col('holt_level')}${LAST}+Data!{col('h')}{r}*Data!{col('holt_trend')}${LAST}"),
                 holt_f, "0.00", first_row=R7 + 1)
    # Holt-Winters (additive)
    base_j = b.data.max_column
    for k, nm in enumerate(["hw_level", "hw_trend", "hw_season"], start=1):
        b._cols[nm] = get_column_letter(base_j + k)
    def hw_level(r):
        return f"={L0}" if r == R7 else (f"={pw_a}*(Data!B{r}-Data!{col('hw_season')}{r - 7})+(1-{pw_a})*"
                                         f"(Data!{col('hw_level')}{r - 1}+Data!{col('hw_trend')}{r - 1})")
    def hw_trend(r):
        return f"={B0}" if r == R7 else f"={pw_b}*(Data!{col('hw_level')}{r}-Data!{col('hw_level')}{r - 1})+(1-{pw_b})*Data!{col('hw_trend')}{r - 1}"
    def hw_season(r):
        if r <= R7:
            return f"=Data!B{r}-{L0}"
        return (f"={pw_g}*(Data!B{r}-Data!{col('hw_level')}{r - 1}-Data!{col('hw_trend')}{r - 1})+"
                f"(1-{pw_g})*Data!{col('hw_season')}{r - 7}")
    tr_mask = np.arange(N) < TR
    b.add_column("hw_level", hw_level, ex(np.where(tr_mask, hw_l, np.nan), 6), "0.00", first_row=R7)
    b.add_column("hw_trend", hw_trend, ex(np.where(tr_mask, hw_t, np.nan), 6), "0.000", first_row=R7)
    b.add_column("hw_season", hw_season, np.where(tr_mask, hw_s, np.nan), "0.00", first_row=2)
    b.add_column("hw_forecast",
                 lambda r: (f"=Data!{col('hw_level')}{r - 1}+Data!{col('hw_trend')}{r - 1}+Data!{col('hw_season')}{r - 7}" if r <= LAST else
                            f"=Data!{col('hw_level')}${LAST}+Data!{col('h')}{r}*Data!{col('hw_trend')}${LAST}"
                            f"+INDEX(Data!{col('hw_season')}${LAST - 6}:{col('hw_season')}${LAST},MOD(Data!{col('h')}{r}-1,7)+1)"),
                 hw_f, "0.00", first_row=R7 + 1)
    b.add_column("seasonal_naive",
                 lambda r: (f"=Data!B{r - 7}" if r <= LAST else f"=Data!B{r - 7 * math.ceil((r - LAST) / 7)}"),
                 sn_f, "0", first_row=R7 + 1)

    # SES sensitivity columns (own alpha each, SES level only) ---------------------------------
    alphas = [0.05, 0.10, 0.20, 0.40, 0.80]
    b.section("3. SES sensitivity: same data, five different alphas (level columns on Data, columns at the far right)")
    rows = []
    sens_cols = []
    for k, al in enumerate(alphas):
        rows.append([al, None, None, None])
    t0, t1 = b.table(["alpha", "SSE (rows 9-141)", "RMSE", "memory 1/alpha (days)"], rows, fmt={0: "0.00", 1: "0", 2: "0.00", 3: "0.0"})
    for c in range(1, 6):
        b.an.cell(row=t0 + c - 1, column=1).fill = INPUT_FILL
    sens_sse = []
    for k, al in enumerate(alphas):
        nm = f"ses_level_a{k + 1}"
        arow = t0 + k
        lev_k, fc_k = run_ses(y, al)
        sens_sse.append(sse_of(y, fc_k))
        b.add_column(nm, lambda r, arow=arow, nm=nm: (f"={L0}" if r == R7 else
                                                      f"=Analysis!$A${arow}*Data!B{r}+(1-Analysis!$A${arow})*Data!{col(nm)}{r - 1}"),
                     np.where(tr_mask, lev_k, np.nan) * np.where(np.arange(N) >= 6, 1, np.nan), "0.00", first_row=R7)
        L = col(nm)
        b.an.cell(row=arow, column=2, value=f"=SUMXMY2(Data!$B$9:$B${LAST},Data!${L}$8:${L}${LAST - 1})").number_format = "0"
        b.an.cell(row=arow, column=3, value=f"=SQRT(B{arow}/{n_fit})").number_format = "0.00"
        b.an.cell(row=arow, column=4, value=f"=1/A{arow}").number_format = "0.0"
        b.checks += [(f"Analysis!B{arow}", f"SES SSE alpha={al}", sens_sse[-1]),
                     (f"Analysis!C{arow}", f"SES RMSE alpha={al}", math.sqrt(sens_sse[-1] / n_fit)),
                     (f"Analysis!D{arow}", f"memory alpha={al}", 1 / al)]
    best_i = int(np.argmin(sens_sse))

    # -------------------------------------------------------------- comparison
    fcol = {"Seasonal naive": "seasonal_naive", "SES": "ses_forecast", "Holt": "holt_forecast", "Holt-Winters": "hw_forecast"}
    b.section("4. Training fit (one-step-ahead, rows 9-141) and holdout accuracy (28 days, multi-step)")
    A_h = f"Data!$B${LAST + 1}:$B${N + 1}"
    rows, exp = [], {}
    for i, name in enumerate(fcol):
        c = col(fcol[name])
        F_tr = f"Data!${c}$9:${c}${LAST}"
        F_h = f"Data!${c}${LAST + 1}:${c}${N + 1}"
        rows.append([name, f"=SUMXMY2({Yr(9, LAST)},{F_tr})", f"=SQRT(B{b.next_row + 1 + i}/{n_fit})",
                     f"=SQRT(SUMXMY2({A_h},{F_h})/COUNT({A_h}))", f"=SUMPRODUCT(ABS({A_h}-{F_h}))/COUNT({A_h})",
                     f"=SUMPRODUCT({A_h}-{F_h})/COUNT({A_h})"])
        sse_i = sse_sn if name == "Seasonal naive" else {"SES": sse_s, "Holt": sse_h, "Holt-Winters": sse_w}[name]
        exp.update({(i, 1): sse_i, (i, 2): math.sqrt(sse_i / n_fit), (i, 3): HOLD[name]["rmse"], (i, 4): HOLD[name]["mae"],
                    (i, 5): HOLD[name]["bias"]})
    c0, c1 = b.table(["Model", "Training SSE", "Training RMSE", "Holdout RMSE", "Holdout MAE", "Holdout bias"], rows,
                     fmt={1: "0", 2: "0.00", 3: "0.00", 4: "0.00", 5: "0.00"}, expect=exp)
    comp0 = c0
    b.row("Holdout RMSE of the best model / seasonal naive", f"=MIN(D{c0}:D{c1})/D{c0}",
          min(v["rmse"] for v in HOLD.values()) / HOLD["Seasonal naive"]["rmse"], "0.00")

    b.section("5. Grid search from Python (step 0.01, minimises training SSE; static numbers, not formulas)")
    rows = [["SES", a_s, None, None, sse_s], ["Holt", a_h, b_h, None, sse_h], ["Holt-Winters", a_w, b_w, g_w, sse_w]]
    g0, g1 = b.table(["Model", "alpha", "beta", "gamma", "SSE at optimum"], rows, fmt={1: "0.00", 2: "0.00", 3: "0.00", 4: "0"})
    b.row("Live SSE of HW minus grid SSE (0 while the yellow cells hold the optimum)",
          f"=B{c0 + 3}-E{g0 + 2}", 0.0, "0.000")

    b.section("6. Final states after the training rows (what the forecast is built from)")
    fl = b.row("Final HW level l140", f"=Data!{col('hw_level')}{LAST}", hw_l[TR - 1], "0.00")
    ft = b.row("Final HW trend b140 (orders/day)", f"=Data!{col('hw_trend')}{LAST}", hw_t[TR - 1], "0.000")
    b.row("Final SES level", f"=Data!{col('ses_level')}{LAST}", ses_l[TR - 1], "0.00")
    rows = []
    exp = {}
    for k in range(7):
        rows.append([DAYNAMES[k], f"=Data!{col('hw_season')}{LAST - 6 + k}", f"=Data!{col('hw_season')}{2 + k}"])
        exp[(k, 1)], exp[(k, 2)] = hw_s[TR - 7 + k], hw_s[k]
    s0r, s1r = b.table(["Weekday (last 7 training days)", "HW seasonal index at day 140", "initial index (week 1 minus mean)"], rows,
                       fmt={1: "0.0", 2: "0.0"}, expect=exp)
    b.bar_chart_from_table("Seasonal index by weekday: final vs initial", 1, [2, 3], s0r, s1r, anchor="J26", y_title="orders vs level")

    b.section("7. Weight of past observations in SES (alpha from section 1)")
    rows, exp = [], {}
    for k in range(14):
        rows.append([k, f"={pa.replace('Analysis!', '')}*(1-{pa.replace('Analysis!', '')})^A{b.next_row + 1 + k}"])
        exp[(k, 1)] = a_s * (1 - a_s) ** k
    wt0, wt1 = b.table(["k = days ago", "weight alpha*(1-alpha)^k"], rows, fmt={1: "0.0000"}, expect=exp)
    b.row("Weight on the 14 most recent days (sum)", f"=SUM(B{wt0}:B{wt1})", float(sum(a_s * (1 - a_s) ** k for k in range(14))), "0.0%")
    b.row("Days until a level jump is 90% absorbed: ln(0.1)/ln(1-alpha)", f"=LN(0.1)/LN(1-{pa.replace('Analysis!', '')})",
          math.log(0.1) / math.log(1 - a_s), "0.0")

    b.line_chart("Orders and one-step / holdout forecasts", "date", ["orders", "ses_forecast", "holt_forecast", "hw_forecast"],
                 anchor="J4", y_title="orders per day")

    sse_rank = sorted([("SES", sse_s), ("Holt", sse_h), ("Holt-Winters", sse_w)], key=lambda x: x[1])
    hold_rank = sorted(HOLD, key=lambda k: HOLD[k]["rmse"])
    wk_idx = int(np.argmin(sens_sse))
    last_season = hw_s[TR - 7:TR]
    b.answers([
        ("Initial level and trend from the first two weeks", f"={L0}",
         f"l7 = {l0:.1f} orders (mean of week 1), b7 = {b0:.3f} orders/day. Both rest on only 14 observations; an unlucky first "
         "fortnight biases every later forecast until the recursion has forgotten it."),
        (f"SES with alpha = {a_s:.2f}: training SSE and RMSE (rows 9-141) and the flat 28-day forecast", f"=Analysis!B{comp0 + 1}",
         f"SSE = {sse_s:,.0f}, RMSE = {math.sqrt(sse_s / n_fit):.1f}; the forecast is the final level {ses_l[TR - 1]:.1f} for every holdout day, "
         "so it ignores the weekly pattern entirely."),
        ("SES sensitivity: which of alpha = 0.05, 0.10, 0.20, 0.40, 0.80 gives the lowest SSE?", f"=Analysis!B{t0 + best_i}",
         f"alpha = {alphas[best_i]:.2f} (SSE {sens_sse[best_i]:,.0f}); alpha = 0.80 gives {sens_sse[4]:,.0f}. A large alpha chases the weekday "
         "ripple (memory 1.25 days), a tiny one is slow after the level shift; the optimum is a compromise."),
        (f"Holt with alpha = {a_h:.2f}, beta = {b_h:.2f}: SSE and the day-28 forecast", f"=Analysis!B{comp0 + 2}",
         f"SSE = {sse_h:,.0f} vs SES {sse_s:,.0f} ({(sse_s - sse_h) / sse_s:.1%} lower). Adding a trend barely matters while the weekly "
         f"pattern is unmodelled; the day-28 forecast is {holt_f[N - 1]:.1f}."),
        (f"Holt-Winters additive (alpha = {a_w:.2f}, beta = {b_w:.2f}, gamma = {g_w:.2f}): SSE and seasonal indices for Mon..Sun", f"=Analysis!B{comp0 + 3}",
         f"SSE = {sse_w:,.0f} ({(sse_s - sse_w) / sse_s:.0%} below SES). Indices Mon..Sun: " + ", ".join(f"{v:+.1f}" for v in last_season) +
         " orders vs the level: weekdays high, weekend low."),
        ("Rank the models by training SSE; compute the naive benchmark's SSE", f"=Analysis!B{comp0}",
         "Training SSE order: " + " < ".join(f"{n} ({v:,.0f})" for n, v in sse_rank) + f". Seasonal naive SSE = {sse_sn:,.0f}: "
         "a model with a seasonal component should beat it, otherwise the smoothing is not earning its parameters."),
        ("Holdout RMSE, MAE and bias for all four models; does the ranking match the training ranking?", f"=Analysis!D{comp0 + 3}",
         "Holdout RMSE order: " + " < ".join(f"{n} ({HOLD[n]['rmse']:.1f})" for n in hold_rank) +
         ". Holdout bias (actual - forecast): " + ", ".join(f"{n} {HOLD[n]['bias']:+.1f}" for n in HOLD) + "."),
        (f"Memory and weights of SES with alpha = {a_s:.2f}", f"=Analysis!B{wt0}",
         f"Weight on yesterday {a_s:.2f}, on 7 days ago {a_s * (1 - a_s) ** 7:.3f}; 90% of a level jump is absorbed after "
         f"{math.log(0.1) / math.log(1 - a_s):.1f} days. The effective memory is about 1/alpha = {1 / a_s:.1f} days."),
        ("Name two limitations of choosing parameters by minimising training SSE and extrapolating the state", "see text",
         "(1) The parameters are tuned on the very rows they are scored on, so the training SSE is optimistic; judge on the holdout. "
         "(2) Holt-Winters extrapolates the last trend and a seasonal pattern that never changes; the additive form also breaks "
         "if the weekday swing grows with the level, and the initial states come from only two weeks."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-23-exponential-smoothing", "23 · Exponential smoothing models",
             "SES, Holt and additive Holt-Winters as recursions with fixed, grid-searched parameters, against seasonal naive.",
             df.rename(columns={"date": "time"}), "time")
    d.stat("Training RMSE, one-step ahead (orders/day)", {k: math.sqrt(v / n_fit) for k, v in
                                                          {"Seasonal naive": sse_sn, "SES": sse_s, "Holt": sse_h, "Holt-Winters": sse_w}.items()},
           "Days 8-140. Holt-Winters removes about two thirds of the SES squared error, because it models the weekly pattern.", decimals=1)
    ts = pd.DataFrame({"time": df["date"], "orders": y, "SES": ses_f, "Holt": holt_f, "Holt-Winters": hw_f})
    d.timeseries("Orders and forecasts (one-step in training, multi-step from 2025-07-21)", ts,
                 "SES and Holt are smooth lines through the weekly saw-tooth; Holt-Winters follows it. The level steps up in late May.",
                 colors={"orders": "#9AA5B1", "SES": "#4E79A7", "Holt": "#F28E2B", "Holt-Winters": "#E15759"}, w=24, h=9)
    hd = pd.DataFrame({"day": np.arange(1, H + 1), "actual": a_all, "SES": ses_f[TR:], "Holt": holt_f[TR:],
                       "Holt-Winters": hw_f[TR:], "seasonal naive": sn_f[TR:]})
    d.xy("Holdout days 1-28: actual vs forecasts", hd, "day", ["actual", "SES", "Holt", "Holt-Winters", "seasonal naive"],
         "Only the seasonal models reproduce the weekly ripple. SES and Holt are blind to it.",
         lines=["SES", "Holt", "Holt-Winters", "seasonal naive"])
    d.bars("Holdout RMSE (orders/day)", pd.DataFrame({"model": list(HOLD), "RMSE": [HOLD[k]["rmse"] for k in HOLD],
                                                      "MAE": [HOLD[k]["mae"] for k in HOLD]}),
           "28-day multi-step forecast error. Same ranking as the training SSE?", w=12)
    d.bars("SES: SSE for five values of alpha", pd.DataFrame({"alpha": [f"alpha {al:.2f}" for al in alphas], "SSE": sens_sse}),
           "A U-shape: too small reacts slowly to the level shift, too large chases the weekday noise.", w=12, h=8)
    seas = pd.DataFrame({"weekday": DAYNAMES, "final index": last_season, "initial index": s0})
    d.bars("Holt-Winters seasonal indices by weekday", seas,
           "Orders above/below the level. The initial indices come from week 1; the final ones are smoothed over 20 weeks.", w=12, h=8)
    d.save(out)

    ctx = dict(a_s=f"{a_s:.2f}", a_h=f"{a_h:.2f}", b_h=f"{b_h:.2f}", a_w=f"{a_w:.2f}", b_w=f"{b_w:.2f}", g_w=f"{g_w:.2f}")
    md(out / "theory.md", THEORY)
    md(out / "task.md", fill(TASK, **ctx))
    return b


def fill(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace(f"@@{k}@@", str(v))
    assert "@@" not in text
    return text


THEORY = r"""
# Theory: exponential smoothing models

## Why smoothing instead of a fixed regression

A regression on time ([lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md)) gives every observation the same
weight and assumes the level, slope and seasonal pattern never change. A **moving average** forgets abruptly. **Exponential
smoothing** keeps a small *state* (level, trend, seasonal indices) that is updated by one line per new observation, so recent
data counts more than old data and the forecast adapts when the business changes. The price is that you must choose how fast to
adapt: the smoothing parameters. This lesson builds the three standard models by hand as row-by-row recursions.

## Simple exponential smoothing (SES)

State: the level $\ell_t$. Forecast and update, with $0<\alpha<1$:

$$
\hat y_{t+1\mid t} = \ell_t, \qquad \ell_t = \alpha\, y_t + (1-\alpha)\,\ell_{t-1}.
$$

Unrolling the recursion shows $\ell_t = \sum_{k\ge 0} \alpha(1-\alpha)^k\, y_{t-k}$ plus a fading contribution of the start value:
weights **decay geometrically** and sum to 1. The weight on the observation $k$ days back is $\alpha(1-\alpha)^k$; the effective
memory is about $1/\alpha$ observations. A step in the level is $90\%$ absorbed after $\ln 0.1/\ln(1-\alpha)$ periods
(6.5 days for $\alpha=0.3$). SES forecasts a **flat line** for every horizon: it cannot represent trend or seasonality.

## Holt's linear trend

Add a slope state $b_t$ with weight $\beta$:

$$
\ell_t = \alpha y_t + (1-\alpha)(\ell_{t-1}+b_{t-1}),\qquad
b_t = \beta(\ell_t-\ell_{t-1}) + (1-\beta)\,b_{t-1},\qquad
\hat y_{t+h\mid t} = \ell_t + h\,b_t .
$$

## Holt-Winters, additive seasonality (period $m=7$)

$$
\hat y_{t+1\mid t} = \ell_t + b_t + s_{t+1-m},\qquad
\ell_t = \alpha(y_t - s_{t-m}) + (1-\alpha)(\ell_{t-1}+b_{t-1}),
$$
$$
b_t = \beta(\ell_t-\ell_{t-1}) + (1-\beta)b_{t-1},\qquad
s_t = \gamma\,(y_t-\ell_{t-1}-b_{t-1}) + (1-\gamma)\,s_{t-m}.
$$

For a horizon of $h$ days the seasonal index is the last estimate for that weekday:
$\hat y_{t+h\mid t} = \ell_t + h\,b_t + s_{t+h-m\lceil h/m\rceil}$. Use the *multiplicative* form
($s$ multiplies instead of adds) when the weekly swing grows with the level.

## Initial values and parameters

The recursion needs starting states. A simple, transparent choice, used here, takes them from the first two weeks:
$\ell_7=\bar y_{1..7}$, $b_7=(\bar y_{8..14}-\bar y_{1..7})/7$ and $s_i=y_i-\ell_7$ for $i=1..7$. Parameters are normally
chosen to minimise the one-step **sum of squared errors** $\text{SSE}=\sum_t (y_t-\hat y_{t\mid t-1})^2$. This course keeps them fixed
in yellow cells so you can see their effect; a grid search over 0.01 steps (done in Python, the optimum is printed in the
workbook) finds the same optimum a solver would.

**Worked example (SES, $\alpha=0.4$, start $\ell_0=100$)** for $y=(110,104,98,120)$:
$\ell_1 = 0.4\cdot110+0.6\cdot100=104.0$; the forecast for $t=2$ is $104.0$ and its error is $104-104.0=0.0$.
$\ell_2=0.4\cdot104+0.6\cdot104.0=104.0$; forecast for $t=3$ is $104.0$ (error $-6.0$). $\ell_3 = 0.4\cdot98+0.6\cdot104=101.6$;
forecast for $t=4$ is $101.6$ (error $+18.4$). The level moves only 40% of the way towards each surprise, so a single odd day
does not rewrite the forecast.

## What the parameters mean in practice

- **Large $\alpha$**: the level follows the data closely (short memory); good after structural changes, but weekday noise leaks into
  the level. **Small $\alpha$**: stable, slow to react. With a weekly pattern *outside* the model the SSE-optimal $\alpha$ is small
  because averaging the ripple is more valuable than speed.
- **$\beta$ near 0**: the slope is nearly constant after initialisation, so it inherits the noise of the initial estimate.
- **$\gamma$ near 0**: the seasonal pattern is frozen at its initial shape; large values let the pattern drift with the data.

## Pitfalls

1. **Optimising and judging on the same rows.** The training SSE always favours the richest model; use a holdout ([lesson 24](../24-backtesting-and-forecast-accuracy/theory.md)).
2. **Flat or straight-line forecasts at long horizons.** SES ignores a trend, Holt extrapolates it forever (damped trend variants shrink it).
3. **Noisy initial states** from a short start-up window, particularly the trend.
4. **Wrong seasonality form** (additive vs multiplicative) or a changing period (holidays, month-end).
5. **A one-step SSE is not a multi-step error.** The 28-day holdout uses states frozen at the end of training and is much harder.
6. **Parameters at the boundary** (0 or 1) usually signal a mis-specified model, not a precise one.

## Related notes

- [Moving averages and exponential smoothing](../08-moving-averages-and-exponential-smoothing/theory.md)
- [Trend, seasonality and noise](../07-trend-seasonality-and-noise/theory.md)
- [Naive and seasonal naive forecasts](../21-naive-and-seasonal-naive-forecasts/theory.md)
- [Backtesting and forecast accuracy](../24-backtesting-and-forecast-accuracy/theory.md)
- Repo notes: [forecasting](../../notes/time_series/forecasting.md), [seasonality and trends](../../notes/time_series/seasonality_and_trends.md)
"""

TASK = r"""
# Task: exponential smoothing models

## Scenario

Hearthside (the online candle shop from lesson 22) wants a forecast that **updates itself** each morning instead of a
regression refitted by hand. In late spring a marketing campaign started and the team is unsure how quickly the forecast should
react to it. You will build simple exponential smoothing (SES), Holt's linear trend and additive Holt-Winters in a spreadsheet,
compare them, and decide which smoothing speed the business should use.

## Data

`data.csv` - 168 consecutive days starting Monday 2025-03-03, one row per day.

| column | meaning |
|---|---|
| `date` | calendar day |
| `orders` | orders placed that day |

The first **140 days are the training period** (states are updated on them); the last **28 days are the holdout** (multi-step
forecast from the final training state; no updating). Use these parameters, found by a grid search on the training SSE:
SES alpha = @@a_s@@; Holt alpha = @@a_h@@, beta = @@b_h@@; Holt-Winters alpha = @@a_w@@, beta = @@b_w@@, gamma = @@g_w@@. Put them in
input cells and make every recursion refer to them.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the initial level (mean of week 1) and initial trend ((mean of week 2 - mean of week 1) / 7).
2. Build SES from day 8 on (forecast for day t = level after day t-1). Report the training SSE and RMSE over days 8-140 and the 28-day forecast.
3. Repeat SES with alpha = 0.05, 0.10, 0.20, 0.40 and 0.80. Which alpha minimises the SSE? Explain why neither extreme wins.
4. Build Holt's model. Report its SSE and the forecast for day 168 (h = 28). How much does the trend term improve on SES?
5. Build additive Holt-Winters with period 7 (initial indices = week-1 values minus week-1 mean). Report its SSE and the seven
   seasonal indices after day 140.
6. Compute the SSE of the seasonal naive forecast (y[t-7]) for the same days and rank all four models by training SSE.
7. Forecast the 28 holdout days with each model (flat level; level + h*trend; level + h*trend + seasonal index) and report RMSE,
   MAE and bias. Does the holdout ranking agree with the training ranking?
8. For your SES alpha, compute the weights alpha*(1-alpha)^k for k = 0..13, their sum, and the number of days needed to absorb 90% of a level jump.
9. *Explain in 3-4 sentences* why minimising training SSE does not guarantee the best forecast, and which of the three
   parameters you trust least.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Orders and forecasts", what happens to the level around late May, and how long does each model take to catch up?
- In "Holdout days 1-28", which models reproduce the weekly zig-zag and which draw a smooth line?
- In "SES: SSE for five values of alpha", read off the shape. Where would you put alpha and why?

## Deliverable

A short note (6-8 lines): *which model would you run in production, with which parameters, and what would make you retune
them?* Include the SSE / holdout RMSE comparison table and one chart of the holdout forecasts. State the biggest weakness
of your chosen model.
"""
