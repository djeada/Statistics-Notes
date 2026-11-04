"""Lesson 27 - Change-point detection (CUSUM and the best two-mean split)."""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "27-change-point-detection"
TITLE = "Change-point detection"
MODULE = "Statistical monitoring and decision-making"
DATASET = "240 hourly reactor-jacket temperature readings (C) with a small mean shift hidden in the noise"
N0 = 100      # phase-I readings used to estimate mu0 and sigma0
K_REF = 0.5   # CUSUM reference value (in sigma units)
H_DEC = 5.0   # CUSUM decision threshold (in sigma units)
HS = [2, 3, 4, 5, 6, 8]


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(2710)
    n = 240
    x = 70.0 + 0.8 * rng.standard_normal(n)
    x[60] += 3.4            # a one-off spike during phase I (a Shewhart chart would shout, CUSUM should not)
    x[140:] += 0.7          # the real change: a sustained +0.7 C shift (about 0.9 sigma) from reading 141
    t = pd.date_range("2026-05-04 00:00:00", periods=n, freq="h")
    return pd.DataFrame({"timestamp": t, "reading": np.arange(1, n + 1), "temp_c": x.round(2)})


def cusum(z: np.ndarray, k: float):
    hi, lo = np.zeros(len(z)), np.zeros(len(z))
    for i in range(len(z)):
        hi[i] = max(0.0, (hi[i - 1] if i else 0.0) + z[i] - k)
        lo[i] = max(0.0, (lo[i - 1] if i else 0.0) - z[i] - k)
    return hi, lo


def arl0_one(k, h):
    b = h + 1.166
    return (math.exp(2 * k * b) - 2 * k * b - 1) / (2 * k * k)


def arl1_one(k, h, delta):
    b, d = h + 1.166, delta - k
    return (math.exp(-2 * d * b) + 2 * d * b - 1) / (2 * d * d)


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    x = df["temp_c"].to_numpy()
    n = len(x)
    read = df["reading"].to_numpy()
    mu0, sd0 = x[:N0].mean(), x[:N0].std(ddof=1)
    z = (x - mu0) / sd0
    hi, lo = cusum(z, K_REF)
    smax = np.maximum(hi, lo)
    runmax = np.maximum.accumulate(smax)
    first_alarm = int(np.argmax(smax > H_DEC)) + 1
    # last reading at which C+ was zero (running)
    last_zero = np.zeros(n)
    cur = 0
    for i in range(n):
        if hi[i] == 0:
            cur = read[i]
        last_zero[i] = cur
    onset = last_zero[first_alarm - 1] + 1
    # best split (SSE of two-mean fit); split after reading j, j in 10..n-10
    sse = np.full(n, np.nan)
    for j in range(10, n - 9):
        a, c = x[:j], x[j:]
        sse[j - 1] = ((a - a.mean()) ** 2).sum() + ((c - c.mean()) ** 2).sum()
    tau = int(np.nanargmin(sse)) + 1
    m1, m2 = x[:tau].mean(), x[tau:].mean()
    sse0 = ((x - x.mean()) ** 2).sum()
    sse_min = float(np.nanmin(sse))
    shift = m2 - m1
    delta = shift / sd0
    tstat = shift / (math.sqrt(sse_min / (n - 2)) * math.sqrt(1 / tau + 1 / (n - tau)))
    shew_all = int((np.abs(z) > 3).sum())
    shew_p1 = int((np.abs(z[:N0]) > 3).sum())
    shew_first = int(np.argmax(np.abs(z) > 3)) + 1

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 27 - Change-point detection",
             "Yellow cells (k, h) are assumptions. CUSUM, the split search and the trade-off table are live formulas.")
    D = lambda name: b.rng(name)  # noqa: E731
    b.section("1. Phase I: what 'normal' looks like (readings 1-100)")
    mu0c = b.row("mu0 = mean of readings 1-100 (C)", f"=AVERAGE(Data!$C$2:$C${N0 + 1})", mu0, "0.000")
    sd0c = b.row("sigma0 = STDEV of readings 1-100 (C)", f"=STDEV(Data!$C$2:$C${N0 + 1})", sd0, "0.000",
                 "Sample SD; phase I includes the one-off spike")
    b.add_column("z", lambda r: f"=(Data!C{r}-{mu0c})/{sd0c}", expected=z)
    b.section("2. CUSUM with reference value k and decision threshold h")
    kc = b.row("k (reference value, sigma units)", K_REF, None, "0.00", "Edit me: half the shift you want to catch", True)
    hc = b.row("h (decision threshold, sigma units)", H_DEC, None, "0.00", "Edit me: larger h = fewer false alarms, slower alarm", True)
    b.add_column("cusum_hi", lambda r: f"=MAX(0,{'0' if r == 2 else 'Data!E' + str(r - 1)}+Data!{b.col('z')}{r}-{kc})", expected=hi)
    assert b.col("cusum_hi") == "E"
    b.add_column("cusum_lo", lambda r: f"=MAX(0,{'0' if r == 2 else 'Data!F' + str(r - 1)}-Data!{b.col('z')}{r}-{kc})", expected=lo)
    assert b.col("cusum_lo") == "F"
    b.add_column("stat_max", lambda r: f"=MAX(Data!E{r},Data!F{r})", expected=smax)
    b.add_column("alarm", lambda r: f"=IF(Data!G{r}>{hc},1,0)", expected=(smax > H_DEC).astype(float), fmt="0")
    b.add_column("runmax", lambda r: f"=Data!G{r}" if r == 2 else f"=MAX(Data!I{r - 1},Data!G{r})", expected=runmax)
    assert b.col("runmax") == "I"
    b.add_column("last_zero", lambda r: (f"=IF(Data!E{r}=0,Data!B{r},0)" if r == 2 else f"=IF(Data!E{r}=0,Data!B{r},Data!J{r - 1})"),
                 expected=last_zero, fmt="0")
    assert b.col("last_zero") == "J"
    sh_all = b.row("Readings beyond +/-3 sigma0 (Shewhart rule), all 240", f'=COUNTIF({D("z")},">3")+COUNTIF({D("z")},"<-3")',
                   shew_all, "0")
    b.row("... of which in phase I (readings 1-100)", f'=COUNTIF(Data!$D$2:$D${N0 + 1},">3")+COUNTIF(Data!$D$2:$D${N0 + 1},"<-3")',
          shew_p1, "0",
          "Single-point rule: the spike counts here")
    fa = b.row("First CUSUM alarm (reading number)", f"=MATCH(1,{D('alarm')},0)", first_alarm, "0")
    b.row("... timestamp", f"=INDEX(Data!$A$2:$A${n + 1},{b.local(fa)})", None, "yyyy-mm-dd hh:mm")
    b.row("C+ at the alarm", f"=INDEX({D('cusum_hi')},{b.local(fa)})", float(hi[first_alarm - 1]), "0.00")
    b.row("C- at the alarm", f"=INDEX({D('cusum_lo')},{b.local(fa)})", float(lo[first_alarm - 1]), "0.00",
          "Only the upper side moved: an upward shift")
    on = b.row("CUSUM estimate of the change start (reading)", f"=INDEX({D('last_zero')},{b.local(fa)})+1", onset, "0",
               "Last time C+ was 0, plus 1")

    b.section("3. Best single split: minimise SSE of a two-mean fit")
    # SSE for split after reading j (rows 2..j+1 | j+2..n+1)
    b.add_column("sse_split", lambda r: f"=DEVSQ(Data!$C$2:C{r})+DEVSQ(Data!C{r + 1}:$C${n + 1})", expected=sse, fmt="0.00")
    assert b.col("sse_split") == "K"
    sr = D("sse_split")
    tc = b.row("Best split: change occurs after reading", f"=MATCH(MIN({sr}),{sr},0)", tau, "0")
    sse1 = b.row("SSE, one mean for everything", f"=DEVSQ({D('temp_c')})", sse0, "0.00")
    ssem = b.row("SSE, two means at the best split", f"=MIN({sr})", sse_min, "0.00")
    b.row("SSE reduction", f"=1-{b.local(ssem)}/{b.local(sse1)}", 1 - sse_min / sse0, "0.0%")
    m1c = b.row("Mean before the split (C)", f"=AVERAGE(OFFSET(Data!$C$2,0,0,{b.local(tc)},1))", m1, "0.000")
    m2c = b.row("Mean after the split (C)", f"=AVERAGE(OFFSET(Data!$C$2,{b.local(tc)},0,{n}-{b.local(tc)},1))", m2, "0.000")
    shc = b.row("Estimated shift (C)", f"={b.local(m2c)}-{b.local(m1c)}", shift, "0.000")
    dc = b.row("Estimated shift in sigma0 units", f"={b.local(shc)}/{b.local(sd0c)}", delta, "0.00")
    b.row("t-statistic of the two means at the split", f"={b.local(shc)}/(SQRT({b.local(ssem)}/({n}-2))*SQRT(1/{b.local(tc)}+1/({n}-{b.local(tc)})))",
          tstat, "0.0", "Optimistic: the split was chosen to maximise it")
    b.row("CUSUM alarm delay after the best split (readings)", f"={b.local(fa)}-{b.local(tc)}", first_alarm - tau, "0")

    b.section("4. Detection delay versus false alarm trade-off (k as above)")
    rows, exp = [], {}
    for i, h in enumerate(HS):
        r = b.next_row + 1 + i
        fa_h = int(min(np.sum(runmax <= h) + 1, n + 1))
        arl0 = arl0_one(K_REF, h) / 2
        arl1 = arl1_one(K_REF, h, delta)
        rows.append([h, f'=COUNTIF({D("runmax")},"<="&A{r})+1',
                     f'=IF(B{r}<={b.local(tc)},"false alarm","real")',
                     f'=IF(B{r}>{b.local(tc)},B{r}-{b.local(tc)},"")',
                     f"=(EXP(2*{b.local(kc)}*(A{r}+1.166))-2*{b.local(kc)}*(A{r}+1.166)-1)/(2*{b.local(kc)}^2)/2",
                     f"=(EXP(-2*({b.local(dc)}-{b.local(kc)})*(A{r}+1.166))+2*({b.local(dc)}-{b.local(kc)})*(A{r}+1.166)-1)/(2*({b.local(dc)}-{b.local(kc)})^2)"])
        exp.update({(i, 1): fa_h, (i, 4): arl0, (i, 5): arl1})
        if fa_h > tau:
            exp[(i, 3)] = fa_h - tau
    t0, t1 = b.table(["h", "First alarm (reading)", "Verdict", "Delay after split", "ARL0 approx (readings)",
                      "ARL1 approx at estimated shift"], rows, fmt={1: "0", 3: "0", 4: "0", 5: "0.0"}, expect=exp)
    b.line_chart("Temperature (C)", "reading", ["temp_c"], anchor="H4", y_title="C")
    b.line_chart("CUSUM statistics (sigma units)", "reading", ["cusum_hi", "cusum_lo"], anchor="H24", y_title="sigma units")
    b.line_chart("SSE of the two-mean fit by split point", "reading", ["sse_split"], anchor="H44", y_title="SSE")

    # facts for answers
    res = {}
    for kk, hh in [(0.25, 5.0), (1.0, 5.0), (0.5, 3.0)]:
        h_, l_ = cusum(z, kk)
        s_ = np.maximum(h_, l_)
        res[(kk, hh)] = int(np.argmax(s_ > hh)) + 1
    hs_first = {h: int(min(np.sum(runmax <= h) + 1, n + 1)) for h in HS}
    b.answers([
        ("mu0 and sigma0 from readings 1-100 (C)", f"={mu0c}",
         f"mu0 = {mu0:.3f} C, sigma0 = {sd0:.3f} C (sample SD)."),
        ("Readings beyond +/-3 sigma0: total, and in phase I", f"={sh_all}",
         f"{shew_all} in total; the first is reading {shew_first}. In phase I there are {shew_p1}: the single spike at reading 61 "
         f"({x[60]:.2f} C). The shift after reading 140 only produces a handful of 3-sigma points - the Shewhart rule barely sees it."),
        (f"First CUSUM alarm with k = {K_REF}, h = {H_DEC:g} (reading, timestamp)", f"={fa}",
         f"Reading {first_alarm} ({df['timestamp'][first_alarm - 1]:%Y-%m-%d %H:%M}), upper side. The phase-I spike lifts C+ to about "
         f"{hi[60]:.1f} but not past h."),
        ("CUSUM estimate of when the shift began", f"={on}",
         f"Reading {int(onset)} (last time C+ was zero, plus one): the alarm fired {first_alarm - int(onset)} readings after the CUSUM-estimated start."),
        ("Best split of the series (reading, means, shift in C and in sigma0)", f"={tc}",
         f"Split after reading {tau}: mean {m1:.3f} C before, {m2:.3f} C after, a shift of {shift:+.3f} C = {delta:.2f} sigma0. "
         f"The fit removes {1 - sse_min / sse0:.1%} of the SSE of a single mean."),
        ("Delay between the best split and the CUSUM alarm (readings)", f"={fa}-{tc}",
         f"{first_alarm - tau} readings, i.e. {first_alarm - tau} hours."),
        ("Trade-off table over h: which h raise a false alarm, which are slow?", f"=Analysis!B{t0 + 3}",
         f"First alarms for h = {', '.join(map(str, HS))}: {', '.join(str(hs_first[h]) for h in HS)}. Alarms at or before reading {tau} are false "
         f"alarms (the phase-I spike). h = 5 is the smallest value that avoids them; each +1 of h costs about "
         f"{(hs_first[8] - hs_first[5]) / 3:.1f} extra readings of delay but multiplies ARL0 by roughly e^(2kh)."),
        ("Change k to 0.25 and to 1.0 (h = 5): what happens to the alarm?", f"={fa}",
         f"k = 0.25 -> first alarm at reading {res[(0.25, 5.0)]} (that is the phase-I spike: too little allowance, so noise accumulates); "
         f"k = 1.0 -> reading {res[(1.0, 5.0)]} (an allowance close to the whole shift of {delta:.2f} sigma0 leaves C+ growing very slowly). "
         f"A k near half the shift ({delta / 2:.2f} sigma0) balances the two."),
        ("Limitations of the two methods", "see text",
         "The SSE split assumes exactly one change, constant variance and independent readings; it will always return a 'best' "
         "split even when nothing changed. CUSUM needs mu0/sigma0 from a clean phase I and k, h chosen for a target shift; "
         "autocorrelated sensors shorten ARL0 and cause more false alarms than the table promises."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-27-change-point", "27 · Change-point detection",
             "A small mean shift hidden in sensor noise: Shewhart limits, CUSUM with threshold h, and the SSE-minimising split.",
             df.rename(columns={"timestamp": "time"}), "time")
    d.stat("Phase I and estimated shift", {"mu0 (C)": mu0, "sigma0 (C)": sd0, "shift (C)": shift, "shift (sigma0)": delta},
           "mu0 and sigma0 from readings 1-100; the shift is the difference of the two means at the best split.",
           decimals=2, w=12)
    d.stat("Where the change is found (reading no.)", {"best split": tau, "CUSUM alarm": first_alarm,
                                                       "delay (readings)": first_alarm - tau},
           "The CUSUM alarm comes a few readings after the best split, as it must: it needs time to accumulate evidence.",
           decimals=0, w=12)
    ts = df[["timestamp"]].rename(columns={"timestamp": "time"}).copy()
    ts["temp_c"] = x
    ts["mu0"] = mu0
    ts["ucl_3sigma"] = mu0 + 3 * sd0
    ts["lcl_3sigma"] = mu0 - 3 * sd0
    ts["two_mean_fit"] = np.where(read <= tau, m1, m2)
    d.timeseries("Temperature with Shewhart limits and the two-mean fit", ts,
                 f"The shift is only about {delta:.1f} sigma: almost every point stays inside the 3-sigma limits, but the stepped fit "
                 "shows a clear change.", dashed=["mu0", "ucl_3sigma", "lcl_3sigma"], unit="celsius",
                 colors={"temp_c": "#4E79A7", "mu0": "#76B7B2", "ucl_3sigma": "#E15759", "lcl_3sigma": "#E15759",
                         "two_mean_fit": "#F28E2B"}, w=24, h=9)
    cs = df[["timestamp"]].rename(columns={"timestamp": "time"}).copy()
    cs["C_plus"] = np.minimum(hi, 3 * H_DEC)
    cs["C_minus"] = np.minimum(lo, 3 * H_DEC)
    cs["h"] = H_DEC
    d.timeseries("CUSUM statistics vs decision threshold h", cs,
                 "C+ climbs steadily after the shift and crosses h; the phase-I spike makes a bump that decays. Display clipped at 3h.",
                 dashed=["h"], colors={"C_plus": "#F28E2B", "C_minus": "#4E79A7", "h": "#E15759"})
    ss = df[["timestamp"]].rename(columns={"timestamp": "time"}).copy()
    ss["sse_two_mean_fit"] = sse
    d.timeseries("SSE of the two-mean fit by candidate split", ss,
                 "Each point is the SSE if the change happened after that reading. The minimum is the estimated change point.",
                 colors={"sse_two_mean_fit": "#B07AA1"})
    trade = pd.DataFrame({"h": [str(h) for h in HS], "first alarm (reading)": [hs_first[h] for h in HS],
                          "best split (reading)": [tau] * len(HS)})
    d.bars("Choosing h: first alarm vs the true change", trade,
           "An alarm before the best-split reading is a false alarm (the phase-I spike). Larger h waits a little longer.", w=12)
    tab = pd.DataFrame({"h": HS, "alarm": [hs_first[h] for h in HS],
                        "verdict": ["false alarm" if hs_first[h] <= tau else "real" for h in HS],
                        "delay": [hs_first[h] - tau if hs_first[h] > tau else None for h in HS],
                        "ARL0": [round(arl0_one(K_REF, h) / 2) for h in HS],
                        "ARL1": [round(arl1_one(K_REF, h, delta), 1) for h in HS]})
    d.table("Trade-off table (k = 0.5)", tab, "ARL0 = readings between false alarms, ARL1 = readings to detect the estimated shift "
            "(Siegmund approximation).", w=12)
    d.save(out)

    md(out / "theory.md", THEORY.replace("@TAU@", str(tau)).replace("@FIRST@", str(first_alarm)))
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: change-point detection

## The problem a single threshold cannot solve

A sensor that drifts from 70.0 C to 70.7 C will almost never produce a point outside the usual +/-3 sigma limits when the
noise is 0.8 C - yet the process has changed, and a month later the change may be expensive. Shewhart-style rules look at
**one reading at a time** and need a large jump. A **change-point** method looks at the *accumulated* evidence of many small
deviations, trading a little delay for much more sensitivity. Two complementary tools are used here: an **online** detector
(CUSUM: "has something changed *yet*?") and an **offline** estimator (the best split: "*when* did it change?").

## Model

Readings $x_1,\dots,x_n$ are independent with mean $\mu_0$ before an unknown change time $\tau$ and $\mu_1=\mu_0+\delta\sigma$
after it, with constant standard deviation $\sigma$. Estimate $\mu_0,\sigma$ from a phase-I stretch known to be in control and
standardise: $z_t=(x_t-\mu_0)/\sigma$.

## CUSUM

Two one-sided sums accumulate the part of each deviation that exceeds the **reference value** $k$ (the allowance):

$$C_t^{+}=\max\bigl(0,\;C_{t-1}^{+}+z_t-k\bigr),\qquad C_t^{-}=\max\bigl(0,\;C_{t-1}^{-}-z_t-k\bigr),\qquad C_0^{\pm}=0.$$

An alarm is raised the first time $C_t^{\pm}>h$, the **decision threshold**. Interpretation:

- $k$ is usually set to **half the shift you want to catch**: $k=\delta/2$ (so $k=0.5$ targets a 1-sigma shift). Deviations smaller
  than $k$ push the sum back to zero, so ordinary noise cannot accumulate.
- $h$ controls how much accumulated evidence you demand; $h=4$ or $5$ with $k=0.5$ is the textbook default.
- The point where $C^{+}$ last equalled 0 before the alarm is a natural estimate of the change start.

Worked example ($k=0.5$): standardised readings $0.2,\;0.9,\;1.1,\;0.6,\;1.4$ give
$C^{+}=\max(0,0.2-0.5)=0,\;0.4,\;1.0,\;1.1,\;2.0$. No single reading exceeds 1.5 sigma, but the sum reaches 2.0 after five
readings; with $h=2$ that is an alarm, with $h=5$ it would still be silent.

## Best split (offline estimate of $\tau$)

For every candidate split $j$ fit one mean to $x_1..x_j$ and another to $x_{j+1}..x_n$ and compute the total
sum of squared errors

$$\mathrm{SSE}(j)=\sum_{t\le j}(x_t-\bar x_{1:j})^2+\sum_{t>j}(x_t-\bar x_{j+1:n})^2 .$$

The estimate is $\hat\tau=\arg\min_j \mathrm{SSE}(j)$; under Gaussian noise this is the maximum-likelihood change point.
Worked example: $x=\{1,2,1,4,5,4\}$. A single mean (2.833) gives $\mathrm{SSE}=14.83$; splitting after $j=3$ gives means 1.333
and 4.333 and $\mathrm{SSE}=0.667+0.667=1.33$ - a 91 % reduction. The SSE-versus-$j$ curve is V-shaped, and its depth tells you
how convincing the change is. Always keep a few points at each end (here 10) since a split near the edge fits one mean to a handful of
values.

In this lesson's data the minimum is at reading @TAU@ and the CUSUM alarm comes at reading @FIRST@.

## Delay versus false alarms

Two numbers summarise a CUSUM chart. **ARL0** is the average number of readings between false alarms when nothing has changed;
**ARL1** is the average number of readings until an alarm after a real shift. Raising $h$ raises both. For one-sided CUSUM,
Siegmund's approximation with $b=h+1.166$ and $\Delta=\delta-k$ is

$$\mathrm{ARL}_1\approx\frac{e^{-2\Delta b}+2\Delta b-1}{2\Delta^2},\qquad
\mathrm{ARL}_0\approx\frac{e^{2kb}-2kb-1}{2k^2}\quad(\Delta=-k).$$

For $k=0.5,\,h=5$ this gives $\mathrm{ARL}_0\approx 938$ one-sided (about 465 for the two-sided chart) and $\mathrm{ARL}_1\approx 10$ readings for
a 1-sigma shift. $\mathrm{ARL}_0$ grows like $e^{2kh}$ while delay grows only linearly in $h$ - so a moderate increase
of $h$ buys a lot of false-alarm protection for a few extra readings of delay.

## Assumptions and pitfalls

1. **Phase I must be clean.** If mu0 or sigma0 are estimated from data that already contain the shift, the chart is calibrated
   to the wrong target. Use a robust estimate ([lesson 2](../02-robust-statistics/theory.md)) when outliers are possible.
2. **Autocorrelation breaks the ARL numbers.** Smooth sensors have correlated errors; effective sample size is smaller and false alarms are
   more frequent than the table says ([lesson 14](../14-spurious-correlation-and-autocorrelation/theory.md)).
3. **The best split always finds something.** Even pure noise has a minimum SSE; judge the reduction in SSE, the size of the shift
   in sigma units, and whether the split is stable when you drop 10 % of the data.
4. **One change point only.** Several changes need binary segmentation or a penalised criterion; a single split between two
   shifts is a compromise.
5. **Alarm is not diagnosis.** CUSUM says the mean moved; it does not say whether the sensor drifted or the process did.
6. **Reset rules matter.** After an alarm you must decide whether to reset the sums; otherwise the chart stays "in alarm".

## Related notes

- [Statistical process control](../26-statistical-process-control/theory.md) - the Shewhart chart this lesson improves on
- [Anomaly detection](../28-time-series-anomaly-detection/theory.md) and
  [false alarms and detection performance](../29-false-alarms-and-detection-performance/theory.md)
- [Rolling statistics](../10-rolling-statistics/theory.md) and [trend and seasonality](../07-trend-seasonality-and-noise/theory.md)
- Repo notes: [stationarity](../../notes/time_series/stationarity.md), [random walk](../../notes/time_series/random_walk.md)
"""

TASK = r"""
# Task: change-point detection

## Scenario

The jacket temperature of a chemical reactor is read every hour. The set-point is 70 C and the control chart has
been quiet for two weeks, yet the quality lab suspects the reactor now runs slightly warmer than it did in early May. A
Shewhart chart (3-sigma limits) has not complained. You must decide whether the process mean has really moved, estimate when,
and propose an alarm rule that would have caught it quickly without crying wolf.

## Data

`data.csv` - 240 hourly readings from 2026-05-04 00:00 to 2026-05-13 23:00.

| column | meaning |
|---|---|
| `timestamp` | hour of the reading |
| `reading` | reading number 1-240 |
| `temp_c` | jacket temperature, degrees Celsius |

Treat readings 1-100 as **phase I** (the process is known to be in control).

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. From phase I compute $\mu_0$ (mean) and $\sigma_0$ (sample standard deviation); standardise all 240 readings.
2. How many readings fall beyond $\pm 3\sigma_0$ in total, and how many in phase I? What is special about the phase-I one?
3. Build the upper and lower CUSUM with $k = 0.5$ and $h = 5$. At which reading and timestamp is the first alarm, and on which side?
4. Estimate the start of the change from the CUSUM (last zero of $C^+$ before the alarm, plus one).
5. For every split point from reading 10 to 230 compute the two-mean SSE. Which split minimises it? Report both means, the shift
   in C and in units of $\sigma_0$, and the percentage reduction of SSE compared with a single mean.
6. How many readings after the best split does the CUSUM alarm?
7. Compute the first alarm for $h = 2, 3, 4, 5, 6, 8$ ($k$ fixed). Which values of $h$ raise a false alarm before the change? Compare their ARL0
   and delay. Which $h$ would you deploy?
8. Change $k$ to 0.25 and to 1.0 with $h = 5$. How does the alarm time change, and why?
9. *Limitations:* name two assumptions behind the split estimate and the CUSUM that this data might violate.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Temperature with Shewhart limits and the two-mean fit", does any single point justify an alarm? What does the stepped line add?
- In "CUSUM statistics vs decision threshold h", what happens to C+ around the phase-I spike and what happens after the change?
- In "SSE of the two-mean fit by candidate split", where is the minimum and how sharp is it?

## Deliverable

A short note (5-8 lines) with three named parts: **Finding** (has the mean moved, by how much, since when), **Alarm rule**
(your k and h with the reason) and **Risk** (expected false-alarm spacing and expected delay).
"""
