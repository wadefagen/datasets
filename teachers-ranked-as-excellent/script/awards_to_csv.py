"""Merge all awards text files in html_txt/ (from extract_awards.py) into one CSV.

Columns: term,unit,lname,fname,role,ranking,course
One row is written per person per course.

Usage:
    python awards_to_csv.py [-i html_txt] [-o isg-flex-awards.csv]

The term is derived from each file name (e.g. summer-2026.txt -> su2026). For a
combined file such as fall-2025-and-winter-2025.txt, the first term in the
name is used.
"""
import argparse
import csv
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "html_txt"
OUTPUT_FILE = BASE_DIR / "isg-flex-awards.csv"
RANKING = "ISG FLEX Award"
SEASONS = {"fall": "fa", "winter": "wi", "spring": "sp", "summer": "su"}
LINE_RE = re.compile(r"^(?P<name>.+?) - (?P<ta>T\.A\. )?(?P<courses>\d.*)$")


def term_from_filename(path):
    m = re.search(r"(fall|winter|spring|summer)-(\d{4})", path.stem.lower())
    if not m:
        raise SystemExit(f"Could not derive term from file name: {path.name}")
    return SEASONS[m.group(1)] + m.group(2)


def split_name(name):
    if "," in name:
        lname, fname = name.split(",", 1)
        fname = fname.strip()
        # The source page uses "Last, -" when there is no first initial.
        return lname.strip(), "" if fname == "-" else fname
    # Some entries are "First Last" with no comma.
    return name.strip(), ""


def convert(lines, term):
    unit = None
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            unit = line[2:].strip()
            continue
        m = LINE_RE.match(line)
        if unit is None or not m:
            print(f"Skipping unparsable line: {line!r}")
            continue
        lname, fname = split_name(m.group("name"))
        role = "TA" if m.group("ta") else "Instructor"
        for course in m.group("courses").split(", "):
            yield [term, unit, lname, fname, role, RANKING, course.strip()]


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("-i", "--input-dir", type=Path, default=INPUT_DIR)
    parser.add_argument("-o", "--output", type=Path, default=OUTPUT_FILE)
    args = parser.parse_args()

    files = sorted(args.input_dir.glob("*.txt"))
    if not files:
        raise SystemExit(f"No .txt files found in {args.input_dir}")

    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["term", "unit", "lname", "fname", "role", "ranking", "course"])
        total = 0
        for path in files:
            term = term_from_filename(path)
            lines = path.read_text(encoding="utf-8").splitlines()
            count = 0
            for row in convert(lines, term):
                writer.writerow(row)
                count += 1
            total += count
            print(f"{path.name}: {count} rows (term={term})")
    print(f"{args.output}: {total} rows total")


if __name__ == "__main__":
    main()
