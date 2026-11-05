"""Lesson 30 - Capstone: statistical monitoring of an application (distribution, trend/season, detectors, decision)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.utils import get_column_letter

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "30-capstone-statistical-monitoring-dashboard"
TITLE = "Capstone: statistical monitoring dashboard"
MODULE = "Statistical monitoring and decision-making"
DATASET = "90 days of an online checkout service: daily requests, p95 latency (ms), errors, deploy and post-mortem labels"
N0 = 45          # phase I: first 45 days define 'normal'
T_DEF = 3.0
K_REF, H_DEC, CAP = 0.5, 5.0, 3.0
THRS = [2, 3, 4, 5, 6, 8]
WD = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
K_MAD = 1.4826


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(3003)
    n = 90
    d = pd.date_range("2026-08-03", periods=n, freq="D")  # a Monday
    wd = d.day_of_week.to_numpy()
    fac = np.array([1.05, 1.08, 1.06, 1.04, 0.97, 0.78, 0.74])
    t = np.arange(n)
    expected = 120000 * (1 + 0.004 * t) * fac[wd]
    req = expected * np.exp(0.04 * rng.standard_normal(n))
    surge, outage, spike, rel, hol = 40, 22, 70, 57, 35
    req[surge] *= 1.9      # marketing push
    req[outage] *= 0.55    # partial outage
    req[hol] *= 0.78       # public holiday (Labor Day): traffic dips, nothing is wrong
    load = req / expected
    lat = 310 * np.exp(0.05 * rng.standard_t(5, n) / np.sqrt(5 / 3)) * load ** 0.15
    lat[outage] *= 1.6
    lat[rel:] *= 1.12      # release regression (+12 % p95)
    lat[spike] *= 1.9      # one-day latency spike
    p = 0.0075 * np.exp(0.05 * rng.standard_normal(n))
    p[outage] = 0.06
    p[rel:] *= 1.2
    p[surge] = 0.012
    err = rng.binomial(req.round().astype(int), p)
    inc = np.zeros(n, int)
    inc[[outage, surge, spike]] = 1
    inc[rel:] = 1
    dep = np.zeros(n, int)
    dep[[10, rel]] = 1
    return pd.DataFrame({"date": d, "requests": req.round().astype(int), "p95_latency_ms": lat.round(1), "errors": err,
                         "deploy": dep, "incident": inc})


def build(out: Path) -> Book:
    from scipy import stats

    df = make_data()
    write_csv(out, df)
    n = len(df)
    req = df["requests"].to_numpy(float)
    lat = df["p95_latency_ms"].to_numpy()
    err = df["errors"].to_numpy(float)
    lab = df["incident"].to_numpy()
    dep = df["deploy"].to_numpy()
    wd = df["date"].dt.day_of_week.to_numpy()
    day = np.arange(1, n + 1, dtype=float)

    # ------------------------------------------------------------ independent python analysis
    sl, ic = np.polyfit(day, req, 1)
    r2 = float(np.corrcoef(day, req)[0, 1] ** 2)
    trend = ic + sl * day
    ratio = req / trend
    fk = np.array([np.median(ratio[wd == k]) for k in range(7)])
    expd = trend * fk[wd]
    lnres = np.log(req / expd)
    sc_req = K_MAD * np.median(np.abs(lnres))
    zr = lnres / sc_req
    ll = np.log(lat)
    med1 = np.median(ll[:N0])
    absdev = np.abs(ll[:N0] - med1)
    s1 = K_MAD * np.median(absdev)
    zl = (ll - med1) / s1
    zcap = np.minimum(zl, CAP)
    cus = np.zeros(n)
    for i in range(n):
        cus[i] = max(0.0, (cus[i - 1] if i else 0.0) + zcap[i] - K_REF)
    alarm = (cus > H_DEC).astype(float)
    first_alarm = int(np.argmax(alarm)) + 1
    rate = err / req
    p0 = float(np.median(rate[:N0]))
    sd_bin = np.sqrt(p0 * (1 - p0) / req)
    serr = (rate - p0) / sd_bin
    ucl3 = p0 + 3 * sd_bin
    pflag = (rate > ucl3).astype(float)
    score = np.maximum.reduce([np.abs(zr), zl, serr])
    flag = (score > T_DEF).astype(float)
    tp = int(((flag == 1) & (lab == 1)).sum())
    fp = int(((flag == 1) & (lab == 0)).sum())
    fn = int(((flag == 0) & (lab == 1)).sum())
    tn = int(((flag == 0) & (lab == 0)).sum())
    prec, rec = tp / (tp + fp), tp / (tp + fn)
    dep_day = int(day[dep == 1].max())
    lag = first_alarm - dep_day
    rate1, rate2 = err[:N0].sum() / req[:N0].sum(), err[-N0:].sum() / req[-N0:].sum()
    skew, skew_ln = float(stats.skew(lat, bias=False)), float(stats.skew(ll, bias=False))
    flagged_req = int((np.abs(zr) > T_DEF).sum())
    ep_before = int(pflag[:dep_day - 1].sum())
    ep_after = int(pflag[dep_day - 1:].sum())

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 30 - Capstone: statistical monitoring dashboard",
             "Solved workbook. Yellow cells are the monitoring policy (T, k, h, cap). Everything else is a live formula.")
    nl = lambda: get_column_letter(b.data.max_column + 1)  # noqa: E731
    l_ = b.local
    R = b.rng

    b.section("0. Monitoring policy (edit the yellow cells)")
    Tc = b.row("Alert threshold T on the combined score (sigma units)", T_DEF, None, "0.0", "Edit me", True)
    kc = b.row("CUSUM reference value k", K_REF, None, "0.00", "Edit me", True)
    hc = b.row("CUSUM decision threshold h", H_DEC, None, "0.0", "Edit me", True)
    capc = b.row("Winsorising cap on the latency z-score for the CUSUM", CAP, None, "0.0", "A single spike must not trigger the CUSUM", True)

    b.section("1. Distribution check: daily p95 latency")
    L_ = R("p95_latency_ms")
    b.add_column("ln_latency", lambda r: f"=LN(C{r})", expected=ll, fmt="0.0000")
    mean_l = b.row("Mean (ms)", f"=AVERAGE({L_})", lat.mean(), "0.0")
    med_l = b.row("Median (ms)", f"=MEDIAN({L_})", float(np.median(lat)), "0.0")
    b.row("Standard deviation (ms)", f"=STDEV({L_})", lat.std(ddof=1), "0.0")
    b.row("P95 of the daily p95 (ms)", f"=PERCENTILE({L_},0.95)", float(np.percentile(lat, 95)), "0.0")
    sk = b.row("Skewness of latency (SKEW)", f"=SKEW({L_})", skew, "0.00", "Positive = long right tail")
    skl = b.row("Skewness of ln(latency)", f"=SKEW({R('ln_latency')})", skew_ln, "0.00", "Smaller after the log; what remains is the genuine spike days")

    b.section("2. Error rate")
    b.add_column("error_rate", lambda r: f"=D{r}/B{r}", expected=rate, fmt="0.0000%")
    r1 = b.row("Error rate, first 45 days", f"=SUM(Data!$D$2:$D${N0 + 1})/SUM(Data!$B$2:$B${N0 + 1})", rate1, "0.000%")
    r2c = b.row("Error rate, last 45 days", f"=SUM(Data!$D${n - N0 + 2}:$D${n + 1})/SUM(Data!$B${n - N0 + 2}:$B${n + 1})", rate2, "0.000%")
    b.row("Ratio last / first (pooled)", f"={l_(r2c)}/{l_(r1)}", rate2 / rate1, "0.00")
    m1r = b.row("Median daily error rate, first 45 days", f"=MEDIAN(Data!${b.col('error_rate')}$2:${b.col('error_rate')}${N0 + 1})",
                float(np.median(rate[:N0])), "0.000%")
    m2r = b.row("Median daily error rate, last 45 days",
                f"=MEDIAN(Data!${b.col('error_rate')}${n - N0 + 2}:${b.col('error_rate')}${n + 1})", float(np.median(rate[-N0:])), "0.000%")
    b.row("Ratio last / first (medians)", f"={l_(m2r)}/{l_(m1r)}", float(np.median(rate[-N0:]) / np.median(rate[:N0])), "0.00",
          "Robust: one outage day no longer dominates")

    b.section("3. Trend and weekday seasonality of requests")
    b.add_column("day", lambda r: "=ROW()-1", expected=day, fmt="0")
    dcol = b.col("day")
    slc = b.row("Trend slope (requests per day)", f"=SLOPE({R('requests')},{R('day')})", sl, "0.0")
    icc = b.row("Trend intercept", f"=INTERCEPT({R('requests')},{R('day')})", ic, "0.0")
    r2r = b.row("R-squared of the linear trend", f"=RSQ({R('requests')},{R('day')})", r2, "0.000")
    b.row("Growth per day (slope / mean requests)", f"={l_(slc)}/AVERAGE({R('requests')})", sl / req.mean(), "0.00%")
    b.add_column("weekday_no", lambda r: f"=WEEKDAY(A{r},2)", expected=wd + 1, fmt="0")
    b.add_column("trend", lambda r: f"={icc}+{slc}*{dcol}{r}", expected=trend, fmt="0")
    b.add_column("ratio", lambda r: f"=B{r}/{b.col('trend')}{r}", expected=ratio, fmt="0.000")
    for k in range(7):
        b.add_column(f"ratio_{WD[k]}", lambda r, k=k: f'=IF({b.col("weekday_no")}{r}={k + 1},{b.col("ratio")}{r},"")',
                     expected=np.where(wd == k, ratio, np.nan), fmt="0.000")
    rows, exp = [], {}
    r0 = b.next_row + 1
    for k in range(7):
        rows.append([k + 1, WD[k], f"=COUNT({R('ratio_' + WD[k])})", f"=MEDIAN({R('ratio_' + WD[k])})"])
        exp.update({(k, 2): int((wd == k).sum()), (k, 3): fk[k]})
    f0, f1 = b.table(["No.", "Weekday", "n", "Median ratio to trend (factor)"], rows, fmt={3: "0.000"}, expect=exp)
    b.bar_chart_from_table("Weekday factor (requests / trend)", 2, [4], f0, f1, anchor="H4", y_title="factor")
    ftab = f"Analysis!$D${f0}:$D${f1}"
    fmax = b.row("Highest weekday factor", f"=MAX({ftab})", fk.max(), "0.000")
    fmin = b.row("Lowest weekday factor", f"=MIN({ftab})", fk.min(), "0.000")
    b.row("Weekend (Sat+Sun mean) as share of the Tuesday factor", f"=AVERAGE(Analysis!$D${f0 + 5}:$D${f1})/Analysis!$D${f0 + 1}",
          fk[5:].mean() / fk[1], "0.0%")
    b.add_column("expected_req", lambda r: f"={b.col('trend')}{r}*INDEX({ftab},{b.col('weekday_no')}{r})", expected=expd, fmt="0")
    b.add_column("ln_resid", lambda r: f"=LN(B{r}/{b.col('expected_req')}{r})", expected=lnres, fmt="0.0000")
    b.add_column("abs_ln_resid", lambda r: f"=ABS({b.col('ln_resid')}{r})", expected=np.abs(lnres), fmt="0.0000")
    scr = b.row("Robust sigma of ln(requests / expected)", f"={K_MAD}*MEDIAN({R('abs_ln_resid')})", sc_req, "0.0000",
                "1.4826 x median absolute residual")
    b.add_column("z_req", lambda r: f"={b.col('ln_resid')}{r}/{scr}", expected=zr, fmt="0.00")
    nreq = b.row("Days with |z_req| > T (requests anomalies)", f'=COUNTIF({R("z_req")},">"&{l_(Tc)})+COUNTIF({R("z_req")},"<"&-{l_(Tc)})', flagged_req, "0")

    b.section("4. Latency level shift: phase I (days 1-45) baseline and CUSUM")
    med1c = b.row("Phase-I median of ln(latency)", f"=MEDIAN(Data!${b.col('ln_latency')}$2:${b.col('ln_latency')}${N0 + 1})", med1, "0.0000")
    b.add_column("absdev_p1", lambda r: f"=ABS({b.col('ln_latency')}{r}-{med1c})",
                 expected=np.concatenate([absdev, np.full(n - N0, np.nan)]), fmt="0.0000")
    s1c = b.row("Phase-I robust sigma of ln(latency)", f"={K_MAD}*MEDIAN(Data!${b.col('absdev_p1')}$2:${b.col('absdev_p1')}${N0 + 1})", s1, "0.0000")
    b.add_column("z_lat", lambda r: f"=({b.col('ln_latency')}{r}-{med1c})/{s1c}", expected=zl, fmt="0.00")
    b.add_column("z_capped", lambda r: f"=MIN({b.col('z_lat')}{r},{capc})", expected=zcap, fmt="0.00")
    zc = b.col("z_capped")
    cl = nl()
    b.add_column("cusum", lambda r: f"=MAX(0,{'0' if r == 2 else cl + str(r - 1)}+{zc}{r}-{kc})", expected=cus, fmt="0.00")
    b.add_column("cusum_alarm", lambda r: f"=IF({b.col('cusum')}{r}>{hc},1,0)", expected=alarm, fmt="0")
    fa = b.row("First CUSUM alarm (day number)", f"=MATCH(1,{R('cusum_alarm')},0)", first_alarm, "0")
    b.add_column("deploy_day", lambda r: f"=IF(E{r}=1,{dcol}{r},0)", expected=np.where(dep == 1, day, 0), fmt="0")
    dd = b.row("Day of the last deploy", f"=MAX({R('deploy_day')})", dep_day, "0")
    b.row("CUSUM alarm lag after the deploy (days)", f"={l_(fa)}-{l_(dd)}", lag, "0")
    b.row("Latency shift estimated from phase I: mean z, last 33 days",
          f"=AVERAGE(Data!${b.col('z_lat')}${dep_day + 1}:${b.col('z_lat')}${n + 1})", float(zl[dep_day - 1:].mean()), "0.00",
          "Sigma units; about 2 sigma = +12 %")

    b.section("5. Error-rate p-chart (binomial limits from phase-I median rate)")
    p0c = b.row("p0 = median error rate of days 1-45", f"=MEDIAN(Data!${b.col('error_rate')}$2:${b.col('error_rate')}${N0 + 1})", p0, "0.0000%")
    b.add_column("err_sigma", lambda r: f"=SQRT({p0c}*(1-{p0c})/B{r})", expected=sd_bin, fmt="0.000000")
    b.add_column("ucl3", lambda r: f"={p0c}+3*{b.col('err_sigma')}{r}", expected=ucl3, fmt="0.0000%")
    b.add_column("pchart_flag", lambda r: f"=IF({b.col('error_rate')}{r}>{b.col('ucl3')}{r},1,0)", expected=pflag, fmt="0")
    b.add_column("z_err", lambda r: f"=({b.col('error_rate')}{r}-{p0c})/{b.col('err_sigma')}{r}", expected=serr, fmt="0.00")
    b.row("Days above the 3-sigma UCL before the deploy", f"=SUMPRODUCT(({R('day')}<{l_(dd)})*{R('pchart_flag')})", ep_before, "0",
          "A pure binomial process would give about 0.1 % of days")
    b.row("Days above the 3-sigma UCL from the deploy on", f"=SUMPRODUCT(({R('day')}>={l_(dd)})*{R('pchart_flag')})", ep_after, "0")

    b.section("6. Combined score, flags and evaluation against the post-mortem labels")
    b.add_column("score", lambda r: f"=MAX(ABS({b.col('z_req')}{r}),{b.col('z_lat')}{r},{b.col('z_err')}{r})", expected=score, fmt="0.00")
    b.add_column("flag", lambda r: f"=IF({b.col('score')}{r}>{Tc},1,0)", expected=flag, fmt="0")
    F_, I_ = R("flag"), R("incident")
    nfl = b.row("Days flagged", f"=SUM({F_})", flag.sum(), "0")
    tpc = b.row("TP (flagged, incident)", f"=COUNTIFS({F_},1,{I_},1)", tp, "0")
    fpc = b.row("FP (flagged, no incident)", f"=COUNTIFS({F_},1,{I_},0)", fp, "0")
    fnc = b.row("FN (not flagged, incident)", f"=COUNTIFS({F_},0,{I_},1)", fn, "0")
    b.row("TN", f"=COUNTIFS({F_},0,{I_},0)", tn, "0")
    pc = b.row("Precision", f"={l_(tpc)}/({l_(tpc)}+{l_(fpc)})", prec, "0.000")
    rc = b.row("Recall", f"={l_(tpc)}/({l_(tpc)}+{l_(fnc)})", rec, "0.000")
    b.row("Flags per 30 days of operation", f"={l_(nfl)}/{n}*30", flag.sum() / n * 30, "0.0")
    rows, exp = [], {}
    r0 = b.next_row + 1
    sweep = []
    for i, t in enumerate(THRS):
        r = r0 + i
        fl = score > t
        tp_, fp_, fn_ = int((fl & (lab == 1)).sum()), int((fl & (lab == 0)).sum()), int((~fl & (lab == 1)).sum())
        pr_, rc_ = (tp_ / (tp_ + fp_) if tp_ + fp_ else 0), tp_ / (tp_ + fn_)
        f1_ = 2 * pr_ * rc_ / (pr_ + rc_) if pr_ + rc_ else 0
        sweep.append((t, int(fl.sum()), tp_, fp_, fn_, pr_, rc_, f1_))
        S_ = R("score")
        rows.append([t, f'=COUNTIF({S_},">"&A{r})', f'=COUNTIFS({S_},">"&A{r},{I_},1)', f'=COUNTIFS({S_},">"&A{r},{I_},0)',
                     f'=COUNTIFS({S_},"<="&A{r},{I_},1)', f"=IF(C{r}+D{r}=0,0,C{r}/(C{r}+D{r}))", f"=C{r}/(C{r}+E{r})",
                     f"=IF(F{r}+G{r}=0,0,2*F{r}*G{r}/(F{r}+G{r}))"])
        exp.update({(i, 1): fl.sum(), (i, 2): tp_, (i, 3): fp_, (i, 4): fn_, (i, 5): pr_, (i, 6): rc_, (i, 7): f1_})
    s0, s1_ = b.table(["T", "Flagged", "TP", "FP", "FN", "Precision", "Recall", "F1"], rows,
                      fmt={5: "0.000", 6: "0.000", 7: "0.000"}, expect=exp)
    b.line_chart_from_table("Precision, recall, F1 by threshold", 1, [6, 7, 8], s0, s1_, anchor="H24", x_title="T")
    b.line_chart("Combined anomaly score", "date", ["score"], anchor="H44", y_title="sigma units")
    best = max(sweep, key=lambda s: (s[7], -s[3]))
    z_out = [(df["date"][i].strftime("%b %d"), round(float(zr[i]), 1)) for i in (22, 35, 40)]

    memo = (f"DECISION: alert when the combined score exceeds T = {T_DEF:g} ({flag.sum():.0f} of {n} days flagged: {tp} true incident days, "
            f"{fp} false alarm(s), {fn} missed). Precision {prec:.0%}, recall {rec:.0%}; at this volume expect about "
            f"{flag.sum() / n * 30:.0f} flagged days per 30, of which about {fp / n * 30:.1f} are false. "
            f"The CUSUM raised the sustained-latency alarm on day {first_alarm}, {lag} days after the day-{dep_day} deploy; a rollback then would have "
            f"saved {n - first_alarm} degraded days. Latency p95 is right-skewed (skew {skew:.2f}, {skew_ln:.2f} after ln) so limits are set on the log scale; "
            f"requests follow a {sl:.0f}/day trend with a weekend factor of {fk[5:].mean():.2f} vs {fk[:5].mean():.2f} on weekdays, so a weekend dip is not an alarm. "
            f"RISKS: error-rate limits assume binomial noise ({ep_before} pre-deploy day(s) already breach 3 sigma: overdispersion); the public-holiday dip is a "
            f"false alarm no seasonal model knows about; labels come from one post-mortem; phase I (45 days) is short.")
    b.answers([
        ("Latency distribution: mean, median, skewness, skewness of ln(latency)", f"={sk}",
         f"Mean {lat.mean():.0f} ms vs median {np.median(lat):.0f} ms; skewness {skew:.2f}, which falls to {skew_ln:.2f} on the log scale. "
         f"The tail is made of a few days (the day-70 spike, the outage) plus the post-deploy level; the log scale tames it, and "
         f"because latency effects are multiplicative (+12 %), limits belong on that scale."),
        ("Error rate in the first and last 45 days: pooled and as a median of daily rates", f"={r1}",
         f"Pooled: {rate1:.3%} first 45 days, {rate2:.3%} last 45 days: only x{rate2 / rate1:.2f}, because the day-23 outage (6 % errors) inflates the first half. "
         f"Median daily rate: {np.median(rate[:N0]):.3%} vs {np.median(rate[-N0:]):.3%} = x{np.median(rate[-N0:]) / np.median(rate[:N0]):.2f}: a real, sustained increase that a pooled ratio hides."),
        ("Request trend: slope, R-squared, growth per day", f"={slc}",
         f"+{sl:.0f} requests per day ({sl / req.mean():.2%} of the mean), R-squared only {r2:.2f}: the weekday cycle and the few anomalies dominate the variation."),
        ("Weekday factors: highest, lowest and weekend share of Tuesday", f"={fmax}",
         f"Highest {fk.max():.3f} ({WD[int(fk.argmax())]}), lowest {fk.min():.3f} ({WD[int(fk.argmin())]}); the weekend runs at "
         f"{fk[5:].mean() / fk[1]:.0%} of a Tuesday."),
        ("Requests anomalies at |z| > T: how many days and which", f"={l_(nreq)}",
         f"{flagged_req} days: " + ", ".join(f"{df['date'][i]:%b %d} (z = {zr[i]:+.1f})" for i in np.where(np.abs(zr) > T_DEF)[0])
         + ". The outage is a drop, the marketing push a surge and the public holiday a dip that is not an incident."),
        ("Latency: phase-I sigma, first CUSUM alarm, deploy day and lag", f"={fa}",
         f"Robust sigma of ln(latency) = {s1:.4f}. Alarm on day {first_alarm}, deploy on day {dep_day}: lag {lag} days. The cap of {CAP:g} stops "
         f"the outage day (z = {zl[22]:.1f}) from triggering it alone."),
        ("Error-rate p-chart: p0 and days above the 3-sigma UCL before and after the deploy", f"={p0c}",
         f"p0 = {p0:.3%}. Days above the UCL: {ep_before} before the deploy, {ep_after} from the deploy on. Even before the deploy the day-to-day rate varies more "
         f"than binomial sampling (overdispersion), so 3 binomial sigmas is too tight."),
        (f"Combined score at T = {T_DEF:g}: days flagged, TP, FP, FN, precision, recall", f"={nfl}",
         f"{int(flag.sum())} flagged; TP {tp}, FP {fp}, FN {fn}, TN {tn}; precision {prec:.3f}, recall {rec:.3f}. "
         f"The false alarm(s): " + ", ".join(f"{df['date'][i]:%b %d}" for i in np.where((flag == 1) & (lab == 0))[0]) + "."),
        ("Threshold sweep: choose T", f"=Analysis!B{s0 + 2}",
         "T / flagged / TP / FP / FN / F1: " + "; ".join(f"{s[0]} / {s[1]} / {s[2]} / {s[3]} / {s[4]} / {s[7]:.2f}" for s in sweep)
         + f". Best F1 at T = {best[0]}. Lower T finds more of the slow-burn release days but adds false alarms; high T only catches the dramatic days."),
        ("Decision memo (see Deliverable): policy, evidence, expected alert load, risks", "see memo", memo),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-30-monitoring-capstone", "30 · Capstone: monitoring dashboard",
             "Distribution, trend and weekday seasonality, robust anomaly scores, CUSUM and binomial error-rate limits for 90 days "
             "of an online checkout service; flagged days are evaluated against the post-mortem labels.",
             df.rename(columns={"date": "time"}), "time")
    d.stat("Volume and latency", {"requests/day": req.mean(), "mean p95 (ms)": lat.mean(), "median p95 (ms)": np.median(lat)},
           "Mean above median: the right-skewed latency tail.", decimals=0, w=7)
    d.stat("Error rate", {"pooled 1st half": rate1, "pooled 2nd half": rate2,
                          "median 1st": float(np.median(rate[:N0])), "median 2nd": float(np.median(rate[-N0:]))},
           "The pooled rates barely differ (the day-23 outage inflates the first half); the medians show the real increase.",
           unit="percentunit", decimals=2, w=7)
    d.stat("Detector result (T = 3)", {"days flagged": flag.sum(), "true incident days": tp, "false alarms": fp, "missed": fn,
                                       "CUSUM alarm (day)": first_alarm, "deploy (day)": dep_day},
           "Flags are evaluated against post-mortem labels; the CUSUM fires a few days after the day-58 deploy.", decimals=0, w=10)
    flagged_r = np.where(np.abs(zr) > T_DEF, req, np.nan)
    rq = pd.DataFrame({"time": df["date"], "requests": req, "expected": expd, "upper": expd * np.exp(T_DEF * sc_req),
                       "lower": expd * np.exp(-T_DEF * sc_req), "anomaly": flagged_r})
    d.timeseries("Requests per day: trend x weekday expectation and alarm band", rq,
                 "Expected = linear trend x median weekday factor; band = +/- T robust sigmas on the log scale. Dots: outage, holiday dip, marketing surge.",
                 points=["anomaly"], dashed=["upper", "lower"],
                 colors={"requests": "#4E79A7", "expected": "#76B7B2", "upper": "#E15759", "lower": "#E15759", "anomaly": "#F28E2B"}, w=12)
    lim = np.exp(med1 + T_DEF * s1)
    lt = pd.DataFrame({"time": df["date"], "p95_latency_ms": lat, "phase_I_median": np.exp(med1), "limit_T": lim,
                       "flagged": np.where(zl > T_DEF, lat, np.nan)})
    d.timeseries("p95 latency vs phase-I baseline", lt, "Baseline = median of days 1-45 (log scale); dashed = baseline + T robust sigmas. "
                 "The post-deploy level sits about 2 sigma above baseline: too small for a point rule, obvious for the CUSUM.",
                 points=["flagged"], dashed=["phase_I_median", "limit_T"], unit="ms",
                 colors={"p95_latency_ms": "#4E79A7", "phase_I_median": "#76B7B2", "limit_T": "#E15759", "flagged": "#F28E2B"}, w=12)
    cs = pd.DataFrame({"time": df["date"], "CUSUM": np.minimum(cus, 3 * H_DEC), "h": H_DEC})
    d.timeseries("CUSUM of latency (capped z, k = 0.5)", cs, "Display clipped at 3h. The cap makes the day-23 outage unable to trigger the alarm; "
                 "the sustained +2 sigma after the deploy crosses h within days.", dashed=["h"],
                 colors={"CUSUM": "#F28E2B", "h": "#E15759"}, w=12)
    clip = lambda v: np.minimum(v, 0.015)  # noqa: E731  (the 6 % outage day would flatten the rest)
    et = pd.DataFrame({"time": df["date"], "error_rate": clip(rate), "p0": p0, "ucl_3sigma": ucl3, "ucl_T": p0 + T_DEF * sd_bin,
                       "flagged": np.where(serr > T_DEF, clip(rate), np.nan)})
    d.timeseries("Error rate with binomial control limits", et, "p-chart limits vary with daily volume. Dots exceed p0 + T sigmas. Display clipped at 1.5 % (the day-23 outage reached 6 %).",
                 points=["flagged"], dashed=["p0", "ucl_3sigma", "ucl_T"], unit="percentunit",
                 colors={"error_rate": "#4E79A7", "p0": "#76B7B2", "ucl_3sigma": "#EDC948", "ucl_T": "#E15759", "flagged": "#F28E2B"}, w=12)
    d.bars("Weekday factor (requests / trend)", pd.DataFrame({"weekday": WD, "factor": fk}),
           "Median of the ratio to trend for each weekday; weekends are about 25 % below weekdays.", w=8)
    ft = df.assign(date=df["date"].dt.strftime("%Y-%m-%d"), error_rate=(rate * 100).round(2), score=score.round(1))
    ft = ft.loc[flag == 1, ["date", "requests", "p95_latency_ms", "error_rate", "score", "incident"]].rename(
        columns={"error_rate": "err %", "p95_latency_ms": "p95 ms"})
    d.table("Table of flagged days (T = 3)", ft, "incident = post-mortem label; flagged days with incident = 0 are false alarms (the holiday dip, a noisy error-rate day).", w=16, h=11)
    d.save(out)

    md(out / "theory.md", (THEORY.replace("@P0@", f"{p0:.4f}").replace("@NMEAN@", f"{req.mean():,.0f}")
                           .replace("@SIGMA_BIN@", f"{np.sqrt(p0 * (1 - p0) / req.mean()):.6f}")
                           .replace("@UCL3@", f"{p0 + 3 * np.sqrt(p0 * (1 - p0) / req.mean()):.4f}")
                           .replace("@SK@", f"{skew:.2f}").replace("@SKL@", f"{skew_ln:.2f}")
                           .replace("@WE@", f"{fk[5:].mean():.2f}")
                           .replace("@S1@", f"{s1:.3f}").replace("@FIRST@", str(first_alarm)).replace("@DEP@", str(dep_day))))
    md(out / "task.md", TASK)
    return b


THEORY = r"""
# Theory: a statistical monitoring dashboard, end to end

## Why a capstone

Every earlier lesson answers one question: is the distribution skewed, is there a trend, is this point unusual, has the level moved, how many alerts
are false. A real monitoring system needs all of them at once, chosen so that the people who are paged trust the pages. A dashboard
that shows a latency line and a red threshold is not monitoring; monitoring is a **policy** (what to watch, what counts as abnormal, who is told)
together with **evidence** that the policy works. This lesson walks through building one for the daily metrics of a checkout service:
requests, p95 latency and error count.

## The workflow

1. **Frame the decision.** What action does an alert trigger (page, rollback, ticket)? What does a false alarm cost versus a miss
   ([lesson 29](../29-false-alarms-and-detection-performance/theory.md))? The answer fixes how aggressive the thresholds should be.
2. **Look at the distribution first** ([lesson 1](../01-distribution-shapes-and-heavy-tails/theory.md),
   [3](../03-percentiles-and-extreme-values/theory.md)). Daily p95 latency here has skewness @SK@, which drops to @SKL@ after taking logs
   (what remains is a handful of genuinely extreme days): latency is multiplicative, so limits belong on the log scale where "12 % slower" is one fixed distance whatever the baseline.
3. **Remove trend and seasonality** ([lesson 7](../07-trend-seasonality-and-noise/theory.md)). Requests grow linearly and have a strong weekday factor
   (weekends at about @WE@ of the trend). Fit the trend, take the *median* ratio to trend per weekday (robust to the very anomalies we want to find), and
   score the residual $z=\ln(\text{requests}/\text{expected})/\hat\sigma$ with $\hat\sigma=1.4826\cdot\text{median}|\ln\text{residual}|$
   ([lesson 28](../28-time-series-anomaly-detection/theory.md)).
4. **Pick a detector per failure type.**
   - *Point anomalies* (outage, spike): robust z-scores, flag $|z|>T$.
   - *Sustained small shifts* (a release that is 12 % slower): CUSUM on the standardised log latency
     ([lesson 27](../27-change-point-detection/theory.md)), with a **Winsorising cap** (here 3) so that one extreme day cannot trigger it.
   - *Rates* (errors per request): a p-chart. With daily volume $n_t$ the binomial standard deviation of the observed rate is
     $\sqrt{p_0(1-p_0)/n_t}$, so the limit moves with traffic. Worked example: $p_0=@P0@$ and $n=@NMEAN@$ give
     $\sigma=@SIGMA_BIN@$ and a 3-sigma upper limit of @UCL3@ ([lesson 26](../26-statistical-process-control/theory.md)).
5. **Combine and calibrate.** Reduce the detectors to one *sigma-scale* score, here $\max(|z_{req}|,z_{lat},z_{err})$, and choose $T$ from labelled history
   with a threshold sweep (precision, recall, F1, cost). A maximum over three scores raises the false-alarm rate roughly threefold compared with one score
   at the same $T$; that is the price of watching three things.
6. **Write the decision memo**: the policy (what, which $T$, $k$, $h$), the evidence (flags, false alarms, misses, delays), the expected alert load per
   month, and the risks.

## Phase I and what it assumes

All baselines are estimated on the first 45 days with medians and MADs, because the phase-I window itself contains an outage, a marketing surge and a
holiday. A mean and standard deviation would be inflated by exactly these days; the median is not
([lesson 2](../02-robust-statistics/theory.md)). If phase I contained a regression, the detectors would be calibrated to the broken state.

## Reading the results as a decision-maker

- A **sustained** problem (the release regression) is found by the CUSUM @FIRST@ - @DEP@ days after the deploy, even though almost no single day
  looks extreme; a pure point detector would only flag the worst of those days. That lag is the detection delay of [lesson 29](../29-false-alarms-and-detection-performance/theory.md).
- A **legitimate** change (public holiday) is flagged because the model knows nothing about it. Add a calendar of known events, or accept this
  false alarm and say so in the memo.
- **Overdispersion**: the day-to-day variation of the error rate is larger than binomial sampling alone predicts (retries, client mix),
  so binomial limits give extra pre-deploy exceedances. Either widen the limits (use $T$ rather than 3) or estimate the extra variance (Laney p').

## Assumptions and pitfalls

1. **Evaluating on the data you tuned on.** The sweep here uses all 90 days; the honest procedure is to tune on one period and report on the next.
2. **Labels are post-hoc.** Every day after the deploy is labelled an incident, but a team would not have ticketed most of them; precision depends on who labels.
3. **A linear trend fitted on all days** is slightly bent by the anomalies; refit after removing flagged days.
4. **Multiple detectors, multiple false-alarm budgets.** Count alerts per month, not per detector.
5. **Alert fatigue** is the real failure mode: a rule with 90 % recall that pages ten times a week will be muted.
6. **Averages are not monitoring.** The overall mean latency changes by little; the decision-relevant facts are the shift after the deploy and the error rate.

## Related notes

- [Percentiles](../03-percentiles-and-extreme-values/theory.md), [trend and seasonality](../07-trend-seasonality-and-noise/theory.md),
  [rolling statistics](../10-rolling-statistics/theory.md), [prediction intervals](../25-prediction-intervals-and-forecast-uncertainty/theory.md)
- [Statistical process control](../26-statistical-process-control/theory.md), [change points](../27-change-point-detection/theory.md),
  [anomaly detection](../28-time-series-anomaly-detection/theory.md), [detection performance](../29-false-alarms-and-detection-performance/theory.md)
- Repo notes: [seasonality and trends](../../notes/time_series/seasonality_and_trends.md), [descriptive statistics](../../notes/foundations/descriptive_statistics.md)
"""

TASK = r"""
# Task: capstone - a statistical monitoring dashboard for a checkout service

## Scenario

You are the new data analyst on the platform team of an online shop. Leadership asks for **one dashboard and one rule set** that tells on-call
engineers when the checkout service is degraded, without paging them for ordinary weekend dips. You have 90 days of daily metrics, the
deploy log, and a post-mortem list of the days that were later judged "degraded". Build the analysis, choose the alert policy, and write the
decision memo the head of engineering will read.

## Data

`data.csv` - 90 days (2026-08-03 to 2026-10-31), one row per day.

| column | meaning |
|---|---|
| `date` | calendar day (the series starts on a Monday) |
| `requests` | checkout requests that day |
| `p95_latency_ms` | 95th percentile of request latency for the day, milliseconds |
| `errors` | requests that ended in a server error |
| `deploy` | 1 on days a release was deployed |
| `incident` | 1 on days the post-mortem judged the service degraded, else 0 |

Treat days 1-45 as **phase I** ("normal"); use medians and MADs there.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. *Distribution.* Mean, median and skewness of `p95_latency_ms`; skewness of its natural logarithm. Which scale should the limits use?
2. Error rate (errors / requests) pooled over the first and over the last 45 days, and the median daily error rate in each half. Compare the two ratios: which one is more trustworthy, and why?
3. *Trend.* Fit a straight line to `requests` against the day number: slope, R-squared, growth per day as a share of the mean.
4. *Seasonality.* Divide requests by the trend, take the **median** ratio for each weekday. Highest and lowest factor? How do weekends compare with a Tuesday?
5. Build the expected requests (trend x weekday factor), the log residual and its robust z-score. How many days exceed $|z| > 3$ and what are they?
6. *Latency shift.* Standardise $\ln$(latency) with the phase-I median and robust sigma, cap $z$ at 3 and run an upper CUSUM ($k = 0.5$, $h = 5$). On which day does it alarm, and how many days after the last deploy?
7. *Error rate.* Compute $p_0$ (median phase-I rate), the binomial 3-sigma upper limit per day and the number of days above it before and after the last deploy. What does the pre-deploy count say about the binomial assumption?
8. *Combined detector.* Score each day as the maximum of $|z_{req}|$, $z_{lat}$ and the error-rate z. With $T = 3$: days flagged, TP, FP, FN, precision, recall against `incident`. Which flagged day is a false alarm and why?
9. Sweep $T = 2, 3, 4, 5, 6, 8$ and tabulate flagged, TP, FP, FN, precision, recall, F1. Which T would you deploy?
10. Write the **decision memo** (see Deliverable) and name two risks the numbers do not show.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Requests per day", which three events leave the alarm band and which of them was not an incident?
- In "p95 latency vs phase-I baseline" and "CUSUM of latency", why does the point rule stay quiet while the CUSUM alarms?
- In "Error rate with binomial control limits", what changes on the deploy day, and what do the two limit lines (3 sigma and T sigma) tell you about
  the choice of limit width?

## Deliverable

A one-page decision memo with four named parts: **Policy** (the detectors and the values of T, k, h), **Evidence** (flags, false alarms, misses,
the CUSUM lag after the deploy), **Alert load** (expected pages per month, how many false) and **Risks** (at least two: e.g. short phase I, label quality,
overdispersion, holidays). Include one chart.
"""
