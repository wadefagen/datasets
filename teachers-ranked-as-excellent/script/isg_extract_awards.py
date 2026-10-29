"""Extract ISG teaching award recipients from a saved HTML page.

Each element with class "season-block" holds one term (e.g. "Summer 2026").
For every term, a text file is written with one Markdown header per unit
followed by the names of everyone who earned the award in that unit.

Usage:
    python extract_awards.py INPUT.html [-o OUTPUT_DIR]
"""
import argparse
import re
from pathlib import Path

from bs4 import BeautifulSoup


def term_filename(term):
    slug = re.sub(r"[^\w]+", "-", term.strip()).strip("-").lower()
    return f"{slug or 'term'}.txt"


def extract_terms(html):
    soup = BeautifulSoup(html, "html.parser")
    for block in soup.select(".season-block"):
        summary = block.find("summary", recursive=False)
        term = summary.get_text(" ", strip=True) if summary else "unknown-term"
        units = []
        for unit in block.select("details"):
            unit_summary = unit.find("summary", recursive=False)
            body = unit.find("p", recursive=False)
            if unit_summary is None or body is None:
                continue
            name = unit_summary.get_text(" ", strip=True)
            people = [
                line.strip()
                for line in body.get_text("\n").split("\n")
                if line.strip()
            ]
            units.append((name, people))
        yield term, units


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("html_file", type=Path)
    parser.add_argument("-o", "--output-dir", type=Path, default=Path("html_txt"))
    args = parser.parse_args()

    html = args.html_file.read_text(encoding="utf-8")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    found = False
    for term, units in extract_terms(html):
        found = True
        lines = []
        for name, people in units:
            lines.append(f"# {name}")
            lines.extend(people)
            lines.append("")
        path = args.output_dir / term_filename(term)
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"{path}: {len(units)} units")

    if not found:
        print("No elements with class 'season-block' found.")


if __name__ == "__main__":
    main()
