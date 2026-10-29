"""Combine isg-flex-awards.csv and uiuc-tre-dataset.csv into
highly-ranked-instructors.csv, sorted with the latest term first.

Usage (from the base folder):
    python3 script/combine.py
"""
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUTS = [BASE_DIR / "isg-flex-awards.csv", BASE_DIR / "uiuc-tre-dataset.csv"]
OUTPUT = BASE_DIR / "highly-ranked-instructors.csv"
HEADER = ["term", "unit", "lname", "fname", "role", "ranking", "course"]

# Chronological order within a calendar year.
SEASON_ORDER = {"wi": 0, "sp": 1, "su": 2, "fa": 3}


def term_key(term):
    # e.g. "fa2025" -> (2025, 3)
    return int(term[2:]), SEASON_ORDER[term[:2]]


def main():
    rows = []
    for path in INPUTS:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            if next(reader) != HEADER:
                raise SystemExit(f"Unexpected header in {path.name}")
            rows.extend(reader)

    # sorted() is stable, so the original order is kept within a term.
    rows.sort(key=lambda r: term_key(r[0]), reverse=True)

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(rows)
    print(f"{OUTPUT.name}: {len(rows)} rows")


if __name__ == "__main__":
    main()
