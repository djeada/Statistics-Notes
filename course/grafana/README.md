# Grafana for the course

Every lesson has `grafana/dashboard.json`. The dashboards are **self-contained**: the lesson's data is embedded in the
panel queries (Grafana's built-in *TestData* data source, scenario `csv_content`). You do not need Prometheus, a CSV
plugin or any ingestion step, and the panels are never empty.

The panels show the **solved analysis** (fitted lines, control limits, rolling statistics, flagged points...) computed
from the lesson's `data.csv`. The statistics themselves are what you compute in the spreadsheet; Grafana is where you
see them and where the "how would I monitor this?" questions in each `task.md` are answered.

## Option 1 - everything at once (recommended)

```bash
cd course/grafana
docker compose up
```

Open <http://localhost:3000>. All 30 dashboards are provisioned automatically (anonymous viewer access is on; sign in as
`admin` / `admin` to edit panels). Search for the lesson number, e.g. `03 · Percentiles and extreme values`.

## Option 2 - import into your own Grafana (10.x or 11.x)

1. Add a data source of type **TestData** with UID `course-testdata` (Connections → Add new connection → TestData).
2. Dashboards → New → Import → upload the lesson's `grafana/dashboard.json`.

If you keep a different UID, replace `course-testdata` in the JSON.

## Working with the dashboards

- The time range is fixed to the period covered by the data; change it with the time picker if you zoom in.
- Hover a panel title for a short description. *Edit → Query* shows the embedded CSV: replace it with your own data or
  point the panel at a real data source to monitor live metrics with the same statistics.
- `_generator/check_grafana.py` runs every panel query through a live Grafana and fails on empty panels.
