"""Helpers shared by the spreadsheet-fundamentals lessons (s01-s05)."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import HEADER_FILL, HEADER_FONT  # noqa: E402


def add_sheet_df(book, name: str, df: pd.DataFrame, fmt: dict[str, str] | None = None) -> None:
    """Add a plain values-only sheet (reference tables, pre-sorted copies...)."""
    ws = book.wb.create_sheet(name)
    for j, col in enumerate(df.columns, start=1):
        c = ws.cell(row=1, column=j, value=str(col))
        c.fill, c.font = HEADER_FILL, HEADER_FONT
        ws.column_dimensions[get_column_letter(j)].width = max(12, len(str(col)) + 3)
    for i, row in enumerate(df.itertuples(index=False), start=2):
        for j, v in enumerate(row, start=1):
            if isinstance(v, pd.Timestamp):
                v = v.to_pydatetime()
            elif isinstance(v, np.integer):
                v = int(v)
            elif isinstance(v, np.floating):
                v = None if np.isnan(v) else float(v)
            c = ws.cell(row=i, column=j, value=v)
            f = (fmt or {}).get(str(df.columns[j - 1]))
            if f:
                c.number_format = f
    ws.freeze_panes = "A2"


def text_formula(ws, cell: str, text: str) -> None:
    """Store a formula as TEXT (so it is shown, not evaluated) - for Google-Sheets-only functions."""
    c = ws[cell]
    c.value = text
    c.data_type = "s"
    c.font = Font(name="Consolas")


def write_csv_named(out: Path, name: str, df: pd.DataFrame) -> None:
    d = df.copy()
    for c in d.columns:
        if pd.api.types.is_datetime64_any_dtype(d[c]):
            d[c] = d[c].dt.strftime("%Y-%m-%d")
    d.to_csv(out / name, index=False)
