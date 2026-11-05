"""Lesson 29 - False alarms and detection performance (confusion matrix, threshold sweep, ROC/PR, base rate)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.chart import Reference, ScatterChart, Series

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import Book, Dash, md, write_csv  # noqa: E402

SLUG = "29-false-alarms-and-detection-performance"
TITLE = "False alarms and detection performance"
MODULE = "Statistical monitoring and decision-making"
DATASET = "720 hourly furnace-zone temperature readings vs controller set-point, 8 labelled fault episodes"
T_DEF = 3.0
C_FN, C_FP, TARGET_RECALL = 10, 1, 0.8
K_MAD = 1.4826
THR = [0.0] + [round(0.25 * i, 2) for i in range(2, 25)] + [99.0]  # 0, 0.5 ... 6, 99
PREV = [0.001, 0.005, 0.02, 0.2]


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(2905)
    n = 720
    t = pd.date_range("2026-06-01", periods=n, freq="h")
    h = t.hour.to_numpy()
    sp = np.where((h >= 6) & (h < 22), 70.0, 66.0)          # day / night set-point
    x = sp + 0.5 * rng.standard_t(5, n) / np.sqrt(5 / 3)    # heavy-ish tails, sd 0.5 C
    lab = np.zeros(n, int)
    starts: list[int] = []
    while len(starts) < 8:
        s = int(rng.integers(30, n - 10))
        if all(abs(s - q) > 40 for q in starts):
            starts.append(s)
    for s in sorted(starts):
        length = int(rng.integers(3, 9))
        mag = rng.uniform(2.5, 6.5) * rng.choice([-1, 1])      # in noise sd; the fault ramps up over the episode
        for j in range(length):
            x[s + j] += mag * 0.5 * (j + 1) / length * (0.9 + 0.2 * rng.random())
            lab[s + j] = 1
    return pd.DataFrame({"timestamp": t, "temp_c": x.round(2), "setpoint_c": sp, "is_fault": lab})


def counts(score, lab, t):
    fl = score >= t
    tp = int((fl & (lab == 1)).sum())
    fp = int((fl & (lab == 0)).sum())
    fn = int((~fl & (lab == 1)).sum())
    tn = int((~fl & (lab == 0)).sum())
    return tp, fp, fn, tn


def metrics(tp, fp, fn, tn):
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn)
    fpr = fp / (fp + tn)
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    return prec, rec, fpr, f1


def build(out: Path) -> Book:
    df = make_data()
    write_csv(out, df)
    x, sp, lab = df["temp_c"].to_numpy(), df["setpoint_c"].to_numpy(), df["is_fault"].to_numpy()
    n = len(df)
    resid = x - sp
    absr = np.abs(resid)
    sig = K_MAD * float(np.median(absr))
    score = absr / sig
    P, N = int(lab.sum()), int((lab == 0).sum())
    flag = (score >= T_DEF).astype(float)
    # episodes
    ep = np.zeros(n)
    k = 0
    for i in range(n):
        if lab[i] == 1:
            if i == 0 or lab[i - 1] == 0:
                k += 1
            ep[i] = k
    det = np.zeros(n)
    for i in range(n):
        if lab[i] == 0:
            det[i] = 0
        elif flag[i] == 1:
            det[i] = 1
        else:
            det[i] = det[i - 1] if (i > 0 and ep[i] == ep[i - 1]) else 0
    n_ep = int(ep.max())
    ep_rows = []
    for e in range(1, n_ep + 1):
        idx = np.where(ep == e)[0]
        ep_rows.append(dict(start=df["timestamp"][idx[0]], length=len(idx), flagged=int(flag[idx].sum()),
                            delay=int((det[idx] == 0).sum()), detected=int(det[idx].max())))
    tp, fp, fn, tn = counts(score, lab, T_DEF)
    prec, rec, fpr, f1 = metrics(tp, fp, fn, tn)

    sweep = []
    for t in THR:
        c = counts(score, lab, t)
        pr, rc, fr, ff = metrics(*c)
        sweep.append(dict(thr=t, tp=c[0], fp=c[1], fn=c[2], tn=c[3], prec=pr, rec=rc, fpr=fr, f1=ff,
                          cost=C_FN * c[2] + C_FP * c[1]))
    sw = pd.DataFrame(sweep)
    auc = sum((sw.fpr[i] - sw.fpr[i + 1]) * (sw.rec[i] + sw.rec[i + 1]) / 2 for i in range(len(sw) - 1))
    best_f1_t = float(sw.thr[sw.f1.idxmax()])
    t_recall = float(max(t for t, r in zip(sw.thr, sw.rec) if r >= TARGET_RECALL))
    fpr_at_recall = float(sw.fpr[sw.thr == t_recall].iloc[0])
    best_cost_t = float(sw.thr[sw.cost.idxmin()])
    cost_def = C_FN * fn + C_FP * fp

    # ------------------------------------------------------------------ workbook
    b = Book(df, "Lesson 29 - False alarms and detection performance",
             "Solved workbook. Yellow cells: alert threshold, recall target, costs. The sweep table does not depend on the threshold cell.")
    b.section("1. Score: how far is each reading from its set-point, in robust sigmas")
    sigc = None
    b.add_column("resid", lambda r: f"=B{r}-C{r}", expected=resid, fmt="0.00")
    b.add_column("abs_resid", lambda r: f"=ABS(E{r})", expected=absr, fmt="0.00")
    sigc = b.row("Robust sigma = 1.4826 x median |residual| (C)", f"={K_MAD}*MEDIAN({b.rng('abs_resid')})", sig, "0.000")
    b.add_column("score", lambda r: f"=F{r}/{sigc}", expected=score, fmt="0.00")
    Tc = b.row("Alert threshold T (alarm when score >= T)", T_DEF, None, "0.00", "Edit me", True)
    b.add_column("alarm", lambda r: f"=IF(G{r}>={Tc},1,0)", expected=flag, fmt="0")
    # episode helper columns
    b.add_column("episode", lambda r: ("=IF(D2=1,1,0)" if r == 2 else f"=IF(D{r}=0,0,IF(D{r - 1}=1,I{r - 1},MAX(I$1:I{r - 1})+1))"),
                 expected=ep, fmt="0")
    b.add_column("detected_so_far", lambda r: ("=IF(AND(D2=1,H2=1),1,0)" if r == 2 else
                                               f"=IF(D{r}=0,0,IF(H{r}=1,1,IF(I{r}=I{r - 1},J{r - 1},0)))"), expected=det, fmt="0")
    assert [b.col(c) for c in ("resid", "abs_resid", "score", "alarm", "episode", "detected_so_far")] == list("EFGHIJ")
    nfault = b.row("Fault readings (is_fault = 1)", f"=SUM({b.rng('is_fault')})", P, "0")
    prev = b.row("Fault prevalence (share of readings)", f"={b.local(nfault)}/COUNT({b.rng('is_fault')})", P / n, "0.0%")

    b.section("2. Confusion matrix at the chosen threshold")
    S, L, A = b.rng("score"), b.rng("is_fault"), b.rng("alarm")
    tpc = b.row("TP: alarm and fault", f"=COUNTIFS({A},1,{L},1)", tp, "0")
    fpc = b.row("FP: alarm but no fault (false alarm)", f"=COUNTIFS({A},1,{L},0)", fp, "0")
    fnc = b.row("FN: no alarm but fault (missed)", f"=COUNTIFS({A},0,{L},1)", fn, "0")
    tnc = b.row("TN: no alarm and no fault", f"=COUNTIFS({A},0,{L},0)", tn, "0")
    l_ = b.local
    precc = b.row("Precision = TP / (TP + FP)", f"={l_(tpc)}/({l_(tpc)}+{l_(fpc)})", prec, "0.000", "Of the alarms, how many were real")
    recc = b.row("Recall (TPR) = TP / (TP + FN)", f"={l_(tpc)}/({l_(tpc)}+{l_(fnc)})", rec, "0.000", "Of the faults, how many were caught")
    fprc = b.row("False-positive rate = FP / (FP + TN)", f"={l_(fpc)}/({l_(fpc)}+{l_(tnc)})", fpr, "0.0000", "Share of healthy readings that alarm")
    f1c = b.row("F1 = 2PR / (P + R)", f"=2*{l_(precc)}*{l_(recc)}/({l_(precc)}+{l_(recc)})", f1, "0.000")
    b.row("False alarms per 30 days (= FP in this data)", f"={l_(fpc)}", fp, "0")
    arl0 = b.row("ARL0: healthy readings per false alarm (hours)", f"=({l_(fpc)}+{l_(tnc)})/{l_(fpc)}", (fp + tn) / fp, "0.0",
                 "Average run length between false alarms")

    b.section("3. Fault episodes: detection delay")
    rows, exp = [], {}
    r0 = b.next_row + 1
    for i, e in enumerate(ep_rows):
        r = r0 + i
        k_ = i + 1
        rows.append([k_, f"=INDEX({b.rng('timestamp')},MATCH(A{r},{b.rng('episode')},0))",
                     f"=COUNTIF({b.rng('episode')},A{r})", f"=COUNTIFS({b.rng('episode')},A{r},{A},1)",
                     f"=COUNTIFS({b.rng('episode')},A{r},{b.rng('detected_so_far')},0)",
                     f"=IF(COUNTIFS({b.rng('episode')},A{r},{b.rng('detected_so_far')},1)>0,1,0)",
                     f'=IF(F{r}=1,E{r},"")'])
        exp.update({(i, 2): e["length"], (i, 3): e["flagged"], (i, 4): e["delay"], (i, 5): e["detected"]})
        if e["detected"]:
            exp[(i, 6)] = e["delay"]
    e0, e1 = b.table(["Episode", "Start", "Length (h)", "Alarm readings", "Delay (h) if first alarm", "Detected (1/0)",
                      "Delay if detected"], rows, fmt={1: "mm-dd hh:mm", 2: "0", 3: "0", 4: "0", 5: "0", 6: "0"}, expect=exp)
    ndet = b.row("Episodes detected", f"=SUM(F{e0}:F{e1})", sum(e["detected"] for e in ep_rows), "0")
    det_delays = [e["delay"] for e in ep_rows if e["detected"]]
    mdel = b.row("Mean detection delay of detected episodes (hours)", f"=AVERAGE(G{e0}:G{e1})", float(np.mean(det_delays)), "0.00",
                 "0 = alarm on the first faulty reading")

    b.section("4. Sweep the threshold (does not use the yellow T)")
    cfn = b.row("Cost of a missed fault reading", C_FN, None, "0", "Edit me (lost product, scrap)", True)
    cfp = b.row("Cost of a false alarm", C_FP, None, "0", "Edit me (technician walk)", True)
    trg = b.row("Recall target", TARGET_RECALL, None, "0.00", "Edit me", True)
    rows, exp = [], {}
    r0 = b.next_row + 1
    m = len(THR)
    Pref, Nref = b.local(nfault), f"(COUNT({L})-{b.local(nfault)})"
    for i, t in enumerate(THR):
        r = r0 + i
        nxt = r + 1
        rows.append([t, f'=COUNTIFS({S},">="&A{r},{L},1)', f'=COUNTIFS({S},">="&A{r},{L},0)', f"={Pref}-B{r}", f"={Nref}-C{r}",
                     f"=IF(B{r}+C{r}=0,0,B{r}/(B{r}+C{r}))", f"=B{r}/{Pref}", f"=C{r}/{Nref}",
                     f"=IF(F{r}+G{r}=0,0,2*F{r}*G{r}/(F{r}+G{r}))", f"={b.local(cfn)}*D{r}+{b.local(cfp)}*C{r}",
                     (f"=(H{r}-H{nxt})*(G{r}+G{nxt})/2" if i < m - 1 else 0),
                     f'=IF(G{r}>={b.local(trg)},A{r},"")'])
        s_ = sweep[i]
        exp.update({(i, 1): s_["tp"], (i, 2): s_["fp"], (i, 3): s_["fn"], (i, 4): s_["tn"], (i, 5): s_["prec"], (i, 6): s_["rec"],
                    (i, 7): s_["fpr"], (i, 8): s_["f1"], (i, 9): s_["cost"]})
        if i < m - 1:
            exp[(i, 10)] = (sw.fpr[i] - sw.fpr[i + 1]) * (sw.rec[i] + sw.rec[i + 1]) / 2
        if sw.rec[i] >= TARGET_RECALL:
            exp[(i, 11)] = s_["thr"]
    t0, t1 = b.table(["T", "TP", "FP", "FN", "TN", "Precision", "Recall", "FPR", "F1", "Cost", "ROC area step", "T if recall ok"],
                     rows, fmt={0: "0.00", 5: "0.000", 6: "0.000", 7: "0.0000", 8: "0.000", 9: "0", 10: "0.0000"}, expect=exp)
    a = lambda col: f"${col}${t0}:${col}${t1}"  # noqa: E731
    auc_c = b.row("ROC AUC (trapezoid over the table)", f"=SUM({a('K')})", auc, "0.000", "Chance = 0.5, perfect = 1")
    bf = b.row("Threshold with the best F1", f"=INDEX({a('A')},MATCH(MAX({a('I')}),{a('I')},0))", best_f1_t, "0.00")
    tr = b.row("Largest T that still reaches the recall target", f"=MAX({a('L')})", t_recall, "0.00")
    b.row("FPR at that threshold", f"=INDEX({a('H')},MATCH({b.local(tr)},{a('A')},0))", fpr_at_recall, "0.0000")
    bc = b.row("Threshold with the lowest total cost", f"=INDEX({a('A')},MATCH(MIN({a('J')}),{a('J')},0))", best_cost_t, "0.00")
    b.row("Total cost at the chosen T (yellow)", f"={b.local(cfn)}*{b.local(fnc)}+{b.local(cfp)}*{b.local(fpc)}", cost_def, "0")
    b.row("Total cost at the cheapest T", f"=MIN({a('J')})", float(sw.cost.min()), "0")

    # charts on the sweep table: ROC (scatter) and precision/recall/F1 vs T (line)
    ch = ScatterChart()
    ch.title, ch.style = "ROC curve (each point = one threshold)", 13
    ch.x_axis.title, ch.y_axis.title = "False-positive rate", "Recall (TPR)"
    ch.x_axis.delete = False
    ch.y_axis.delete = False
    xs = Reference(b.an, min_col=8, min_row=t0, max_row=t1)
    ys = Reference(b.an, min_col=7, min_row=t0, max_row=t1)
    ser = Series(ys, xs, title="ROC")
    ser.marker.symbol = "circle"
    ser.marker.size = 5
    ch.series.append(ser)
    ch.width, ch.height = 14, 9
    b.an.add_chart(ch, "N4")
    b.line_chart_from_table("Precision, recall and F1 by threshold", 1, [6, 7, 9], t0, t1 - 1, anchor="N24", x_title="T")

    b.section("5. Base-rate fallacy: precision depends on how rare faults are")
    rows, exp = [], {}
    r0 = b.next_row + 1
    for i, pi in enumerate(PREV):
        r = r0 + i
        rows.append([pi, f"={b.local(recc)}*A{r}/({b.local(recc)}*A{r}+{b.local(fprc)}*(1-A{r}))",
                     f"=1000*A{r}*{b.local(recc)}", f"=1000*(1-A{r})*{b.local(fprc)}"])
        exp.update({(i, 1): rec * pi / (rec * pi + fpr * (1 - pi)), (i, 2): 1000 * pi * rec, (i, 3): 1000 * (1 - pi) * fpr})
    q0, q1 = b.table(["Prevalence", "Precision (PPV)", "True alarms / 1000 readings", "False alarms / 1000 readings"], rows,
                     fmt={0: "0.0%", 1: "0.0%", 2: "0.00", 3: "0.00"}, expect=exp)
    ppv_lo = rec * 0.005 / (rec * 0.005 + fpr * 0.995)

    ep_txt = ", ".join(f"{e['delay']}" for e in ep_rows)
    undetected = [i + 1 for i, e in enumerate(ep_rows) if not e["detected"]]
    b.answers([
        ("Robust sigma of the residuals and the share of fault readings", f"={sigc}",
         f"sigma-hat = {sig:.3f} C (1.4826 x median |temp - set-point|). {P} of {n} readings ({P / n:.1%}) are labelled faults in {n_ep} episodes."),
        (f"Confusion matrix at T = {T_DEF:g}", f"={tpc}",
         f"TP = {tp}, FP = {fp}, FN = {fn}, TN = {tn} (they add up to {n})."),
        ("Precision, recall, false-positive rate, F1", f"={precc}",
         f"Precision {prec:.3f}, recall {rec:.3f}, FPR {fpr:.4f}, F1 {f1:.3f}. An FPR of only {fpr:.1%} still means {fp} false alarms "
         f"against {tp} real ones, because healthy readings outnumber faulty ones {N / P:.0f} to 1."),
        ("Fault episodes: how many are detected, and what is the mean delay?", f"={ndet}",
         f"{sum(e['detected'] for e in ep_rows)} of {n_ep} episodes are detected; delays before the first alarm (hours, per episode): {ep_txt} "
         f"(a never-detected episode shows its full length). Mean delay of detected episodes: {np.mean(det_delays):.2f} h. "
         f"Reading-level recall is only {rec:.2f}, yet the episode-level view is far better: faults ramp up, so their first hours are small and "
         f"hide in the noise while the later hours are caught."
         + (f" Episode(s) {', '.join(map(str, undetected))} never trip the alarm: small offsets hide in the noise." if undetected else "")),
        ("False alarms per month and the average spacing between them", f"={arl0}",
         f"{fp} false alarms in 720 hours: one every {(fp + tn) / fp:.0f} hours (ARL0), i.e. about {fp / 30:.1f} per day."),
        (f"Which threshold maximises F1, and which is the largest T with recall >= {TARGET_RECALL:.0%} (and its FPR)?", f"={bf}",
         f"Best F1 = {sw.f1.max():.3f} at T = {best_f1_t:g}. Recall >= {TARGET_RECALL:.0%} needs T <= {t_recall:g}, where the FPR is {fpr_at_recall:.3f}."),
        ("ROC AUC from the sweep table", f"={auc_c}",
         f"AUC = {auc:.3f}: a random fault reading scores higher than a random healthy one with that probability. AUC ignores prevalence, "
         f"so it can look excellent while precision is poor."),
        (f"Cheapest threshold with a missed fault costing {C_FN} and a false alarm {C_FP}", f"={bc}",
         f"T = {best_cost_t:g} gives cost {sw.cost.min():.0f}, versus {cost_def} at T = {T_DEF:g}. Expensive misses push the threshold down; "
         f"change the yellow costs to move it."),
        ("Precision if faults were only 0.5 % of readings", f"=Analysis!B{q0 + 1}",
         f"PPV = {ppv_lo:.1%} with the same recall ({rec:.2f}) and FPR ({fpr:.4f}): at that rarity most alarms are false even though the "
         f"detector itself did not change. At 20 % prevalence it would be {rec * 0.2 / (rec * 0.2 + fpr * 0.8):.1%}."),
        ("Limitations of this evaluation", "see text",
         "Labels are perfect here; real fault logs are late, incomplete and sometimes wrong. The threshold is tuned on the same data it is evaluated "
         "on, so the numbers are optimistic (use a held-out period). Counting readings rewards long episodes; the operational unit is the episode. "
         "A set-point model that is wrong at transitions creates the false alarms that no threshold can remove."),
    ])

    # ------------------------------------------------------------------- grafana
    d = Dash("stats-29-detection-performance", "29 · False alarms and detection performance",
             "Confusion matrix, precision/recall/F1, threshold sweep, ROC and the base-rate effect for a labelled temperature monitor.",
             df.rename(columns={"timestamp": "time"}), "time")
    d.stat("Counts at T = 3 (readings)", {"TP": tp, "FP": fp, "FN": fn, "TN": tn}, "Confusion matrix of alarm vs fault label.",
           decimals=0, w=10)
    d.stat("Rates at T = 3", {"precision": prec, "recall": rec, "false-positive rate": fpr, "F1": f1},
           "Precision and recall disagree because healthy readings vastly outnumber faulty ones.", unit="percentunit", decimals=1, w=14)
    ts = pd.DataFrame({"time": df["timestamp"], "score": score, "threshold": T_DEF,
                       "fault reading": np.where(lab == 1, score, np.nan),
                       "false alarm": np.where((flag == 1) & (lab == 0), score, np.nan)})
    d.timeseries("Anomaly score over the month", ts, "Score = |temp - set-point| / robust sigma. Orange: labelled faults. Red: false alarms.",
                 points=["fault reading", "false alarm"], dashed=["threshold"],
                 colors={"score": "#9AA5B1", "threshold": "#E15759", "fault reading": "#F28E2B", "false alarm": "#E15759"}, w=24)
    roc = pd.DataFrame({"fpr": sw.fpr, "recall": sw.rec, "chance": sw.fpr})
    d.xy("ROC curve", roc, "fpr", ["recall", "chance"], "Each point is one threshold; the diagonal is a coin flip. Moving along the curve trades "
         "false alarms for detections.", lines=["recall", "chance"])
    pr = sw[(sw["thr"] >= 0.5) & (sw["thr"] <= 6)]
    prd = pd.DataFrame({"T": pr["thr"], "precision": pr.prec, "recall": pr.rec, "F1": pr.f1})
    d.xy("Precision, recall and F1 by threshold", prd, "T", ["precision", "recall", "F1"],
         "Raising T buys precision and costs recall; F1 peaks in between.", lines=["precision", "recall", "F1"])
    sel = [2.0, 2.5, 3.0, 3.5, 4.0, 5.0]
    bar = pd.DataFrame({"T": [f"{t:.1f}" for t in sel], "true alarms (TP)": [counts(score, lab, t)[0] for t in sel],
                        "false alarms (FP)": [counts(score, lab, t)[1] for t in sel], "missed (FN)": [counts(score, lab, t)[2] for t in sel]})
    d.bars("Alarms by threshold", bar, "The cost-optimal threshold depends on the price of a miss versus a false alarm.", w=12)
    ppv = pd.DataFrame({"prevalence": ["0.1%", "0.5%", "2%", "5.3% (this data)", "20%"],
                        "precision": [rec * p / (rec * p + fpr * (1 - p)) for p in [0.001, 0.005, 0.02, P / n, 0.2]]})
    d.bars("Base-rate effect: precision at T = 3", ppv, "Same detector, same recall and FPR; only the prevalence changes.",
           unit="percentunit", w=12)
    et = pd.DataFrame({"episode": range(1, n_ep + 1), "start": [e["start"].strftime("%m-%d %H:%M") for e in ep_rows],
                       "hours": [e["length"] for e in ep_rows], "alarm readings": [e["flagged"] for e in ep_rows],
                       "delay (h)": [e["delay"] for e in ep_rows], "detected": [e["detected"] for e in ep_rows]})
    d.table("Fault episodes and detection delay (T = 3)", et, "delay = faulty hours before the first alarm.", w=24, h=10)
    d.save(out)

    md(out / "theory.md", THEORY)
    md(out / "task.md", TASK.replace("@CFN@", str(C_FN)).replace("@CFP@", str(C_FP)))
    return b


THEORY = r"""
# Theory: false alarms and detection performance

## Why an alert rule must be judged on both errors

Every detector can be made to catch all faults by alarming all the time, or to never raise a false alarm by never alarming. A rule is only
useful for the point it sets between those extremes. Judging it by "it caught the fault" or "it rarely fires" alone hides half of the
story and leads to alert fatigue (people stop reacting) or silent failures. To choose a threshold responsibly you need labelled history, a
vocabulary for the four outcomes, and a way to put prices on them.

## The confusion matrix

Compare the alarm with the truth for every reading:

| | fault | healthy |
|---|---|---|
| **alarm** | TP (true positive) | FP (false alarm) |
| **no alarm** | FN (miss) | TN |

Definitions (all conditional proportions):

$$\text{precision}=\frac{TP}{TP+FP},\qquad \text{recall (TPR)}=\frac{TP}{TP+FN},\qquad \text{FPR}=\frac{FP}{FP+TN},\qquad
F_1=\frac{2\,\text{precision}\cdot\text{recall}}{\text{precision}+\text{recall}} .$$

Recall and FPR condition on the **truth** (how the detector treats faults and healthy readings); precision conditions on the **alarm**
(how trustworthy an alert is). Worked example with $TP=8,\,FP=4,\,FN=2,\,TN=86$: precision $=8/12=0.667$, recall $=8/10=0.800$,
FPR $=4/90=0.044$, $F_1=2(0.667)(0.8)/(1.467)=0.727$. $F_1$ is a harmonic mean, so it is low whenever either component is low; it
ignores TN completely.

## Sweeping the threshold

For a score $s_t$ and threshold $T$ the detector alarms when $s_t\ge T$. Raising $T$ lowers FP and TP together. Evaluating many
thresholds traces:

- the **ROC curve**: recall against FPR. The diagonal is a coin flip; area under the curve (AUC) is the probability that a random fault
  scores higher than a random healthy reading. AUC is independent of the threshold and of prevalence.
- the **precision-recall curve**: preferable when faults are rare, because it shows what fraction of alarms are real.

The threshold is a decision, not an estimate: pick it by expected cost, $\text{cost}(T)=c_{FN}\,FN(T)+c_{FP}\,FP(T)$, or by a constraint such as
"recall at least 80 %" or "at most one false alarm per day".

## Base-rate fallacy

If faults are rare, even a detector with a small FPR produces mostly false alarms. By Bayes' theorem
([conditional probability](../../notes/probability/bayes_theorem.md))

$$\text{precision}=\frac{\text{recall}\cdot\pi}{\text{recall}\cdot\pi+\text{FPR}\cdot(1-\pi)},\qquad \pi=\text{prevalence}.$$

Worked example: recall 0.90, FPR 0.02, $\pi=1\,\%$. Per 1000 readings there are $1000\cdot0.01\cdot0.9=9$ true alarms and
$1000\cdot0.99\cdot0.02=19.8$ false ones, so precision is $9/28.8=31\,\%$. The same detector at $\pi=20\,\%$ has precision 92 %. Judge a
detector in the prevalence in which it will run; precision and F1 do not transfer, but recall and FPR do.

## Time-series specifics: ARL and delay

Sensors produce a stream, so two operational quantities matter more than FPR per reading:

- **ARL0**, the average run length between false alarms, $\approx 1/\text{FPR}$ readings when alarms are independent. An FPR of 1 % per hourly
  reading is one false alarm every four days.
- **Detection delay**, the number of faulty readings before the first alarm in an episode. Evaluate by **episode** (was the incident
  caught, and how late?) as well as by reading; a 6-hour fault with 5 alarms counts once as an incident but five times in TP.

Delay and ARL0 trade off exactly as in [lesson 27](../27-change-point-detection/theory.md): lowering the false-alarm rate lengthens the delay.

## Assumptions and pitfalls

1. **Labels are the ceiling.** Late, partial or wrong labels bias every metric; an unlabelled real fault counts as a false alarm.
2. **Tuning on the evaluation data is optimistic.** Choose $T$ on one period and report on another
   ([backtesting, lesson 24](../24-backtesting-and-forecast-accuracy/theory.md)).
3. **Prevalence shifts** (a new line, a bad batch) change precision without any change to the detector.
4. **Reading-level vs episode-level metrics** answer different questions; state which one you report.
5. **Accuracy is a trap**: with 5 % faults, "never alarm" has 95 % accuracy and recall 0.
6. **The score model matters more than the threshold.** If the set-point model is wrong at transitions the false alarms come in at specific hours;
   see [lesson 28](../28-time-series-anomaly-detection/theory.md).
7. **Alarms correlate**: consecutive hours are not independent, so ARL0 from a rate is only a rough guide.

## Related notes

- [Outlier detection](../04-outlier-detection/theory.md), [statistical process control](../26-statistical-process-control/theory.md)
- [Permutation tests](../18-permutation-tests/theory.md) for judging whether a difference in detection rate between two rules is real
- Repo notes: [Bayes' theorem](../../notes/probability/bayes_theorem.md)
"""

TASK = r"""
# Task: false alarms and detection performance

## Scenario

A furnace-zone temperature is logged every hour and compared with the controller's set-point (70 C by day, 66 C at night). An
alarm raises a ticket for a technician. Operations kept a log of confirmed fault periods during June and now ask three things:
how good is a "3-sigma" alert rule, what happens if you move the threshold, and whether the rule would still be useful in a month
when faults are much rarer. A missed fault reading costs about @CFN@ times as much as a false alarm.

## Data

`data.csv` - 720 hourly readings (2026-06-01 00:00 to 2026-06-30 23:00).

| column | meaning |
|---|---|
| `timestamp` | hour of the reading |
| `temp_c` | measured zone temperature, degrees Celsius |
| `setpoint_c` | controller set-point for that hour, degrees Celsius |
| `is_fault` | 1 if the hour belongs to a confirmed fault period in the operations log, else 0 |

Define the **score** as $|temp - setpoint|$ divided by $\hat\sigma = 1.4826\times\mathrm{median}|temp - setpoint|$ (robust, so the faults do not inflate it);
the alarm rule is score $\ge T$.

## Questions

Work in a spreadsheet (import `data.csv`), then compare with `solution.xlsx`.

1. Compute $\hat\sigma$ and the share of readings labelled as faults.
2. With $T=3$ build the confusion matrix (TP, FP, FN, TN).
3. Compute precision, recall, false-positive rate and F1. Why is precision so much lower than the FPR suggests?
4. The fault readings form consecutive episodes. How many episodes are detected (at least one alarm), and what is the mean detection delay
   (faulty hours before the first alarm)?
5. How many false alarms are there in the month and what is the average spacing between them (ARL0, in hours)?
6. Build a table over thresholds $0, 0.5, 0.75, \dots, 6$ and $99$. Which threshold maximises F1? Which is the largest threshold that still gives recall $\ge 80\%$, and what is the FPR there?
7. Estimate the area under the ROC curve with the trapezoid rule over your table.
8. Add a cost column ($@CFN@\times FN + @CFP@\times FP$). Which threshold is cheapest, and by how much does it beat $T=3$?
9. Suppose next month only 0.5 % of readings are faulty but the detector's recall and FPR at $T=3$ stay the same. What is the precision?
10. *Limitations:* give two reasons why these metrics may be too optimistic or misleading for deciding on the production threshold.

## Grafana

Import `grafana/dashboard.json` (see `../grafana/README.md`; no data-source setup is needed).

- In "Anomaly score over the month", which red dots (false alarms) cluster, and what do they have in common?
- Read the knee of the "ROC curve": what recall do you get at about 1 % FPR?
- In "Alarms by threshold", at which threshold do the false alarms start to drop below the true alarms?

## Deliverable

A short note (5-8 lines) with three named parts: **Threshold** (your choice and why: cost, recall target or false-alarm budget),
**Expected behaviour** (precision, recall, false alarms per month, typical delay) and **Caveats** (prevalence, labels, optimistic tuning).
"""
