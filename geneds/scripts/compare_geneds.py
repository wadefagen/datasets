"""Compare two gened CSV files and report what is new in the newer one.

Usage:
    python compare_geneds.py history/sp2023.csv history/sp2027.csv
    python compare_geneds.py sp2023 sp2027          (looks in history/)
"""
import argparse
import csv
import sys
from pathlib import Path

HERE = Path(__file__).parent.parent
CATEGORIES = ["ACP", "CS", "HUM", "NAT", "QR", "SBS"]


def resolve(name):
    path = Path(name)
    if path.exists():
        return path
    candidate = HERE / "history" / (name if name.endswith(".csv") else name + ".csv")
    if candidate.exists():
        return candidate
    sys.exit(f"File not found: {name}")


def load(path):
    """Return {course: (title, {category: value})}."""
    courses = {}
    raw = Path(path).read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp1252")
    if True:
        for row in csv.DictReader(text.splitlines()):
            cats = {c: row[c].strip() for c in CATEGORIES if row.get(c, "").strip()}
            courses[row["Course"].strip()] = (row["Course Title"].strip(), cats)
    return courses


def fmt(cats):
    return ", ".join(f"{k}={v}" for k, v in cats.items()) or "-"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("older")
    parser.add_argument("newer")
    args = parser.parse_args()

    old = load(resolve(args.older))
    new = load(resolve(args.newer))

    added = sorted(set(new) - set(old))
    print(f"New gened courses in {args.newer} (not in {args.older}): {len(added)}")
    for course in added:
        title, cats = new[course]
        print(f"  {course}: {title} [{fmt(cats)}]")

    gained = []
    for course in sorted(set(new) & set(old)):
        extra = {k: v for k, v in new[course][1].items() if k not in old[course][1]}
        if extra:
            gained.append((course, new[course][0], extra))
    print(f"\nExisting courses with newly added gened categories: {len(gained)}")
    for course, title, extra in gained:
        print(f"  {course}: {title} [+ {fmt(extra)}]")


if __name__ == "__main__":
    main()
