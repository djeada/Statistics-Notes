"""Lesson 28 - Time-series anomaly detection (seasonal baseline + robust residual score)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "28-time-series-anomaly-detection"
TITLE = "Time-series anomaly detection"
MODULE = "Statistical monitoring and decision-making"
DATASET = "154 daily mean compressor-housing temperatures (C), strong weekday cycle, injected spikes and a level shift"
T_DEF = 3.5       # decision threshold on the robust z-score
WARM = 42         # days before the first score (28 for the baseline + 14 residuals for the scale)
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
THRS = [2.5, 3.0, 3.5, 4.0, 5.0, 6.0]
K_MAD = 1.4826


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(2808)
    n = 154
    d = pd.date_range("2026-01-05", periods=n, freq="D")  # 2026-01-05 is a Monday
    wd = d.day_of_week.to_numpy()
    prof = np.array([0.5, 1.2, 1.0, 0.8, 0.3, -7.5, -10.5])  # plant runs Mon-Fri, idles at the weekend
    x = 52.0 + prof[wd] + 1.0 * rng.standard_normal(n)
    ev = np.array(["none"] * n, dtype=object)
    for i, dl in {19: 7.5, 47: 6.5, 63: -9.0, 79: 8.0, 92: 5.5, 101: 7.0}.items():
        x[i] += dl
        ev[i] = "spike"
    x[112:] += 6.0  # cooling-loop fouling: sustained +6 C from day 113
    ev[112:] = "shift"
    return pd.DataFrame({"date": d, "weekday": [DAYS[i] for i in wd], "temp_c": x.round(1), "event": ev})


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    x = df["temp_c"].to_numpy()
    n = len(x)
    wd = df["weekday"].to_numpy()
    ev = df["event"].to_numpy()
    weekend = np.isin(wd, ["Sat", "Sun"])

    base = np.full(n, np.nan)
    for i in range(28, n):
        base[i] = np.median([x[i - 7], x[i - 14], x[i - 21], x[i - 28]])
    resid = x - base
    absr = np.abs(resid)
    scale = np.full(n, np.nan)
    for i in range(WARM, n):
        a = max(28, i - 28)
        scale[i] = K_MAD * np.median(absr[a:i])
    z = resid / scale
    absz = np.abs(z)
    flag = np.where(np.isnan(z), np.nan, (absz > T_DEF).astype(float))
    med0 = float(np.median(x[:WARM]))
    sc0 = K_MAD * float(np.median(np.abs(x[:WARM] - med0)))
    absdev0 = np.abs(x - med0)
    zn = (x - med0) / sc0
    flagn = (np.abs(zn) > T_DEF).astype(float)
    shift_idx = np.where(ev == "shift")[0]
    shiftday = np.where((flag == 1) & (ev == "shift"), np.arange(n) + 1, 0).astype(float)
    shiftday[np.isnan(flag)] = 0
    prof_mean = {w: float(np.mean(x[:WARM][wd[:WARM] == w])) for w in DAYS}

    scored = ~np.isnan(z)
    sp = ev == "spike"
    caught = int(((flag == 1) & sp).sum())
    spikes_scored = int((sp & scored).sum())
    fa_normal = int(((flag == 1) & (ev == "none")).sum())
    shift_flagged = int(((flag == 1) & (ev == "shift")).sum())
    last_shift_flag = int(shiftday.max())
    first_shift_day = int(shift_idx[0]) + 1

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 28 - Time-series anomaly detection",
             "Solved workbook. Yellow cell = decision threshold on |z|. Everything else is a live formula.")
    T = b.row("Threshold T on |robust z|", T_DEF, None, "0.0", "Edit me", True)
    b.add_column("baseline", lambda r: f"=MEDIAN(C{r - 7},C{r - 14},C{r - 21},C{r - 28})", expected=base, fmt="0.00")
    b.add_column("residual", lambda r: f"=C{r}-E{r}", expected=resid, fmt="0.00")
    b.add_column("abs_resid", lambda r: f"=ABS(F{r})", expected=absr, fmt="0.00")
    b.add_column("scale", lambda r: f"={K_MAD}*MEDIAN(G{max(30, r - 28)}:G{r - 1})", expected=scale, fmt="0.000")
    b.add_column("z", lambda r: f"=F{r}/H{r}", expected=z, fmt="0.00")
    b.add_column("abs_z", lambda r: f"=ABS(I{r})", expected=absz, fmt="0.00")
    b.add_column("flag", lambda r: f"=IF(J{r}>{T},1,0)", expected=flag, fmt="0")
    assert [b.col(c) for c in ("baseline", "residual", "abs_resid", "scale", "z", "abs_z", "flag")] == list("EFGHIJK")
    # naive weekday-blind detector (reference = first 6 weeks)

    b.section("1. Weekday cycle in the first 6 weeks (days 1-42)")
    rows, exp = [], {}
    for i, w in enumerate(DAYS):
        rows.append([w, f'=COUNTIF(Data!$B$2:$B${WARM + 1},A{b.next_row + 1 + i})',
                     f'=AVERAGEIFS(Data!$C$2:$C${WARM + 1},Data!$B$2:$B${WARM + 1},A{b.next_row + 1 + i})'])
        exp.update({(i, 1): 6, (i, 2): prof_mean[w]})
    p0, p1 = b.table(["Weekday", "n", "Mean temp (C)"], rows, fmt={2: "0.00"}, expect=exp)
    b.bar_chart_from_table("Mean temperature by weekday (first 6 weeks)", 1, [3], p0, p1, anchor="H4", y_title="C")
    rng_ = f"Analysis!$C${p0}:$C${p1}"
    rngr = b.row("Highest minus lowest weekday mean (C)", f"=MAX({rng_})-MIN({rng_})",
                 max(prof_mean.values()) - min(prof_mean.values()), "0.00")

    b.section("2. Naive detector: one global robust z, calibrated on days 1-42, blind to weekday")
    med0r = b.row("Median of days 1-42 (C)", f"=MEDIAN(Data!$C$2:$C${WARM + 1})", med0, "0.00")
    b.add_column("absdev0", lambda r: f"=ABS(C{r}-{med0r})", expected=absdev0, fmt="0.00")
    sc0r = b.row("Robust sigma = 1.4826 x MAD (C)", f"={K_MAD}*MEDIAN(Data!$L$2:$L${WARM + 1})", sc0, "0.000")
    b.add_column("z_naive", lambda r: f"=(C{r}-{med0r})/{sc0r}", expected=zn, fmt="0.00")
    b.add_column("flag_naive", lambda r: f"=IF(ABS(M{r})>{T},1,0)", expected=flagn, fmt="0")
    assert [b.col(c) for c in ("absdev0", "z_naive", "flag_naive")] == list("LMN")
    nf = b.row("Days flagged by the naive detector", f"=SUM({b.rng('flag_naive')})", flagn.sum(), "0")
    nfw = b.row("... of which Saturdays or Sundays",
                f'=COUNTIFS({b.rng("flag_naive")},1,{b.rng("weekday")},"Sat")+COUNTIFS({b.rng("flag_naive")},1,{b.rng("weekday")},"Sun")',
                (flagn[weekend]).sum(), "0")
    b.row("Weekend days in the whole series", f'=COUNTIF({b.rng("weekday")},"Sat")+COUNTIF({b.rng("weekday")},"Sun")', weekend.sum(), "0")

    b.section("3. Seasonal baseline + rolling robust residual score (starts on day 43)")
    b.add_column("shift_flag_day", lambda r: f'=IF(AND(K{r}=1,D{r}="shift"),ROW()-1,0)', expected=shiftday, fmt="0")
    assert b.col("shift_flag_day") == "O"
    sc_last = b.row("Robust scale on the last day (C)", f"=INDEX({b.rng('scale')},{n})", float(scale[-1]), "0.000")
    b.row("Days with a score", f"=COUNT({b.rng('z')})", int(scored.sum()), "0")
    fl = b.row("Days flagged (|z| > T)", f"=SUM({b.rng('flag')})", np.nansum(flag), "0")
    hit = b.row("... of which labelled `spike`", f'=COUNTIFS({b.rng("flag")},1,{b.rng("event")},"spike")', caught, "0")
    b.row("Labelled spikes in the data", f'=COUNTIF({b.rng("event")},"spike")', int(sp.sum()), "0")
    b.row("Labelled spikes that have a score (after day 42)", f'=COUNTIFS({b.rng("event")},"spike",{b.rng("scale")},">0")',
          spikes_scored, "0")
    fa = b.row("... flagged on ordinary days (false alarms)", f'=COUNTIFS({b.rng("flag")},1,{b.rng("event")},"none")', fa_normal, "0")
    sf = b.row("... flagged during the level shift", f'=COUNTIFS({b.rng("flag")},1,{b.rng("event")},"shift")', shift_flagged, "0")
    b.row("Day number the level shift starts", f'=MATCH("shift",{b.rng("event")},0)', first_shift_day, "0")
    lastf = b.row("Last day number flagged inside the shift", f"=MAX({b.rng('shift_flag_day')})", last_shift_flag, "0")
    b.row("Weekend days flagged as 'seasonal' anomalies",
          f'=COUNTIFS({b.rng("flag")},1,{b.rng("weekday")},"Sat",{b.rng("event")},"none")+COUNTIFS({b.rng("flag")},1,{b.rng("weekday")},"Sun",{b.rng("event")},"none")',
          int(((flag == 1) & weekend & (ev == "none")).sum()), "0")
    # worked example: the day of the first scored spike dropout
    r63 = 63 + 2
    ex_base = b.row("Baseline on 2026-03-09 (C)", f"=Data!E{r63}", float(base[63]), "0.00")
    b.row("Residual on 2026-03-09 (C)", f"=Data!F{r63}", float(resid[63]), "0.00")
    b.row("Robust z on 2026-03-09", f"=Data!I{r63}", float(z[63]), "0.00")

    b.section("4. Threshold sensitivity (days flagged by group)")
    rows, exp = [], {}
    for i, t in enumerate(THRS):
        r = b.next_row + 1 + i
        rows.append([t, f'=COUNTIFS({b.rng("abs_z")},">"&A{r},{b.rng("event")},"none")',
                     f'=COUNTIFS({b.rng("abs_z")},">"&A{r},{b.rng("event")},"spike")',
                     f'=COUNTIFS({b.rng("abs_z")},">"&A{r},{b.rng("event")},"shift")',
                     f'=COUNTIFS({b.rng("abs_z")},">"&A{r},{b.rng("weekday")},"Sat")+COUNTIFS({b.rng("abs_z")},">"&A{r},{b.rng("weekday")},"Sun")'])
        exp.update({(i, 1): int(((absz > t) & (ev == "none")).sum()), (i, 2): int(((absz > t) & sp).sum()),
                    (i, 3): int(((absz > t) & (ev == "shift")).sum()), (i, 4): int(((absz > t) & weekend).sum())})
    s0, s1 = b.table(["T", "flags on ordinary days", f"flags on spikes (of {spikes_scored})", "flags during shift",
                      "flags on weekends"], rows, fmt={0: "0.0"}, expect=exp)
    b.line_chart("Temperature, baseline (C)", "date", ["temp_c", "baseline"], anchor="H24", y_title="C")
    b.line_chart("Robust z-score", "date", ["z"], anchor="H44", y_title="z")

    sweep = {t: (int(((absz > t) & (ev == "none")).sum()), int(((absz > t) & sp).sum()), int(((absz > t) & (ev == "shift")).sum()))
             for t in THRS}
    spike_days = [f"{df['date'][i]:%Y-%m-%d} ({x[i]:.1f} C)" for i in np.where(sp & scored & (flag == 1))[0]]
    missed_scored = [f"{df['date'][i]:%Y-%m-%d}" for i in np.where(sp & scored & (flag != 1))[0]]
    early_spike = f"{df['date'][np.where(sp & ~scored)[0][0]]:%Y-%m-%d}"
    safe_t = [t for t in THRS if sweep[t][0] == 0 and sweep[t][1] == spikes_scored]
    b.answers([
        ("Mean temperature by weekday, first 6 weeks; spread between highest and lowest", f"={rngr}",
         f"Weekdays sit near {np.mean([prof_mean[w] for w in DAYS[:5]]):.1f} C, Saturday {prof_mean['Sat']:.1f} C, Sunday {prof_mean['Sun']:.1f} C: "
         f"a weekly swing of {max(prof_mean.values()) - min(prof_mean.values()):.1f} C, far larger than the day-to-day noise (about 1 C)."),
        (f"Naive detector (median {med0:.1f} C, robust sigma {sc0:.2f} C, T = {T_DEF}): days flagged and how many are weekends", f"={nf}",
         f"{int(flagn.sum())} flagged, {int(flagn[weekend].sum())} of them Saturdays/Sundays. Nothing is wrong at the weekend - the detector simply "
         f"does not know about the cycle. The rest are the spikes and the level-shift days."),
        ("Seasonal baseline, residual, robust scale and z for 2026-03-09", f"={ex_base}",
         f"Baseline {base[63]:.2f} C (median of the previous four Mondays), observed {x[63]:.1f} C, residual {resid[63]:+.2f} C, "
         f"scale {scale[63]:.2f} C, z = {z[63]:.1f}. A sensor dropout: far beyond {T_DEF}."),
        (f"Seasonal detector, T = {T_DEF}: days flagged, labelled spikes caught, false alarms on ordinary days", f"={fl}",
         f"{int(np.nansum(flag))} flags: {caught} labelled spikes ({', '.join(spike_days)}), {shift_flagged} days inside the level shift, "
         f"and {fa_normal} on ordinary days. No weekend is flagged unless something else is wrong."),
        ("Which labelled spike is not detected, and why?", f"={hit}",
         f"The spike on {early_spike} falls in the first 42 days, which have no baseline/scale yet"
         + (f"; also not flagged: {', '.join(missed_scored)}." if missed_scored else ". All other labelled spikes are caught.")),
        ("Level shift: how many days are flagged, when does flagging stop, and why?", f"={sf}",
         f"{shift_flagged} of {len(shift_idx)} shifted days flagged; the last flag is day {last_shift_flag} (shift began on day {first_shift_day}). "
         f"Two things silence it: the shifted residuals quickly fill the 28-day window used for the robust scale (a quarter of it after one week, "
         f"half after two), so sigma-hat grows from about {scale[111]:.1f} C to {np.nanmax(scale[112:]):.1f} C and z falls below T; and after about three weeks "
         f"the four-same-weekday baseline has adopted the new level anyway. The process is still 6 C too hot. "
         f"Point detectors do not report persistent shifts for long - use CUSUM (lesson 27)."),
        ("Threshold sensitivity T = 2.5 ... 6: choose a T", f"=Analysis!B{s0 + 2}",
         "Flags on ordinary days / spikes caught / shift days flagged: "
         + "; ".join(f"T={t}: {sweep[t][0]}/{sweep[t][1]}/{sweep[t][2]}" for t in THRS)
         + f". T values {', '.join(str(t) for t in safe_t)} catch all {spikes_scored} scorable spikes with no false alarm; "
           f"the largest of these leaves the most margin before a real spike is missed."),
        ("Limitations of the seasonal robust-z approach", "see text",
         "It needs 6 weeks of history before it scores anything; holidays and one-off events break the 'same weekday' assumption; "
         "heavy-tailed noise gives more flags than the Gaussian 0.05 % per day implies; a level shift is flagged briefly and then silently adopted as the new normal."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-28-anomaly", "28 · Time-series anomaly detection",
             "Weekday-aware baseline and robust z-scores: injected spikes are caught, weekends are not false alarms; "
             "a level shift is flagged for about a week and then absorbed.", df.rename(columns={"date": "time"}), "time")
    d.stat("Seasonal detector (T = 3.5)", {"days flagged": float(np.nansum(flag)), "spikes caught": caught,
                                           "false alarms (ordinary days)": fa_normal, "shift days flagged": shift_flagged},
           "Of the 6 labelled spikes only 5 can be scored (one is in the first 6 weeks).", decimals=0, w=12)
    d.stat("Naive weekday-blind detector", {"days flagged": float(flagn.sum()), "of which weekends": float(flagn[weekend].sum())},
           "Same threshold, one global baseline: a flood of weekend false alarms.", decimals=0, w=12,
           thresholds=[(None, "green"), (5, "red")])
    ts = pd.DataFrame({"time": df["date"], "temp_c": x, "baseline": base, "upper": base + T_DEF * scale,
                       "lower": base - T_DEF * scale,
                       "flagged": np.where(flag == 1, x, np.nan)})
    d.timeseries("Daily temperature, seasonal baseline and alarm band", ts,
                 "Baseline = median of the previous four same weekdays; band = baseline +/- T x robust scale. Dots = flagged days.",
                 points=["flagged"], dashed=["upper", "lower"], unit="celsius",
                 colors={"temp_c": "#4E79A7", "baseline": "#76B7B2", "upper": "#E15759", "lower": "#E15759", "flagged": "#F28E2B"},
                 w=24, h=9)
    zs = pd.DataFrame({"time": df["date"], "z_seasonal": z, "T": T_DEF, "minus_T": -T_DEF})
    d.timeseries("Robust residual z-score", zs, "The shift shows as a block of high z that decays as the baseline catches up.",
                 dashed=["T", "minus_T"], colors={"z_seasonal": "#4E79A7", "T": "#E15759", "minus_T": "#E15759"})
    zn_df = pd.DataFrame({"time": df["date"], "z_naive": zn, "T": T_DEF, "minus_T": -T_DEF})
    d.timeseries("Naive z-score (no seasonal baseline)", zn_df, "Every weekend sits far below -T: the weekday cycle is read as an anomaly.",
                 dashed=["T", "minus_T"], colors={"z_naive": "#B07AA1", "T": "#E15759", "minus_T": "#E15759"})
    prof_df = pd.DataFrame({"weekday": DAYS, "mean temp (C)": [prof_mean[w] for w in DAYS]})
    d.bars("Weekday profile, first 6 weeks (C)", prof_df, "The seasonal swing is about 11 C; the noise is about 1 C.", w=12)
    fl_tbl = pd.DataFrame({"date": df["date"].dt.strftime("%Y-%m-%d"), "weekday": wd, "temp_c": x,
                           "z": z.round(1), "event": ev})[flag == 1]
    d.table("Days flagged by the seasonal detector", fl_tbl, "event is the ground-truth label from the maintenance log.", w=12)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: time-series anomaly detection

## The failure this prevents

A temperature that is 8 C lower than usual is an emergency on a Wednesday and perfectly normal on a Sunday. A detector
that compares each reading with one global mean and spread cannot tell the two apart: it floods the on-call engineer with
weekend alarms until the alerts are muted - and then misses the real spike. Anomaly detection for time series is therefore
mostly about **building the right expectation first** (trend, seasonality) and only then asking how surprising the data are.

## Types of anomaly

- **Point anomaly**: a single reading far from its expected value (sensor dropout, transient spike).
- **Level shift**: the series jumps and stays (fouling, recalibration, a new setpoint). Several consecutive points are anomalous.
- **Contextual anomaly**: a value that is ordinary overall but wrong *for its context* (25 C on a Sunday when Sundays are 41 C).
- **Variance change**: the noise itself becomes larger or smaller (see [rolling statistics](../10-rolling-statistics/theory.md)).

## Expected value: a seasonal baseline

Write $x_t=\text{baseline}_t+e_t$. With a weekly cycle one simple, robust baseline is the **median of the same weekday in the
previous $m$ weeks**:

$$\hat b_t=\operatorname{median}\bigl(x_{t-7},x_{t-14},\dots,x_{t-7m}\bigr),\qquad e_t=x_t-\hat b_t .$$

Using only past values makes the detector *online* (it never peeks at the future), and the median means one earlier spike
does not corrupt the baseline. Here $m=4$, so the first 28 days produce no baseline. The residual $e_t$ is noisier than the
raw noise because $\hat b_t$ is itself an estimate: with four values the median has a standard deviation of roughly 0.6 times that of one
observation, which inflates the residual standard deviation by about 15-20 %. This is why the *scale* must be estimated from the residuals, not from the raw readings.

## Robust residual score

Scale the residual by a robust estimate of its usual size. With $\mathrm{MAD}=\operatorname{median}|e-\operatorname{median}(e)|$ and, since
residuals are already centred near 0, the median absolute residual over the last $w$ days:

$$\hat\sigma_t = 1.4826\cdot\operatorname{median}\bigl(|e_{t-w}|,\dots,|e_{t-1}|\bigr),\qquad z_t=\frac{e_t}{\hat\sigma_t}.$$

The constant $1.4826=1/\Phi^{-1}(0.75)$ makes $\hat\sigma$ consistent with the standard deviation for Gaussian noise
(equivalently the "modified z-score" of Iglewicz and Hoaglin multiplies by $0.6745$). Flag the day when $|z_t|>T$.
Median and MAD resist the very anomalies we are trying to find; a mean and standard deviation would be inflated by them
([lesson 2](../02-robust-statistics/theory.md), [lesson 4](../04-outlier-detection/theory.md)).

## Worked example

Previous four Mondays: 52.4, 53.1, 52.8, 51.9. The median is $(52.4+52.8)/2=52.6$. Today's reading is 59.4, so
$e=6.8$. The last 7 absolute residuals are 0.4, 1.1, 0.7, 1.6, 0.2, 0.9, 1.3 with median 0.9, so $\hat\sigma=1.4826\cdot0.9=1.33$ and
$z=6.8/1.33=5.1$. With $T=3.5$ this is an alarm. Under pure Gaussian noise $P(|Z|>3.5)=4.65\times10^{-4}$, i.e. about 0.17 false
alarms per year of daily data - but real residuals have heavier tails, so expect more.

## Choosing T and the adaptation time

Raising $T$ lowers false alarms and misses small anomalies; the trade-off is quantified in
[lesson 29](../29-false-alarms-and-detection-performance/theory.md). Two things limit how long a **level shift** is
flagged. The baseline (median of four weeks) is half-absorbed after two weeks and fully absorbed after three. Faster still,
the shifted residuals enter the rolling window that estimates the scale, which inflates $\hat\sigma$ and shrinks $z$ - in this
lesson's data the shift is flagged for only about a week. Re-learning is useful after a legitimate setpoint change and dangerous
when a real, permanent fault is accepted as normal.
Pair a point detector with a change-point detector such as CUSUM ([lesson 27](../27-change-point-detection/theory.md)) or a
fixed reference level.

## Assumptions and pitfalls

1. **The season is stable.** Holidays, daylight-saving shifts and product launches change the cycle; flags cluster around them.
2. **Warm-up costs history.** The first $7m$ + $w/2$ days cannot be scored; anomalies there are invisible.
3. **Contaminated baselines and scales.** If two of the four earlier same weekdays were anomalous the median is wrong; a long run of
   anomalies also inflates the rolling scale. A longer window, or excluding already-flagged days from the scale, helps.
4. **Heavy tails and autocorrelation** make the Gaussian false-alarm rate optimistic ([lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md)).
5. **Trend.** A drifting series has a lagging baseline; detrend or use a regression baseline
   ([lesson 7](../07-trend-seasonality-and-noise/theory.md), [lesson 22](../22-trend-and-seasonal-regression-forecasting/theory.md)).
6. **Multiple testing.** Scoring 365 days with $T=3$ is 365 chances to alarm; the daily error rate is not the yearly one.

## Related notes

- [Seasonal naive forecasts](../21-naive-and-seasonal-naive-forecasts/theory.md) - the baseline above is a seasonal naive forecast with a median
- [Statistical process control](../26-statistical-process-control/theory.md)
- Repo notes: [seasonality and trends](../../notes/time_series/seasonality_and_trends.md)
"""

TASK = r"""
# Task: time-series anomaly detection

## Scenario

A refrigeration compressor housing has a temperature probe whose **daily mean** is logged. The plant runs Monday to Friday and idles
at the weekend. The current alert rule ("one global robust z-score, alarm above 3.5") pages the on-call technician every
weekend, so the team wants to switch it off. Before they do, you must build a detector that respects the weekly cycle,
test it against the maintenance log, and say which kinds of events it can and cannot catch.

## Data

`data.csv` - 154 daily means (22 weeks, Monday 2026-01-05 to Sunday 2026-06-07).

| column | meaning |
|---|---|
| `date` | calendar day |
| `weekday` | Mon ... Sun |
| `temp_c` | daily mean housing temperature, degrees Celsius |
| `event` | maintenance log label: `none`, `spike` (brief fault, one day) or `shift` (a persistent change, every day from the first labelled day on) |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the mean temperature for each weekday over the first 6 weeks (days 1-42). How large is the spread between the highest and the
   lowest weekday?
2. *Naive detector.* Take the median and $1.4826\times\mathrm{MAD}$ of days 1-42, standardise all 154 days and flag $|z|>3.5$.
   How many days are flagged, and how many of them are Saturdays or Sundays?
3. For 2026-03-09 compute the seasonal baseline (median of the previous four same weekdays), the residual, the robust scale (
   $1.4826\times$ the median absolute residual of the previous up-to-28 residuals) and the z-score.
4. Score every day from day 43 on. With $T=3.5$: how many days are flagged, how many of the labelled spikes are caught and how many
   flags fall on ordinary days (`none`)?
5. Which labelled spike is not detected, and why?
6. For the `shift` period: how many days are flagged, on which day does the flagging stop, and why does it stop although the
   process is still wrong?
7. Repeat the count of flags by group for $T=2.5, 3, 3.5, 4, 5, 6$. Which $T$ would you use, and what do you give up at each end?
8. *Limitations:* name two situations in which this seasonal detector fails (data or process), and one thing you would add to it.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Daily temperature, seasonal baseline and alarm band", where are the orange dots and which labelled events do they match?
- Compare "Naive z-score" with "Robust residual z-score": what pattern does the first show that the second removes?
- In "Days flagged by the seasonal detector", which `event` values appear, and what does that say about the false-alarm rate?

## Deliverable

A short note (5-8 lines) with three named parts: **Recommendation** (replace the old rule or not, with the T you chose),
**Evidence** (flags, catches, false alarms, weekend flags before and after) and **Blind spots** (what it will not catch, e.g. a persistent shift).
"""
