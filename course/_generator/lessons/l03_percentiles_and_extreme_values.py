"""Lesson 03 - Percentiles and extreme values.  REFERENCE LESSON: copy its structure for the others."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "03-percentiles-and-extreme-values"
TITLE = "Percentiles and extreme values"
MODULE = "Understanding data beyond averages"
DATASET = "600 API requests, 5 s apart (latency in ms, endpoint, HTTP status)"
SLO_MS = 250  # the threshold used in the task
WINDOW = 50  # rows per time window (= 250 s)


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(303)
    n = 600
    t = pd.date_range("2026-03-02 09:00:00", periods=n, freq="5s")
    ep = rng.choice(["search", "checkout", "profile"], size=n, p=[0.5, 0.3, 0.2])
    mu = {"search": np.log(80), "checkout": np.log(140), "profile": np.log(60)}
    sg = {"search": 0.35, "checkout": 0.45, "profile": 0.30}
    lat = np.array([rng.lognormal(mu[e], sg[e]) for e in ep])
    idx = np.arange(n)
    slow = (idx >= 360) & (idx < 456) & (ep == "checkout") & (rng.random(n) < 0.35)  # degraded DB path
    lat[slow] += rng.lognormal(np.log(900), 0.3, slow.sum())
    status = np.where(lat > 1500, 504, np.where(rng.random(n) < 0.01, 500, 200))
    return pd.DataFrame({"timestamp": t, "endpoint": ep, "latency_ms": lat.round(1), "status": status})


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    lat = df["latency_ms"].to_numpy()
    q = lambda x, p: float(np.percentile(x, p))  # numpy 'linear' == Excel/Sheets PERCENTILE (inclusive)

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 03 - Percentiles and extreme values",
             "Solved workbook. Yellow cells are assumptions you can change; everything else is a live formula.")
    L = b.rng("latency_ms")
    for e in ["search", "checkout", "profile"]:  # helper columns so PERCENTILE can ignore other endpoints
        b.add_column(f"lat_{e}", lambda r, e=e: f'=IF(Data!B{r}="{e}",Data!C{r},"")', expected=None)

    b.section("1. The average and the percentile ladder")
    mean = b.row("Mean latency (ms)", f"=AVERAGE({L})", float(lat.mean()), "0.0")
    ladder = {}
    for p in (50, 90, 95, 99):
        ladder[p] = b.row(f"P{p} (ms)", f"=PERCENTILE({L},{p / 100})", q(lat, p), "0.0")
    mx = b.row("Maximum (ms)", f"=MAX({L})", float(lat.max()), "0.0")
    b.row("Mean / median", f"={b.local(mean)}/{b.local(ladder[50])}", float(lat.mean() / q(lat, 50)), "0.00",
          "Right-skewed data: mean > median")

    b.section("2. Service level objective")
    slo = b.row("SLO threshold (ms)", SLO_MS, None, "0", "Edit me", is_input=True)
    share = b.row("Share of requests slower than SLO", f'=COUNTIF({L},">"&{b.local(slo)})/COUNT({L})',
                  float((lat > SLO_MS).mean()), "0.00%")
    b.row("Requests slower than SLO", f'=COUNTIF({L},">"&{b.local(slo)})', int((lat > SLO_MS).sum()), "0")
    b.row("Is P95 within the SLO?", f'=IF({ladder[95].split("!")[1]}<={b.local(slo)},"yes","no")', None)
    b.row("Mean latency within the SLO?", f'=IF({b.local(mean)}<={b.local(slo)},"yes","no")', None)

    b.section("3. Percentiles by endpoint (the average hid the problem)")
    rows, exp = [], {}
    for i, e in enumerate(["search", "checkout", "profile"]):
        c = b.col(f"lat_{e}")
        rng_e = f"Data!${c}$2:${c}${b.n + 1}"
        x = lat[df["endpoint"] == e]
        rows.append([e, f"=COUNT({rng_e})", f"=AVERAGE({rng_e})", f"=PERCENTILE({rng_e},0.5)",
                     f"=PERCENTILE({rng_e},0.95)", f"=PERCENTILE({rng_e},0.99)"])
        exp.update({(i, 1): len(x), (i, 2): x.mean(), (i, 3): q(x, 50), (i, 4): q(x, 95), (i, 5): q(x, 99)})
    t0, t1 = b.table(["Endpoint", "n", "Mean", "P50", "P95", "P99"], rows,
                     fmt={2: "0.0", 3: "0.0", 4: "0.0", 5: "0.0"}, expect=exp)
    ep_rows = (t0, t1)

    b.section("4. Percentiles per 5-minute window (50 requests each)")
    rows, exp = [], {}
    win_stats = []
    for k in range(len(df) // WINDOW):
        a, z = 2 + k * WINDOW, 1 + (k + 1) * WINDOW
        x = lat[k * WINDOW:(k + 1) * WINDOW]
        rng_w = f"Data!$C${a}:$C${z}"
        rows.append([f"=Data!A{a}", f"=AVERAGE({rng_w})", f"=PERCENTILE({rng_w},0.5)",
                     f"=PERCENTILE({rng_w},0.95)", f"=PERCENTILE({rng_w},0.99)"])
        exp.update({(k, 1): x.mean(), (k, 2): q(x, 50), (k, 3): q(x, 95), (k, 4): q(x, 99)})
        win_stats.append((df["timestamp"].iloc[k * WINDOW], x.mean(), q(x, 50), q(x, 95), q(x, 99)))
    w0, w1 = b.table(["Window start", "Mean", "P50", "P95", "P99"], rows,
                     fmt={0: "hh:mm", 1: "0.0", 2: "0.0", 3: "0.0", 4: "0.0"}, expect=exp)
    b.line_chart_from_table("Mean vs tail latency per window (ms)", 1, [2, 4, 5], w0, w1, anchor="H4",
                            y_title="ms")

    worst = int(np.argmax([s[3] for s in win_stats]))
    b.answers([
        ("Mean latency (ms)", f"={mean}", f"The average is {lat.mean():.0f} ms - comfortably under a {SLO_MS} ms SLO."),
        ("P50 / P95 / P99 (ms)", f"={ladder[95]}",
         f"P50 = {q(lat, 50):.0f}, P95 = {q(lat, 95):.0f}, P99 = {q(lat, 99):.0f}. The P95 shown here passes, but P99 is "
         f"{q(lat, 99) / q(lat, 50):.0f}x the median: the tail is where the pain is."),
        (f"Share of requests slower than {SLO_MS} ms", f"={share}",
         f"{(lat > SLO_MS).mean():.1%} of requests ({int((lat > SLO_MS).sum())} of {len(lat)}) break the SLO even though the mean passes."),
        ("Which endpoint violates the SLO at P95?", f"=Analysis!E{ep_rows[0] + 1}",
         f"checkout: P95 = {q(lat[df.endpoint == 'checkout'], 95):.0f} ms vs search {q(lat[df.endpoint == 'search'], 95):.0f} ms and "
         f"profile {q(lat[df.endpoint == 'profile'], 95):.0f} ms. A pooled percentile cannot tell you this."),
        ("Which 5-minute window has the worst P95?", f"=Analysis!D{w0 + worst}",
         f"Window starting {win_stats[worst][0]:%H:%M} (P95 = {win_stats[worst][3]:.0f} ms, mean only {win_stats[worst][1]:.0f} ms)."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-03-percentiles", "03 · Percentiles and extreme values",
             "Why the mean is not enough: percentile ladder, SLO exceedance and per-window tail latency "
             "(values computed from data.csv).", df.rename(columns={"timestamp": "time"}), "time")
    d.stat("Percentile ladder (ms)", {"mean": lat.mean(), "P50": q(lat, 50), "P90": q(lat, 90), "P95": q(lat, 95),
                                      "P99": q(lat, 99), "max": lat.max()},
           "All 600 requests pooled. The mean looks healthy; P99 does not.", unit="ms", decimals=0,
           thresholds=[(None, "green"), (SLO_MS, "red")])
    raw = df[["timestamp", "latency_ms"]].rename(columns={"timestamp": "time"}).copy()
    raw["slo_ms"] = SLO_MS
    d.timeseries("Raw request latency vs SLO", raw, "Each dot is one request.", points=["latency_ms"],
                 dashed=["slo_ms"], unit="ms", colors={"slo_ms": "#E15759"})
    wdf = pd.DataFrame(win_stats, columns=["time", "mean", "P50", "P95", "P99"])
    wdf["slo_ms"] = SLO_MS
    d.timeseries("Mean vs tail per 5-minute window", wdf, "The mean barely moves while P99 explodes.",
                 dashed=["slo_ms"], unit="ms", colors={"slo_ms": "#E15759"})
    edf = pd.DataFrame([[e, np.percentile(lat[df.endpoint == e], 50), np.percentile(lat[df.endpoint == e], 95),
                         np.percentile(lat[df.endpoint == e], 99)] for e in ["search", "checkout", "profile"]],
                       columns=["endpoint", "P50", "P95", "P99"])
    d.bars("Percentiles by endpoint (ms)", edf, "Pooling hides that one endpoint is slow.", unit="ms")
    bins = np.arange(0, 1300, 50)
    cnt, _ = np.histogram(np.clip(lat, 0, 1249), bins=bins)
    d.bars("Latency histogram (50 ms buckets, last bucket = 1200+)", pd.DataFrame(
        {"bucket_ms": [f"{int(a)}-{int(a) + 50}" if a < 1200 else "1200+" for a in bins[:-1]], "requests": cnt}), "Long right tail.", w=12)
    d.save(out)

    # ------------------------------------------------------------------ markdown
    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK.format(slo=SLO_MS))
    return b


THEORY = r"""
# Theory: percentiles and extreme values

## Why the mean is the wrong summary for latency

Response times, file sizes, incomes and queue lengths are **right-skewed**: most values are small and a few are very
large. The arithmetic mean is pulled towards those few large values, but it also *averages them away* when most users
are fast. Two systems with the same mean can deliver completely different experiences, so what matters is the **shape of
the distribution**, especially its tail.

## Definition

The **p-th percentile** $Q_p$ is a value such that a fraction $p/100$ of the observations are at or below it.
Equivalently, $Q_p = F^{-1}(p/100)$ where $F$ is the empirical distribution function.

- $P50$ is the **median**: half of the requests are faster.
- $P95$ is the value that 95 % of requests do not exceed; 1 in 20 requests is slower.
- $P99$, $P99.9$ describe the **tail**: what your unluckiest users see.

Do not confuse the two directions: $P95 = 230\,\text{ms}$ does **not** mean "95 % of requests exceed the SLO"; it means
5 % of requests take longer than 230 ms.

## Computing a sample percentile

Sort the $n$ observations $x_{(1)} \le \dots \le x_{(n)}$. The common "linear interpolation" definition (used by
Excel/Sheets `PERCENTILE`, `numpy.percentile`) places $x_{(k)}$ at position $(k-1)/(n-1)$ and interpolates:

$$
h = (n-1)\,p + 1,\qquad
Q_p = x_{(\lfloor h \rfloor)} + (h - \lfloor h \rfloor)\,\bigl(x_{(\lfloor h \rfloor + 1)} - x_{(\lfloor h \rfloor)}\bigr).
$$

Worked example with $n = 5$ values $\{12, 15, 20, 40, 200\}$ and $p = 0.9$: $h = 4 \cdot 0.9 + 1 = 4.6$, so
$Q_{0.9} = x_{(4)} + 0.6\,(x_{(5)} - x_{(4)}) = 40 + 0.6 \cdot 160 = 136$. Other textbooks use slightly different
interpolation rules, so small samples can give slightly different answers in different tools.

## Exceedance and SLOs

A **service-level objective** is a statement about a percentile or a proportion, for example "P95 latency below 250 ms"
or equivalently "at most 5 % of requests slower than 250 ms". The **exceedance share** for a threshold $c$ is

$$
\hat{\pi}(c) = \frac{\#\{x_i > c\}}{n}.
$$

Percentile and exceedance are two views of the same curve: $P95 \le c \iff \hat\pi(c) \le 5\%$.

## The tail needs enough data

An extreme percentile is determined by very few points. With $n = 600$ requests, $P99$ is decided by the 6 slowest
requests, and $P99.9$ by less than one. The standard error of a sample percentile grows quickly in the tail and with
heavy-tailed data, so:

- do not report $P99.9$ from a few hundred samples;
- compare tail percentiles over windows long enough to contain many tail events;
- use the bootstrap (lesson 17) to attach a confidence interval to a percentile.

## Percentiles do not average

You **cannot** compute the P95 of a day by averaging the P95 of each hour (or each server). Percentiles are not linear:
the P95 of a union depends on the whole distributions, not on their P95s. Either keep raw values, or store histograms and
merge the histograms.

This is also why Prometheus `histogram_quantile` is an *estimate*: it interpolates linearly inside a bucket, so its
accuracy is limited by the bucket boundaries. Pick buckets around your SLO threshold.

## Assumptions and pitfalls

1. **Pooling hides segments.** A healthy endpoint can mask a broken one in the pooled percentile; always slice by
   endpoint, region, customer tier.
2. **Aggregation window matters.** A one-minute P99 and a one-day P99 answer different questions.
3. **Coordinated omission.** If you only measure requests that completed, timeouts vanish from your percentiles.
4. **Mean versus percentile of means.** Averaging first and taking percentiles later (or the reverse) are different
   statistics.

## Related notes

- [Distribution shape and skewness](../01-distribution-shapes-and-heavy-tails/theory.md)
- [Robust statistics](../02-robust-statistics/theory.md)
- [Bootstrapping confidence intervals](../17-bootstrapping-and-confidence-intervals/theory.md)
"""

TASK = r"""
# Task: percentiles and extreme values

## Scenario

You run the on-call rotation for an e-commerce API. The dashboards show an average latency of "about 115 ms" and the
team believes the service meets its objective: **P95 latency below {slo} ms**. Support keeps getting complaints about slow
checkouts. Your job is to find out whether the average is hiding a problem.

## Data

`data.csv` - 600 requests, one every 5 seconds (09:00:00 - 09:49:55).

| column | meaning |
|---|---|
| `timestamp` | when the request arrived |
| `endpoint` | `search`, `checkout` or `profile` |
| `latency_ms` | server response time in milliseconds |
| `status` | HTTP status code |

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute the **mean** latency. Does it meet a {slo} ms objective?
2. Compute **P50, P90, P95, P99** and the maximum. How many times larger is P99 than the median?
3. What share of requests is slower than {slo} ms? How many requests is that?
4. Compute count, mean, P50, P95 and P99 **per endpoint**. Which endpoint violates the objective?
5. Split the data into windows of 50 consecutive requests (5 minutes each) and compute mean, P95 and P99 per window.
   In which window does the tail explode? What happens to the mean in the same window?
6. Change the threshold to 150 ms. How does the exceedance share change, and what does that say about choosing
   an SLO from the average?
7. *Explain in two sentences* why you cannot average the 12 window P95 values to obtain the P95 of the whole run.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- Find the degraded period on the "Raw request latency vs SLO" panel. Which time range is it?
- Compare "Mean vs tail per 5-minute window" with your table from question 5.
- Which endpoint's bar breaks the SLO line in "Percentiles by endpoint"?

## Deliverable

A short note (5-8 lines) answering: *Is the service meeting its SLO, for whom is it failing, and since when?*
Include one chart and state one limitation of using 600 requests to estimate P99.
"""
