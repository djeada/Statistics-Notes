"""Shared helpers for building the 30-lesson applied statistics course.

Every lesson module in ``lessons/`` calls these helpers to produce, in its own folder:

    theory.md            what the method is and why it works
    task.md              the exercise (scenario, dataset, questions, deliverable)
    data.csv             the dataset (raw columns only)
    solution.xlsx        the solved workbook: Data / Analysis / Answers sheets with live formulas
    grafana/dashboard.json   a self-contained dashboard (data is embedded, no data source setup)

Every number the workbook computes with a formula is registered as a *check* against a value
computed independently in Python.  ``build.py`` recalculates the workbook in LibreOffice and
fails if any cell disagrees, so the workbook cannot silently contain a wrong formula.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference, ScatterChart, Series
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

COURSE_DIR = Path(__file__).resolve().parent.parent

HEADER_FILL = PatternFill("solid", fgColor="1F3A5F")
HEADER_FONT = Font(bold=True, color="FFFFFF")
SECTION_FILL = PatternFill("solid", fgColor="DCE6F2")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")  # yellow = an assumption you may change


# --------------------------------------------------------------------------- csv
def write_csv(out: Path, df: pd.DataFrame) -> None:
    """Write ``data.csv``.  Datetime columns are written as ISO-8601 (``2026-01-01``)."""
    d = df.copy()
    for c in d.columns:
        if pd.api.types.is_datetime64_any_dtype(d[c]):
            d[c] = d[c].dt.strftime("%Y-%m-%d" if (d[c].dt.normalize() == d[c]).all() else "%Y-%m-%dT%H:%M:%S")
    d.to_csv(out / "data.csv", index=False)


# ------------------------------------------------------------------------- workbook
class Book:
    """An xlsx with ``Data`` (raw rows), ``Analysis`` (formulas) and ``Answers`` sheets.

    Usage::

        b = Book(df)                          # writes the Data sheet
        p95 = b.row("P95", f"=PERCENTILE({b.rng('Latency_ms')},0.95)", expect=float(np.percentile(...)))
        b.save(out / "solution.xlsx")

    ``expect`` registers a check; ``b.checks`` is verified after LibreOffice recalculation.
    """

    def __init__(self, df: pd.DataFrame, title: str, subtitle: str = ""):
        self.df = df.reset_index(drop=True)
        self.n = len(self.df)
        self.wb = Workbook()
        self.data = self.wb.active
        self.data.title = "Data"
        self.an = self.wb.create_sheet("Analysis")
        self.ans = self.wb.create_sheet("Answers")
        self.checks: list[tuple[str, str, float]] = []  # (sheet!cell, label, expected)
        self._cols: dict[str, str] = {}
        self._write_data()
        self.an["A1"] = title
        self.an["A1"].font = Font(bold=True, size=14)
        if subtitle:
            self.an["A2"] = subtitle
            self.an["A2"].font = Font(italic=True, color="555555")
        self.an.column_dimensions["A"].width = 44
        for c in "BCDEFGH":
            self.an.column_dimensions[c].width = 16
        self._r = 4  # next free row in Analysis

    # -- Data sheet ---------------------------------------------------------
    def _write_data(self) -> None:
        for j, name in enumerate(self.df.columns, start=1):
            c = self.data.cell(row=1, column=j, value=str(name))
            c.fill, c.font = HEADER_FILL, HEADER_FONT
            L = get_column_letter(j)
            self._cols[str(name)] = L
            self.data.column_dimensions[L].width = max(12, len(str(name)) + 2)
        for i, row in enumerate(self.df.itertuples(index=False), start=2):
            for j, v in enumerate(row, start=1):
                if isinstance(v, pd.Timestamp):
                    v = v.to_pydatetime()
                    fmt = "yyyy-mm-dd" if (v.hour, v.minute) == (0, 0) else "yyyy-mm-dd hh:mm"
                    cell = self.data.cell(row=i, column=j, value=v)
                    cell.number_format = fmt
                elif isinstance(v, (np.integer,)):
                    self.data.cell(row=i, column=j, value=int(v))
                elif isinstance(v, (np.floating, float)):
                    self.data.cell(row=i, column=j, value=None if math.isnan(v) else float(v))
                else:
                    self.data.cell(row=i, column=j, value=v)
        self.data.freeze_panes = "A2"

    def col(self, name: str) -> str:
        """Column letter of a Data column, e.g. ``b.col('Latency_ms') -> 'C'``."""
        return self._cols[name]

    def rng(self, name: str, first: int = 2, last: int | None = None, absolute: bool = True) -> str:
        """``Data!$C$2:$C$121`` for a column (rows are Excel rows; header is row 1)."""
        last = last or self.n + 1
        L = self.col(name)
        return f"Data!${L}${first}:${L}${last}" if absolute else f"Data!{L}{first}:{L}{last}"

    def ref(self, name: str, row: int) -> str:
        """``Data!C7`` for one cell."""
        return f"Data!{self.col(name)}{row}"

    def add_column(self, name: str, fn, expected=None, fmt: str = "0.000", first_row: int = 2) -> str:
        """Add a formula column to the Data sheet.

        ``fn(row) -> formula string`` is called for each Excel row from ``first_row`` to the end.
        ``expected`` is a pandas Series / array of the same length as the data (NaN = leave blank);
        every non-NaN value becomes a check.  Returns the column letter.
        """
        j = self.data.max_column + 1
        L = get_column_letter(j)
        c = self.data.cell(row=1, column=j, value=name)
        c.fill, c.font = HEADER_FILL, HEADER_FONT
        self.data.column_dimensions[L].width = max(12, len(name) + 2)
        self._cols[name] = L
        exp = None if expected is None else np.asarray(expected, dtype=float)
        for r in range(first_row, self.n + 2):
            if exp is not None and np.isnan(exp[r - 2]):
                continue
            cell = self.data.cell(row=r, column=j, value=fn(r))
            cell.number_format = fmt
            if exp is not None:
                self.checks.append((f"Data!{L}{r}", f"{name} row {r}", float(exp[r - 2])))
        return L

    # -- Analysis sheet -----------------------------------------------------
    def section(self, text: str) -> None:
        self._r += 1
        for col in range(1, 5):
            self.an.cell(row=self._r, column=col).fill = SECTION_FILL
        self.an.cell(row=self._r, column=1, value=text).font = Font(bold=True)
        self._r += 1

    def row(self, label: str, formula, expect=None, fmt: str = "0.000", note: str = "", is_input: bool = False,
            tol: float | None = None) -> str:
        """Add ``label | value-or-formula | note`` to Analysis; returns the absolute cell, e.g. ``Analysis!$B$7``.

        ``expect`` (a number) registers a check.  ``is_input=True`` highlights an editable assumption.
        """
        r = self._r
        self.an.cell(row=r, column=1, value=label)
        cell = self.an.cell(row=r, column=2, value=formula)
        cell.number_format = fmt
        if is_input:
            cell.fill = INPUT_FILL
        if note:
            self.an.cell(row=r, column=3, value=note).font = Font(italic=True, color="666666")
        if expect is not None:
            self.checks.append((f"Analysis!B{r}", label, float(expect)))
        self._r += 1
        return f"Analysis!$B${r}"

    def local(self, cell_abs: str) -> str:
        """Strip the sheet prefix: ``Analysis!$B$7 -> $B$7`` (for formulas written on the Analysis sheet)."""
        return cell_abs.split("!")[-1]

    def table(self, headers: list[str], rows: list[list], fmt: dict[int, str] | None = None,
              expect: dict[tuple[int, int], float] | None = None) -> tuple[int, int]:
        """Write a small table in Analysis starting at the next free row.

        ``rows`` cells may be values or formulas. ``fmt`` maps column index -> number format.
        ``expect`` maps (row_index, col_index) (0-based within ``rows``) -> expected number.
        Returns (first_data_row, last_data_row).
        """
        r0 = self._r
        for j, h in enumerate(headers, start=1):
            c = self.an.cell(row=r0, column=j, value=h)
            c.fill, c.font = HEADER_FILL, HEADER_FONT
            c.alignment = Alignment(horizontal="center", wrap_text=True)
        for i, vals in enumerate(rows):
            for j, v in enumerate(vals, start=1):
                c = self.an.cell(row=r0 + 1 + i, column=j, value=v)
                if fmt and (j - 1) in fmt:
                    c.number_format = fmt[j - 1]
        for (i, j), e in (expect or {}).items():
            L = get_column_letter(j + 1)
            self.checks.append((f"Analysis!{L}{r0 + 1 + i}", f"table[{i},{j}]", float(e)))
        self._r = r0 + len(rows) + 2
        return r0 + 1, r0 + len(rows)

    def skip(self, n: int = 1) -> None:
        self._r += n

    @property
    def next_row(self) -> int:
        return self._r

    # -- charts -------------------------------------------------------------
    def _place(self, chart, anchor: str | None, ws) -> None:
        chart.width, chart.height = 18, 9
        ws.add_chart(chart, anchor or "F4")

    def line_chart(self, title: str, x_name: str, y_names: list[str], anchor: str | None = None,
                   y_title: str = "", ws=None, last: int | None = None, first: int = 2) -> None:
        """Line chart of Data columns (rows ``first..last``) against the ``x_name`` column."""
        ch = LineChart()
        ch.title, ch.y_axis.title = title, y_title
        last = last or self.n + 1
        for nm in y_names:
            j = list(self._cols).index(nm) + 1
            ch.add_data(Reference(self.data, min_col=j, min_row=first - 1, max_row=last), titles_from_data=True)
        xj = list(self._cols).index(x_name) + 1
        ch.set_categories(Reference(self.data, min_col=xj, min_row=first, max_row=last))
        ch.x_axis.number_format = "mmm-dd" if "date" in x_name.lower() or "time" in x_name.lower() else "General"
        ch.x_axis.delete = False
        ch.y_axis.delete = False
        for s in ch.series:
            s.smooth = False
            s.marker.symbol = "none"
        self._place(ch, anchor, ws or self.an)

    def scatter_chart(self, title: str, x_name: str, y_names: list[str], anchor: str | None = None,
                      x_title: str = "", y_title: str = "", lines: list[str] | None = None, ws=None,
                      last: int | None = None, first: int = 2) -> None:
        """Scatter chart; names in ``lines`` are drawn as lines (e.g. a fitted curve), others as markers."""
        ch = ScatterChart()
        ch.title, ch.style = title, 13
        ch.x_axis.title, ch.y_axis.title = x_title or x_name, y_title
        ch.x_axis.delete = False
        ch.y_axis.delete = False
        last = last or self.n + 1
        xj = list(self._cols).index(x_name) + 1
        xref = Reference(self.data, min_col=xj, min_row=first, max_row=last)
        for nm in y_names:
            j = list(self._cols).index(nm) + 1
            s = Series(Reference(self.data, min_col=j, min_row=first - 1, max_row=last), xref, title_from_data=True)
            if lines and nm in lines:
                s.marker.symbol = "none"
            else:
                s.marker.symbol = "circle"
                s.marker.size = 5
                s.graphicalProperties.line.noFill = True
            ch.series.append(s)
        self._place(ch, anchor, ws or self.an)

    def bar_chart_from_table(self, title: str, cat_col: int, val_cols: list[int], first_row: int, last_row: int,
                             anchor: str | None = None, x_title: str = "", y_title: str = "") -> None:
        """Column chart from a table already written on the Analysis sheet (1-based column indexes)."""
        ch = BarChart()
        ch.type = "col"
        ch.title, ch.x_axis.title, ch.y_axis.title = title, x_title, y_title
        ch.x_axis.delete = False
        ch.y_axis.delete = False
        for j in val_cols:
            ch.add_data(Reference(self.an, min_col=j, min_row=first_row - 1, max_row=last_row), titles_from_data=True)
        ch.set_categories(Reference(self.an, min_col=cat_col, min_row=first_row, max_row=last_row))
        self._place(ch, anchor, self.an)

    def line_chart_from_table(self, title: str, cat_col: int, val_cols: list[int], first_row: int, last_row: int,
                              anchor: str | None = None, x_title: str = "", y_title: str = "") -> None:
        ch = LineChart()
        ch.title, ch.x_axis.title, ch.y_axis.title = title, x_title, y_title
        ch.x_axis.delete = False
        ch.y_axis.delete = False
        for j in val_cols:
            ch.add_data(Reference(self.an, min_col=j, min_row=first_row - 1, max_row=last_row), titles_from_data=True)
        ch.set_categories(Reference(self.an, min_col=cat_col, min_row=first_row, max_row=last_row))
        for s in ch.series:
            s.smooth = False
            s.marker.symbol = "none"
        self._place(ch, anchor, self.an)

    # -- Answers sheet + save -----------------------------------------------
    def answers(self, items: list[tuple[str, str, str]]) -> None:
        """``items`` = (question, value-formula-or-text, interpretation). Matches the task.md question numbers."""
        for j, h in enumerate(["#", "Question (see task.md)", "Value", "Interpretation"], start=1):
            c = self.ans.cell(row=1, column=j, value=h)
            c.fill, c.font = HEADER_FILL, HEADER_FONT
        self.ans.column_dimensions["A"].width = 5
        self.ans.column_dimensions["B"].width = 52
        self.ans.column_dimensions["C"].width = 16
        self.ans.column_dimensions["D"].width = 90
        for i, (q, v, interp) in enumerate(items, start=1):
            self.ans.cell(row=i + 1, column=1, value=i)
            self.ans.cell(row=i + 1, column=2, value=q).alignment = Alignment(wrap_text=True, vertical="top")
            c = self.ans.cell(row=i + 1, column=3, value=v)
            c.number_format = "0.000"
            c.alignment = Alignment(vertical="top")
            self.ans.cell(row=i + 1, column=4, value=interp).alignment = Alignment(wrap_text=True, vertical="top")

    def save(self, path: Path) -> None:
        self.wb.save(path)


# ----------------------------------------------------------------------- grafana
GRAFANA_DS = {"type": "grafana-testdata-datasource", "uid": "course-testdata"}
PALETTE = ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F", "#EDC948", "#B07AA1", "#9C755F"]


def _csv(df: pd.DataFrame, time_col: str | None) -> str:
    d = df.copy()
    if time_col and time_col in d.columns:
        d[time_col] = pd.to_datetime(d[time_col]).dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    return d.to_csv(index=False, float_format="%.6g")


class Dash:
    """Builds a Grafana dashboard whose panels read CSV that is embedded in the JSON (TestData ``csv_content``).

    The dashboard works as soon as it is imported; no Prometheus, no files to mount, no plugin.
    ``time_range`` is fixed to the data so the panels are not empty.

    Panel methods take a DataFrame holding only the columns to show.  The first column is the x-axis.
    """

    def __init__(self, uid: str, title: str, description: str, df_for_range: pd.DataFrame | None = None,
                 time_col: str = "time"):
        self.uid, self.title, self.description = uid, title, description
        self.panels: list[dict] = []
        self.time_col = time_col
        self._y = 0
        self._x = 0
        self._id = 1
        self.range = None
        if df_for_range is not None:
            t = pd.to_datetime(df_for_range[time_col])
            pad = (t.max() - t.min()) * 0.01
            self.range = ((t.min() - pad).strftime("%Y-%m-%dT%H:%M:%SZ"), (t.max() + pad).strftime("%Y-%m-%dT%H:%M:%SZ"))

    def _add(self, panel: dict, w: int = 12, h: int = 9) -> None:
        if self._x + w > 24:
            self._x, self._y = 0, self._y + h
        panel["id"] = self._id
        panel["gridPos"] = {"x": self._x, "y": self._y, "w": w, "h": h}
        self._id += 1
        self._x += w
        self.panels.append(panel)

    def _target(self, df: pd.DataFrame, time_col: str | None) -> list[dict]:
        return [{"refId": "A", "datasource": GRAFANA_DS, "scenarioId": "csv_content", "csvContent": _csv(df, time_col)}]

    def text(self, md: str, w: int = 24, h: int = 4, title: str = "") -> None:
        self._add({"type": "text", "title": title, "options": {"mode": "markdown", "content": md}}, w, h)

    def timeseries(self, title: str, df: pd.DataFrame, description: str = "", points: list[str] | None = None,
                   dashed: list[str] | None = None, bars: list[str] | None = None, unit: str = "short",
                   w: int = 12, h: int = 9, ymin: float | None = None, stack_fill: list[tuple[str, str]] | None = None,
                   colors: dict[str, str] | None = None) -> None:
        """Time series. ``points``: columns drawn as dots only (e.g. flagged anomalies); ``dashed``: dashed lines;
        ``bars``: drawn as bars. Empty cells in a column are gaps."""
        overrides = []
        cols = [c for c in df.columns if c != self.time_col]
        colors = colors or {}
        for i, c in enumerate(cols):
            props = [{"id": "color", "value": {"mode": "fixed", "fixedColor": colors.get(c, PALETTE[i % len(PALETTE)])}}]
            if points and c in points:
                props += [{"id": "custom.drawStyle", "value": "points"}, {"id": "custom.pointSize", "value": 8},
                          {"id": "custom.showPoints", "value": "always"}]
            elif bars and c in bars:
                props += [{"id": "custom.drawStyle", "value": "bars"}, {"id": "custom.fillOpacity", "value": 60}]
            elif dashed and c in dashed:
                props += [{"id": "custom.lineStyle", "value": {"fill": "dash", "dash": [10, 10]}}]
            overrides.append({"matcher": {"id": "byName", "options": c}, "properties": props})
        defaults = {"unit": unit, "custom": {"drawStyle": "line", "lineWidth": 2, "fillOpacity": 0, "showPoints": "never",
                                             "spanNulls": False}}
        if ymin is not None:
            defaults["min"] = ymin
        self._add({"type": "timeseries", "title": title, "description": description, "datasource": GRAFANA_DS,
                   "targets": self._target(df, self.time_col),
                   "fieldConfig": {"defaults": defaults, "overrides": overrides},
                   "options": {"legend": {"displayMode": "list", "placement": "bottom"}, "tooltip": {"mode": "multi"}}},
                  w, h)

    def xy(self, title: str, df: pd.DataFrame, x: str, ys: list[str], description: str = "", lines: list[str] | None = None,
           w: int = 12, h: int = 9) -> None:
        """Scatter plot of ``ys`` against numeric column ``x``; names in ``lines`` are drawn as lines (fitted curves)."""
        overrides = []
        for i, c in enumerate(ys):
            kind = "lines" if lines and c in lines else "points"
            overrides.append({"matcher": {"id": "byName", "options": c}, "properties": [
                {"id": "color", "value": {"mode": "fixed", "fixedColor": PALETTE[i % len(PALETTE)]}},
                {"id": "custom.show", "value": kind}, {"id": "custom.pointSize.fixed", "value": 6}]})
        self._add({"type": "xychart", "title": title, "description": description, "datasource": GRAFANA_DS,
                   "targets": self._target(df[[x] + ys], None),
                   "fieldConfig": {"defaults": {"custom": {"show": "points", "pointSize": {"fixed": 6}, "lineWidth": 2}},
                                   "overrides": overrides},
                   "options": {"mapping": "manual", "series": [
                       {"x": x, "y": y, "color": {"fixed": PALETTE[i % len(PALETTE)]}} for i, y in enumerate(ys)],
                       "legend": {"displayMode": "list", "placement": "bottom"}}}, w, h)

    def bars(self, title: str, df: pd.DataFrame, description: str = "", unit: str = "short", stacking: str = "none",
             w: int = 12, h: int = 9, horizontal: bool = False) -> None:
        """Bar chart: first column = category label (string or number), other columns = bar series."""
        self._add({"type": "barchart", "title": title, "description": description, "datasource": GRAFANA_DS,
                   "targets": self._target(df, None),
                   "fieldConfig": {"defaults": {"unit": unit, "custom": {"fillOpacity": 80}}, "overrides": []},
                   "options": {"xField": df.columns[0], "stacking": stacking, "showValue": "auto",
                               "orientation": "horizontal" if horizontal else "vertical",
                               "legend": {"displayMode": "list", "placement": "bottom"}, "tooltip": {"mode": "multi"}}},
                  w, h)

    def stat(self, title: str, values: dict[str, float], description: str = "", unit: str = "short", decimals: int = 3,
             w: int = 24, h: int = 4, thresholds: list[tuple[float | None, str]] | None = None) -> None:
        """One big number per key in ``values`` (a one-row table)."""
        steps = [{"color": c, "value": v} for v, c in (thresholds or [(None, "blue")])]
        self._add({"type": "stat", "title": title, "description": description, "datasource": GRAFANA_DS,
                   "targets": self._target(pd.DataFrame([values]), None),
                   "fieldConfig": {"defaults": {"unit": unit, "decimals": decimals,
                                                "thresholds": {"mode": "absolute", "steps": steps}}, "overrides": []},
                   "options": {"reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
                               "colorMode": "value", "graphMode": "none", "textMode": "value_and_name"}}, w, h)

    def table(self, title: str, df: pd.DataFrame, description: str = "", w: int = 12, h: int = 9) -> None:
        self._add({"type": "table", "title": title, "description": description, "datasource": GRAFANA_DS,
                   "targets": self._target(df, None), "fieldConfig": {"defaults": {}, "overrides": []},
                   "options": {"showHeader": True}}, w, h)

    def to_json(self) -> dict:
        d = {"uid": self.uid, "title": self.title, "description": self.description, "tags": ["statistics-course"],
             "timezone": "utc", "schemaVersion": 39, "version": 1, "editable": True, "graphTooltip": 1, "refresh": "",
             "annotations": {"list": []}, "templating": {"list": []}, "panels": self.panels,
             "time": {"from": self.range[0], "to": self.range[1]} if self.range else {"from": "now-6h", "to": "now"}}
        return d

    def save(self, out: Path) -> None:
        (out / "grafana").mkdir(exist_ok=True)
        (out / "grafana" / "dashboard.json").write_text(json.dumps(self.to_json(), indent=1) + "\n")


# --------------------------------------------------------------------- misc helpers
def md(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n")
