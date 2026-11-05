"""Lesson 06 - Time aggregation and sampling frequency."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import HEADER_FILL, HEADER_FONT, Book, Dash, md, write_csv  # noqa: E402

SLUG = "06-time-aggregation-and-sampling-frequency"
TITLE = "Time aggregation and sampling frequency"
MODULE = "Understanding time series"
DATASET = "14 days of 15-minute web-service metrics (requests, errors, mean latency, CPU gauge)"
DAYS, PER_DAY, PER_HOUR = 14, 96, 4
CPU_LIMIT = 80
INCIDENT_DAY, INCIDENT_FIRST = 8, 56  # day index; first of four 15-minute slots (14:00-14:45)


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(606)
    n = DAYS * PER_DAY
    t = pd.date_range("2026-02-02 00:00:00", periods=n, freq="15min")  # Monday 00:00
    h = (np.arange(n) % PER_DAY) / PER_HOUR
    dow = (np.arange(n) // PER_DAY) % 7
    shape = 0.8 * np.exp(-(((h - 13) / 3.5) ** 2)) + 0.6 * np.exp(-(((h - 20.5) / 2.5) ** 2))
    lam = (60 + 1900 * shape) * np.where(dow >= 5, 0.7, 1.0) * rng.normal(1, 0.06, n)
    req = rng.poisson(lam)
    p = 0.006 + 0.04 * np.exp(-lam / 80)  # low-traffic hours: few requests, many of them failing bots/retries
    inc = np.zeros(n, bool)
    inc[INCIDENT_DAY * PER_DAY + INCIDENT_FIRST: INCIDENT_DAY * PER_DAY + INCIDENT_FIRST + 4] = True
    p = np.where(inc, 0.30, p)
    err = rng.binomial(req, p)
    lat = 100 + 0.04 * lam + rng.normal(0, 4, n) + np.where(inc, 150, 0)
    cpu = 20 + 0.012 * lam + rng.normal(0, 2, n)
    job = (np.arange(n) % PER_HOUR) == 1  # an hourly batch job runs :10-:25, so only the :15 sample catches it
    cpu = np.where(job, cpu + 50, cpu)
    return pd.DataFrame({"timestamp": t, "requests": req, "errors": err, "mean_latency_ms": lat.round(1),
                         "cpu_pct": np.clip(cpu, 0, 100).round(1)})


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    n = len(df)
    req, err = df["requests"].to_numpy(), df["errors"].to_numpy()
    lat, cpu = df["mean_latency_ms"].to_numpy(), df["cpu_pct"].to_numpy()
    rate = err / req
    pos = np.arange(n) % PER_HOUR

    b = Book(df, "Lesson 06 - Time aggregation and sampling frequency",
             "Solved workbook. Yellow cells are assumptions you can change; everything else is a live formula.")
    loc = b.local
    cr, ce, cl, cc = b.col("requests"), b.col("errors"), b.col("mean_latency_ms"), b.col("cpu_pct")
    b.add_column("error_rate", lambda r: f"=Data!{ce}{r}/Data!{cr}{r}", expected=rate, fmt="0.0000")
    b.add_column("latency_x_requests", lambda r: f"=Data!{cr}{r}*Data!{cl}{r}", expected=req * lat, fmt="0.0")
    b.add_column("minute_in_hour", lambda r: f"=MOD(ROW()-2,4)*15", expected=pos * 15, fmt="0")
    cm = b.col("minute_in_hour")
    cpu_on_hour = np.where(pos == 0, cpu, np.nan)
    b.add_column("cpu_on_hour", lambda r: f'=IF(Data!{cm}{r}=0,Data!{cc}{r},"")', expected=cpu_on_hour, fmt="0.0")
    RQ, ER, LAT, CPU, RT, LXR = (b.rng(c) for c in ["requests", "errors", "mean_latency_ms", "cpu_pct", "error_rate", "latency_x_requests"])
    MIN, COH = b.rng("minute_in_hour"), b.rng("cpu_on_hour")

    # ----------------------------------------------------------- Hourly sheet (336 rows)
    hs = b.wb.create_sheet("Hourly", 2)
    heads = ["hour_start", "requests", "errors", "error_rate", "cpu_mean", "cpu_max", "cpu_at_hour_start"]
    for j, hname in enumerate(heads, start=1):
        c = hs.cell(row=1, column=j, value=hname)
        c.fill, c.font = HEADER_FILL, HEADER_FONT
        hs.column_dimensions[get_column_letter(j)].width = 18
    nh = n // PER_HOUR
    hreq, herr = req.reshape(nh, 4).sum(1), err.reshape(nh, 4).sum(1)
    hcpu = cpu.reshape(nh, 4)
    for i in range(nh):
        a, z, r = 2 + PER_HOUR * i, 1 + PER_HOUR * (i + 1), i + 2
        hs.cell(row=r, column=1, value=f"=Data!A{a}").number_format = "yyyy-mm-dd hh:mm"
        hs.cell(row=r, column=2, value=f"=SUM(Data!{cr}{a}:{cr}{z})")
        hs.cell(row=r, column=3, value=f"=SUM(Data!{ce}{a}:{ce}{z})")
        hs.cell(row=r, column=4, value=f"=C{r}/B{r}").number_format = "0.0000"
        hs.cell(row=r, column=5, value=f"=AVERAGE(Data!{cc}{a}:{cc}{z})").number_format = "0.0"
        hs.cell(row=r, column=6, value=f"=MAX(Data!{cc}{a}:{cc}{z})").number_format = "0.0"
        hs.cell(row=r, column=7, value=f"=Data!{cc}{a}").number_format = "0.0"
        for col, v in zip("BCDEFG", [hreq[i], herr[i], herr[i] / hreq[i], hcpu[i].mean(), hcpu[i].max(), hcpu[i][0]]):
            b.checks.append((f"Hourly!{col}{r}", f"hourly {col} row {r}", float(v)))
    hs.freeze_panes = "A2"
    HR = lambda col: f"Hourly!${col}$2:${col}${nh + 1}"
    herate = herr / hreq

    # ----------------------------------------------------------- 1 whole period
    b.section("1. The whole period: totals and the two ways to average a rate")
    treq = b.row("Total requests", f"=SUM({RQ})", int(req.sum()), "#,##0")
    terr = b.row("Total errors", f"=SUM({ER})", int(err.sum()), "#,##0")
    pooled = b.row("Error rate, pooled (total errors / total requests)", f"={loc(terr)}/{loc(treq)}", err.sum() / req.sum(), "0.000%")
    mean_rate = b.row("Error rate, mean of the 1,344 interval rates", f"=AVERAGE({RT})", float(rate.mean()), "0.000%",
                      "gives a quiet 03:00 slot the same weight as a busy noon")
    b.row("Overstatement by averaging rates (ratio)", f"={loc(mean_rate)}/{loc(pooled)}", float(rate.mean() / (err.sum() / req.sum())), "0.00")
    wlat = b.row("Latency, request-weighted mean (ms)", f"=SUM({LXR})/{loc(treq)}", float((req * lat).sum() / req.sum()), "0.0")
    ulat = b.row("Latency, plain mean of the interval means (ms)", f"=AVERAGE({LAT})", float(lat.mean()), "0.0")
    b.row("Difference weighted - plain (ms)", f"={loc(wlat)}-{loc(ulat)}", float((req * lat).sum() / req.sum() - lat.mean()), "0.0")

    # ----------------------------------------------------------- 2 daily
    b.section("2. Daily aggregation (96 slots per day)")
    rows, exp = [], {}
    r0 = b.next_row + 1
    days = []
    for i in range(DAYS):
        a, z = 2 + PER_DAY * i, 1 + PER_DAY * (i + 1)
        r = r0 + i
        sl = slice(PER_DAY * i, PER_DAY * (i + 1))
        d_req, d_err = int(req[sl].sum()), int(err[sl].sum())
        rows.append([f"=Data!A{a}", f"=SUM(Data!{cr}{a}:{cr}{z})", f"=SUM(Data!{ce}{a}:{ce}{z})", f"=C{r}/B{r}",
                     f"=AVERAGE(Data!{b.col('error_rate')}{a}:{b.col('error_rate')}{z})",
                     f"=SUM(Data!{b.col('latency_x_requests')}{a}:{b.col('latency_x_requests')}{z})/B{r}",
                     f"=AVERAGE(Data!{cl}{a}:{cl}{z})", f"=MAX(Data!{cc}{a}:{cc}{z})", f"=AVERAGE(Data!{cc}{a}:{cc}{z})",
                     f"=MAX(Data!{cr}{a}:{cr}{z})"])
        vals = [d_req, d_err, d_err / d_req, rate[sl].mean(), (req[sl] * lat[sl]).sum() / d_req, lat[sl].mean(), cpu[sl].max(),
                cpu[sl].mean(), req[sl].max()]
        days.append(dict(date=pd.Timestamp("2026-02-02") + pd.Timedelta(days=i), req=d_req, err=d_err, rate=d_err / d_req,
                         mrate=rate[sl].mean(), wlat=vals[4], ulat=vals[5], cmax=vals[6], cmean=vals[7], rpeak=vals[8]))
    exp = {}
    for i, dday in enumerate(days):
        for j, key in enumerate(["req", "err", "rate", "mrate", "wlat", "ulat", "cmax", "cmean", "rpeak"], start=1):
            exp[(i, j)] = dday[key]
    t0, t1 = b.table(["date", "requests", "errors", "error rate (pooled)", "mean of 15-min rates", "latency (weighted)",
                      "latency (plain mean)", "peak CPU", "mean CPU", "peak 15-min requests"], rows,
                     fmt={0: "yyyy-mm-dd", 1: "#,##0", 2: "#,##0", 3: "0.00%", 4: "0.00%", 5: "0.0", 6: "0.0", 7: "0.0", 8: "0.0", 9: "#,##0"},
                     expect=exp)
    b.line_chart_from_table("Daily error rate: pooled vs mean of interval rates", 1, [4, 5], t0, t1, anchor="L4", y_title="rate")
    worst = int(np.argmax([x["rate"] for x in days]))
    med_rate = float(np.median([x["rate"] for x in days]))
    wd = b.row("Highest daily pooled error rate", f"=MAX(D{t0}:D{t1})", days[worst]["rate"], "0.00%")
    b.row("... divided by the median daily rate", f"={loc(wd)}/MEDIAN(D{t0}:D{t1})", days[worst]["rate"] / med_rate, "0.00")
    pk = b.row("Peak-to-average requests per 15 min (whole period)", f"=MAX({RQ})/AVERAGE({RQ})", float(req.max() / req.mean()), "0.00",
               "capacity must cover the peak, not the daily average")

    # ----------------------------------------------------------- 3 weekly
    b.section("3. Weekly aggregation")
    rows, exp = [], {}
    r0 = b.next_row + 1
    weeks = []
    for w in range(2):
        a, z = t0 + 7 * w, t0 + 7 * w + 6
        sl = slice(7 * PER_DAY * w, 7 * PER_DAY * (w + 1))
        dd = days[7 * w: 7 * w + 7]
        rows.append([f"Week {w + 1}", f"=SUM(B{a}:B{z})", f"=SUM(C{a}:C{z})", f"=C{r0 + w}/B{r0 + w}", f"=AVERAGE(D{a}:D{z})",
                     f"=MAX(D{a}:D{z})"])
        vals = dict(req=sum(x["req"] for x in dd), err=sum(x["err"] for x in dd))
        vals["rate"] = vals["err"] / vals["req"]
        vals["avgdaily"] = float(np.mean([x["rate"] for x in dd]))
        vals["maxdaily"] = max(x["rate"] for x in dd)
        weeks.append(vals)
        exp.update({(w, 1): vals["req"], (w, 2): vals["err"], (w, 3): vals["rate"], (w, 4): vals["avgdaily"], (w, 5): vals["maxdaily"]})
    w0, w1 = b.table(["week", "requests", "errors", "error rate (pooled)", "average of the 7 daily rates", "worst day"], rows,
                     fmt={1: "#,##0", 2: "#,##0", 3: "0.000%", 4: "0.000%", 5: "0.000%"}, expect=exp)

    # ----------------------------------------------------------- 4 resolution
    b.section("4. What does coarser aggregation hide?  Worst error rate at each resolution")
    mx = {"15 minutes": float(rate.max()), "1 hour": float(herate.max()), "1 day": max(x["rate"] for x in days),
          "1 week": max(w["rate"] for w in weeks)}
    rows = [["15 minutes", f"=MAX({RT})"], ["1 hour", f"=MAX({HR('D')})"], ["1 day", f"=MAX(D{t0}:D{t1})"], ["1 week", f"=MAX(D{w0}:D{w1})"]]
    exp = {(i, 1): v for i, v in enumerate(mx.values())}
    q0, q1 = b.table(["resolution", "worst error rate"], rows, fmt={1: "0.0%"}, expect=exp)
    b.bar_chart_from_table("Worst error rate by aggregation level", 1, [2], q0, q1, anchor="L24", y_title="error rate")

    # ----------------------------------------------------------- 5 sampling / aliasing
    b.section("5. Sampling frequency: what a CPU gauge shows depends on WHEN you look")
    lim = b.row("CPU alert limit (%)", CPU_LIMIT, None, "0", "Edit me", is_input=True)
    m15 = b.row("Mean CPU, all 15-minute samples", f"=AVERAGE({CPU})", float(cpu.mean()), "0.0")
    p15 = b.row("Peak CPU, all 15-minute samples", f"=MAX({CPU})", float(cpu.max()), "0.0")
    mh = b.row("Mean CPU, only the sample at the top of the hour (hourly sampling)", f"=AVERAGE({COH})", float(np.nanmean(cpu_on_hour)), "0.0")
    ph = b.row("Peak CPU, only the sample at the top of the hour", f"=MAX({COH})", float(np.nanmax(cpu_on_hour)), "0.0")
    n15 = b.row("15-minute samples at or above the limit", f"=COUNTIF({CPU},\">=\"&{loc(lim)})", int((cpu >= CPU_LIMIT).sum()), "0")
    nh_ = b.row("Top-of-hour samples at or above the limit", f"=COUNTIF({COH},\">=\"&{loc(lim)})", int((cpu_on_hour[~np.isnan(cpu_on_hour)] >= CPU_LIMIT).sum()), "0")
    nhh = b.row("Hours in which the hourly MAX reaches the limit", f"=COUNTIF({HR('F')},\">=\"&{loc(lim)})", int((hcpu.max(1) >= CPU_LIMIT).sum()), "0",
                f"of {nh} hours")
    hmean_max = b.row("Highest hourly MEAN CPU", f"=MAX({HR('E')})", float(hcpu.mean(1).max()), "0.0", "averaging also hides the peak")
    rows, exp = [], {}
    r0 = b.next_row + 1
    for i, off in enumerate([0, 15, 30, 45]):
        r = r0 + i
        rows.append([off, f"=AVERAGEIF({MIN},A{r},{CPU})", f"=COUNTIFS({MIN},A{r},{CPU},\">=\"&{loc(lim)})"])
        exp[(i, 1)] = float(cpu[pos == i].mean())
        exp[(i, 2)] = int(((pos == i) & (cpu >= CPU_LIMIT)).sum())
    a0, a1 = b.table(["minute of the hour sampled", "mean CPU", "samples at or above the limit"], rows, fmt={1: "0.0", 2: "0"}, expect=exp)
    b.bar_chart_from_table("Mean CPU depends on the minute you sample", 1, [2], a0, a1, anchor="L44", x_title="minute", y_title="CPU %")
    phase = {off: float(cpu[pos == i].mean()) for i, off in enumerate([0, 15, 30, 45])}

    # ---------------------------------------------------------------- answers
    inc_hour = INCIDENT_DAY * 24 + INCIDENT_FIRST // 4
    inc_idx = INCIDENT_DAY * PER_DAY + INCIDENT_FIRST
    b.answers([
        ("Total requests and errors; error rate pooled vs mean of 15-minute rates", f"={pooled}",
         f"{int(req.sum()):,} requests, {int(err.sum()):,} errors: pooled rate {err.sum() / req.sum():.2%}. The mean of the 1,344 interval rates is {rate.mean():.2%} "
         f"({rate.mean() / (err.sum() / req.sum()):.1f}x higher) because quiet night slots, with a few requests and a high failure share, count as much as busy ones. "
         "Pooled is the rate a request experiences."),
        ("Mean latency: request-weighted vs plain mean of 15-minute means", f"={wlat}",
         f"Weighted {(req * lat).sum() / req.sum():.1f} ms vs plain {lat.mean():.1f} ms: latency rises with load, and the weighted mean gives busy slots their larger share of requests."),
        ("Daily table; which day is worst and by what factor above the median day?", f"={wd}",
         f"Worst day {days[worst]['date']:%d %b} (pooled error rate {days[worst]['rate']:.2%}) vs a median day of {med_rate:.2%}, i.e. {days[worst]['rate'] / med_rate:.1f}x. "
         f"Peak-to-average load is {req.max() / req.mean():.1f}."),
        ("Weekly pooled rate vs average of the daily rates", f"=Analysis!D{w0}",
         f"Week 1: {weeks[0]['rate']:.3%} pooled vs {weeks[0]['avgdaily']:.3%} average of daily rates; week 2: {weeks[1]['rate']:.3%} vs {weeks[1]['avgdaily']:.3%}. "
         "Averaging daily rates weights a quiet weekend day like a busy weekday."),
        ("Worst error rate at 15-minute, hourly, daily and weekly resolution", f"=Analysis!B{q0 + 1}",
         f"{mx['15 minutes']:.1%} at 15 minutes, {mx['1 hour']:.1%} per hour, {mx['1 day']:.1%} per day, {mx['1 week']:.1%} per week: a one-hour outage with a 30 % failure rate "
         "(day 9, 14:00) is a 3 % blip on the daily chart and invisible on the weekly one."),
        ("CPU: all samples vs only the top-of-hour sample; samples above the limit", f"={ph}",
         f"All samples: mean {cpu.mean():.1f}, peak {cpu.max():.1f}, {int((cpu >= CPU_LIMIT).sum())} samples >= {CPU_LIMIT}. Top-of-hour only: mean {np.nanmean(cpu_on_hour):.1f}, "
         f"peak {np.nanmax(cpu_on_hour):.1f}, {int((cpu_on_hour[~np.isnan(cpu_on_hour)] >= CPU_LIMIT).sum())} samples >= {CPU_LIMIT}. Hourly sampling concludes 'plenty of headroom'; "
         f"the hourly MAX reaches {CPU_LIMIT} in {int((hcpu.max(1) >= CPU_LIMIT).sum())} hours. Even the hourly MEAN tops out at {hcpu.mean(1).max():.1f}."),
        ("Mean CPU by sampled minute (0, 15, 30, 45)", f"=Analysis!B{a0 + 1}",
         f"Minute 0: {phase[0]:.1f}, minute 15: {phase[15]:.1f}, minute 30: {phase[30]:.1f}, minute 45: {phase[45]:.1f}. A hidden periodic job (a spike of about 15 minutes every hour) "
         "is seen at one phase and missed at the others: aliasing. To see a 15-minute event you must sample at least every 7.5 minutes (Nyquist), and in practice faster."),
        ("Which aggregate for which metric? (sum / mean / max)", "see text",
         "Requests and errors are counters: sum them (and derive rates from the sums). Latency is a mean per slot: weight by requests. CPU is a gauge: use mean for cost, max "
         "(or a high percentile of fine-grained samples) for capacity. Never average rates, percentiles or means of different sample sizes without weights. Limitation: only 14 days, "
         "one incident and one batch schedule; weekly patterns cannot be separated from these single events."),
    ])

    # ---------------------------------------------------------------- grafana
    d = Dash("stats-06-time-aggregation", "06 · Time aggregation and sampling frequency",
             "The same 14 days at 15-minute, hourly, daily and weekly resolution: what each aggregation hides "
             "(values computed from data.csv).", df.rename(columns={"timestamp": "time"}), "time")
    d.stat("Aggregation choices change the answer",
           {"error rate pooled (%)": 100 * err.sum() / req.sum(), "error rate, mean of 15-min rates (%)": 100 * rate.mean(),
            "latency weighted (ms)": (req * lat).sum() / req.sum(), "latency plain mean (ms)": lat.mean(),
            "peak CPU, all samples (%)": cpu.max(), "peak CPU, hourly samples (%)": np.nanmax(cpu_on_hour)},
           "Left of each pair: the correct aggregate; right: the naive one.", decimals=2, thresholds=[(None, "blue")])
    hours = pd.date_range(df["timestamp"].iloc[0], periods=nh, freq="h")
    drate = np.repeat([x["rate"] for x in days], 24)
    hdf = pd.DataFrame({"time": hours, "hourly error rate (%)": 100 * herate, "daily pooled error rate (%)": 100 * drate})
    d.timeseries("Error rate: hourly vs daily aggregation (%)", hdf,
                 "The hourly series shows a one-hour burst at about 30 %; the daily average (dashed) turns it into a small bump.",
                 dashed=["daily pooled error rate (%)"], unit="percent", colors={"hourly error rate (%)": "#E15759", "daily pooled error rate (%)": "#4E79A7"})
    cdf = pd.DataFrame({"time": hours, "CPU hourly max (15-min samples)": hcpu.max(1), "CPU hourly mean": hcpu.mean(1),
                        "CPU hourly snapshot (sample at :00)": hcpu[:, 0], "alert limit": CPU_LIMIT})
    d.timeseries("CPU: what each way of reducing the data shows (%)", cdf,
                 "The hourly snapshot never reaches the limit, the hourly mean neither, the hourly max does at busy times.",
                 dashed=["alert limit"], unit="percent",
                 colors={"CPU hourly max (15-min samples)": "#E15759", "CPU hourly mean": "#59A14F",
                         "CPU hourly snapshot (sample at :00)": "#4E79A7", "alert limit": "#F28E2B"})
    rs = pd.DataFrame({"resolution": list(mx), "worst error rate (%)": [100 * v for v in mx.values()]}).round(2)
    d.bars("Worst error rate by aggregation level (%)", rs, "The incident shrinks from about 30 % to about 1 % as the window grows.", unit="percent")
    ph_ = pd.DataFrame({"minute sampled": [f":{o:02d}" for o in phase], "mean CPU (%)": list(phase.values())}).round(2)
    d.bars("Mean CPU by the minute of the hour that is sampled (%)", ph_,
           "Aliasing: the hourly job is visible only at :15; sampling at :00 gives a flat, low reading.", unit="percent")
    dl = pd.DataFrame({"time": [x["date"] for x in days], "latency weighted by requests (ms)": np.round([x["wlat"] for x in days], 2),
                       "plain mean of 15-min means (ms)": np.round([x["ulat"] for x in days], 2)})
    d.timeseries("Daily mean latency: weighted vs plain (ms)", dl,
                 "The weighted mean is higher every day: busy slots are slower and carry most of the requests. Both peak on the incident day.", unit="ms",
                 colors={"latency weighted by requests (ms)": "#4E79A7", "plain mean of 15-min means (ms)": "#F28E2B"})
    d.save(out)

    md(out / "theory.md", fill(THEORY, theory_values(df, days, mx, phase)))
    md(out / "task.md", TASK.replace("<<limit>>", str(CPU_LIMIT)))
    return b


def fill(text: str, vals: dict) -> str:
    for k, v in vals.items():
        text = text.replace(f"<<{k}>>", str(v))
    return text


def theory_values(df, days, mx, phase) -> dict:
    # worked example 1: ratio of sums vs mean of ratios
    night, day = (50, 5), (950, 10)
    mean_rate = (night[1] / night[0] + day[1] / day[0]) / 2
    pooled = (night[1] + day[1]) / (night[0] + day[0])
    lat_n, lat_d = 90.0, 160.0
    wl = (night[0] * lat_n + day[0] * lat_d) / (night[0] + day[0])
    # example 2: aliasing
    f, fs = 1 / 60, 1 / 45
    return {
        "e_night": f"{night[1] / night[0]:.1%}", "e_day": f"{day[1] / day[0]:.2%}", "e_mean": f"{mean_rate:.2%}", "e_pooled": f"{pooled:.2%}",
        "e_ratio": f"{mean_rate / pooled:.1f}", "e_wl": f"{wl:.1f}", "e_ul": f"{(lat_n + lat_d) / 2:.1f}",
        "alias_period": f"{1 / abs(fs - f):.0f}",
        "mx15": f"{mx['15 minutes']:.0%}", "mxh": f"{mx['1 hour']:.1%}", "mxd": f"{mx['1 day']:.1%}", "mxw": f"{mx['1 week']:.1%}",
        "ph0": f"{phase[0]:.1f}", "ph15": f"{phase[15]:.1f}",
    }


THEORY = r"""
# Theory: time aggregation and sampling frequency

## Why the window and the aggregate function are part of the result

Raw monitoring data is almost never read raw: a dashboard shows one point per minute, a report one per day, a capacity review one per week. Each step reduces many values
to one, and **what you keep depends on the function (sum, mean, max, weighted mean) and on the window**. Choose badly and the burst that took the checkout down for an hour
disappears into a daily average, or a nightly batch job that saturates the CPU is never seen because the gauge is read only on the hour. Two separate questions are involved:

1. **Aggregation**: given fine-grained data, how do I combine it into coarser buckets correctly?
2. **Sampling**: given that data is only observed every $\Delta$ time units, which phenomena are visible at all?

## Pick the aggregate by what the metric *is*

| metric type | example | right daily aggregate | wrong one |
|---|---|---|---|
| **counter / amount** (additive) | requests, errors, revenue | sum | mean of the per-slot values times a different number of slots |
| **rate / ratio** | error rate, conversion rate | ratio of sums $\sum \text{errors}/\sum \text{requests}$ | mean of the per-slot ratios |
| **mean per slot** | mean latency per 15 min | weighted mean $\sum n_i\bar x_i/\sum n_i$ (weights = request counts) | unweighted mean of the $\bar x_i$ |
| **gauge** (level at an instant) | CPU %, queue length, temperature | mean for cost/typical level, **max** (or high percentile) for capacity and alarms, last for state | the value at one fixed instant |
| **percentile** | P95 latency | recompute from raw values or merge histograms | mean of per-slot P95 ([percentiles do not average](../03-percentiles-and-extreme-values/theory.md)) |

For a ratio with numerator $a_i$ and denominator $b_i$ in slot $i$ the correct aggregate is $\sum a_i / \sum b_i$, a *weighted* mean of the slot ratios $a_i/b_i$ with weights $b_i$.
The unweighted mean is a different statistic that over-represents low-traffic slots. This is the same mechanism as [Simpson's paradox](../05-sampling-bias-and-simpson-s-paradox/theory.md).

### Worked example

A night slot has 50 requests and 5 errors (<<e_night>>); a day slot has 950 requests and 10 errors (<<e_day>>). The mean of the two slot rates is <<e_mean>>, the pooled rate is
$15/1000=<<e_pooled>>$: the naive average is <<e_ratio>> times too high. The same two slots with mean latency 90 ms (night) and 160 ms (day) give a weighted mean of <<e_wl>> ms
(the typical request saw a loaded system) against an unweighted <<e_ul>> ms. In the data of this lesson, the pooled error rate and the mean of the interval rates differ in
exactly this way.

## Aggregation hides short events

A bucket average dilutes an event by the ratio of event duration to bucket length. In the dataset a one-hour outage has a 30 % failure rate at the worst 15-minute slots. The worst
error rate seen at each resolution is: 15 min <<mx15>>, 1 hour <<mxh>>, 1 day <<mxd>>, 1 week <<mxw>>. Alert on short windows (or on max / high percentiles), and report long windows for trend.
Averaging is a low-pass filter: it keeps the slow component (trend, seasonality) and removes the fast component (bursts). Useful for planning, dangerous for detection.

Related practical points: time zones and daylight-saving changes (a "day" can have 23 or 25 hours); partial buckets at the ends of the data; missing data (`AVERAGE` over what exists
versus `SUM` that silently undercounts); and week alignment (ISO week starts Monday).

## Sampling frequency and aliasing

A gauge sampled every $\Delta$ (sampling frequency $f_s=1/\Delta$) can represent only fluctuations slower than the **Nyquist frequency** $f_s/2$. A periodic component of frequency
$f > f_s/2$ is not lost: it is **aliased** to the apparent frequency

$$
f_\text{alias} = \left| f - k f_s \right|,\quad k = \text{the integer nearest to } f/f_s.
$$

Example: a process with a 60-minute cycle ($f=1/60$ per min) read every 45 minutes ($f_s=1/45$) appears to have $|1/60-1/45|=1/180$ per minute, a **<<alias_period>>-minute cycle that does not exist**.
If it is read exactly once per cycle ($f_s=f$) the alias frequency is 0: it shows as a constant whose level depends on the phase of the reading.

That is what the CPU gauge in the data does. An hourly batch job runs about 15 minutes after the full hour. Reading the gauge on the hour never catches it (mean CPU <<ph0>> %), reading it at :15 always does
(<<ph15>> %). Both are "correct" samples and both are misleading. For a short event of duration $T$ sample at least every $T/2$, store a **max** over each window next to the mean when you
downsample, or use event counters and histograms that accumulate between scrapes (the reason Prometheus counters and histograms survive coarse scrape intervals much better than gauges).

Before aggregating or resampling, aggregate in the direction that **preserves information for the decision**: sums and counts for volume, max and percentiles for risk, ratios of sums for rates.

## Assumptions and pitfalls

1. **Averaging an average** is only valid with equal weights (equal bucket sizes and equal counts); otherwise weight by the denominator.
2. **Aggregating after the ratio** (mean of hourly error rates) answers "what is a typical hour?", not "what did a request experience?". Decide which question you are asking.
3. **A coarser window cannot be un-aggregated.** Keep raw (or fine-grained) data for as long as storage allows; downsample with several functions (sum, max, count), not just the mean.
4. **Retention policies bite:** a five-minute series that is rolled up to one hour after 30 days has lost every short incident older than a month.
5. **Aligned sampling can alias** (cron jobs, hourly scrapes); jittering the scrape time or sampling faster reveals it.
6. **Bucket boundaries matter**: a burst across 14:55-15:05 is split between two hourly buckets and looks half as bad in each.
7. **Different windows, different statistics**: do not compare a daily mean with an hourly mean without saying so.

## Related notes

- [Percentiles and extreme values](../03-percentiles-and-extreme-values/theory.md)
- [Trend, seasonality and noise](../07-trend-seasonality-and-noise/theory.md) and [rolling statistics](../10-rolling-statistics/theory.md)
- [Seasonality and trends](../../notes/time_series/seasonality_and_trends.md) and [frequency-domain analysis](../../notes/time_series/frequency_domain_analysis.md)
- [Statistical process control](../26-statistical-process-control/theory.md)
"""

TASK = r"""
# Task: time aggregation and sampling frequency

## Scenario

You maintain the metrics for a web shop. The management report is built from **daily** numbers and the capacity plan from **hourly CPU readings**. Two
sentences from last week's review make you suspicious: "the error rate is a steady 1 %, so nothing happened on any day" and "the servers never exceed 50 % CPU at the top
of the hour, so we can cut the instance count." You have the full 15-minute metrics for 14 days and must check what the coarser views hide, and which aggregation is correct for each metric.

## Data

`data.csv` - 1,344 rows, one per 15-minute slot, 2 Feb 2026 00:00 (Monday) to 15 Feb 2026 23:45.

| column | meaning |
|---|---|
| `timestamp` | start of the 15-minute slot |
| `requests` | requests served in the slot |
| `errors` | requests that returned an error in the slot |
| `mean_latency_ms` | mean response time in the slot (ms) |
| `cpu_pct` | CPU utilisation read at the start of the slot (%) - a gauge |

## Questions

Work in a spreadsheet (import `data.csv`; you will need `SUM`, `AVERAGE`, `MAX`, `SUMPRODUCT`, `COUNTIF` and blocks of 4 rows = 1 hour, 96 rows = 1 day), then compare with `solution.xlsx`.

1. Compute total requests and errors. Compute the error rate (a) as total errors / total requests and (b) as the average of the 1,344 interval error rates. Why do they differ?
2. Compute the mean latency (a) as the plain average of the 1,344 slot means and (b) weighted by `requests`. Which one describes the average request?
3. Aggregate to days: requests, errors, pooled error rate and the average of the interval rates. Which day is worst and how many times the median daily rate is it?
4. Aggregate to weeks. Compare each week's pooled error rate with the average of its seven daily rates.
5. Find the worst error rate at 15-minute, hourly, daily and weekly resolution. What does coarser aggregation do to the worst value, and what would an alert on daily data have shown?
6. Compute mean and peak CPU (a) from all 15-minute samples and (b) from only the sample at the top of each hour. How many samples reach <<limit>> % in each case? How many hours have a MAX of at least <<limit>> %?
7. Compute the mean CPU separately for the readings at minute 0, 15, 30 and 45 of the hour. What does the pattern tell you about the sampling interval of the CPU gauge?
8. *Explain in three sentences* which aggregate (sum, mean, weighted mean, ratio of sums, max) you would use for requests, error rate, latency and CPU in a capacity report, and one limitation of 14 days of data.

## Grafana

Import `grafana/dashboard.json` (no data-source setup is needed).

- In "Error rate: hourly vs daily aggregation", find the burst. When does it occur and how large is it on the hourly versus the daily line?
- In "CPU: what each way of reducing the data shows", which reduction would have triggered a <<limit>> % alert and which never would?
- In "Mean CPU by the minute of the hour that is sampled", which minute is special and why?

## Deliverable

A short note (6-10 lines) titled *What the daily report and the hourly snapshot do not show* with three named parts: **Corrections** (the right error rate and latency, with numbers),
**Hidden events** (the incident and the CPU pattern, with the resolution at which each becomes visible) and **Recommendation** (aggregation and sampling rules for the report and the alerts).
Include one chart.
"""
