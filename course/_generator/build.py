#!/usr/bin/env python3
"""Build the course: ``python build.py`` (all lessons) or ``python build.py 3 12 s2`` (selected; ``sN`` = spreadsheet track).

For each lesson module ``lessons/lNN_*.py`` this runs ``build(out_dir) -> Book``, saves the workbook, recalculates it in
LibreOffice headless, and compares every registered check against the value computed independently in Python.
It also fails on any error value (#DIV/0!, #NAME?, ...) anywhere in the recalculated workbook.

Requires: numpy pandas scipy statsmodels openpyxl, and ``soffice`` (LibreOffice) on PATH.
"""
from __future__ import annotations

import datetime
import importlib.util
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from openpyxl import load_workbook

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from common import COURSE_DIR  # noqa: E402

ERRORS = ("#DIV/0!", "#NAME?", "#VALUE!", "#N/A", "#REF!", "#NUM!", "#NULL!", "Err:")


def recalc(src: Path, dst_dir: Path) -> Path:
    profile = Path(tempfile.mkdtemp(prefix="lo_profile_"))
    try:
        subprocess.run(["soffice", f"-env:UserInstallation=file://{profile}", "--headless", "--calc",
                        "--convert-to", "xlsx:Calc MS Excel 2007 XML", "--outdir", str(dst_dir), str(src)],
                       check=True, capture_output=True, timeout=300)
    finally:
        shutil.rmtree(profile, ignore_errors=True)
    return dst_dir / src.name


def verify(book, xlsx: Path) -> list[str]:
    problems: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        out = recalc(xlsx, Path(td))
        wb = load_workbook(out, data_only=True)
        for ws in wb:
            for row in ws.iter_rows():
                for c in row:
                    if isinstance(c.value, str) and c.value.startswith(ERRORS):
                        problems.append(f"error value {c.value} at {ws.title}!{c.coordinate}")
        for ref, label, expected in book.checks:
            sheet, cell = ref.split("!")
            got = wb[sheet][cell].value
            if isinstance(got, datetime.datetime):  # date-formatted cell: compare as an Excel serial number
                got = (got - datetime.datetime(1899, 12, 30)).total_seconds() / 86400
            if not isinstance(got, (int, float)):
                problems.append(f"{ref} [{label}] expected {expected:.6g}, got {got!r}")
            elif not math.isclose(got, expected, rel_tol=1e-6, abs_tol=1e-6):
                problems.append(f"{ref} [{label}] expected {expected:.6g}, got {got:.6g}")
    return problems


def load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv: list[str]) -> int:
    # arguments: "3" -> lesson l03, "s2" -> spreadsheet-fundamentals lesson s02
    wanted = {("s%02d" % int(a[1:]) if a[0] == "s" else "l%02d" % int(a)) for a in argv}
    failed = 0
    for f in sorted((HERE / "lessons").glob("[ls][0-9][0-9]_*.py"), key=lambda p: (p.stem[0] != "l", p.stem)):
        if wanted and f.stem[:3] not in wanted:
            continue
        mod = load(f)
        out = COURSE_DIR / mod.SLUG
        out.mkdir(parents=True, exist_ok=True)
        book = mod.build(out)
        book.save(out / "solution.xlsx")
        problems = verify(book, out / "solution.xlsx")
        if not problems:  # ship the recalculated file: same formulas, but with cached values (viewers that do not calculate)
            with tempfile.TemporaryDirectory() as td:
                shutil.copy(recalc(out / "solution.xlsx", Path(td)), out / "solution.xlsx")
        status = "OK " if not problems else "FAIL"
        print(f"[{status}] {mod.SLUG}: {len(book.checks)} checks")
        for p in problems[:15]:
            print("      ", p)
        failed += bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
