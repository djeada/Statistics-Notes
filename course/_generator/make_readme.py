#!/usr/bin/env python3
"""Regenerate course/README.md (the lesson index) from the lesson modules."""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
COURSE = HERE.parent
rows = []
for f in sorted((HERE / "lessons").glob("l[0-9][0-9]_*.py")):
    spec = importlib.util.spec_from_file_location(f.stem, f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    rows.append((int(f.stem[1:3]), m.MODULE, m.TITLE, m.SLUG, getattr(m, "DATASET", "")))

lines = ["| # | Lesson | Theory | Task | Data | Solution | Grafana | Dataset |", "|---:|---|---|---|---|---|---|---|"]
cur = None
for n, module, title, slug, ds in rows:
    if module != cur:
        lines.append(f"| | **{module}** | | | | | | |")
        cur = module
    lines.append(f"| {n:02d} | {title} | [theory]({slug}/theory.md) | [task]({slug}/task.md) | [csv]({slug}/data.csv) | "
                 f"[xlsx]({slug}/solution.xlsx) | [json]({slug}/grafana/dashboard.json) | {ds} |")

srows = []
for f in sorted((HERE / "lessons").glob("s[0-9][0-9]_*.py")):
    spec = importlib.util.spec_from_file_location(f.stem, f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    srows.append((int(f.stem[1:3]), m.TITLE, m.SLUG, getattr(m, "DATASET", "")))
slines = ["| # | Lesson | Theory | Task | Data | Solution | Dataset |", "|---:|---|---|---|---|---|---|"]
for n, title, slug, ds in srows:
    slines.append(f"| S{n} | {title} | [theory]({slug}/theory.md) | [task]({slug}/task.md) | [csv]({slug}/data.csv) | "
                  f"[xlsx]({slug}/solution.xlsx) | {ds} |")

text = (COURSE / "README.template.md").read_text().replace("{{TABLE}}", "\n".join(lines)).replace("{{SHEETS_TABLE}}", "\n".join(slines))
(COURSE / "README.md").write_text(text)
print(f"README.md written ({len(rows)} lessons + {len(srows)} spreadsheet lessons)")
