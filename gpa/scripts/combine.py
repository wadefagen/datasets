import csv

from os import listdir
from os.path import isfile, join

allRows = []
fieldnames = ["Year", "Term", "YearTerm", "Subject", "Number", "Course Title", "Sched Type", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F", "W", "Students", "Primary Instructor"]

def replaceKey(orig, new):
  if orig in row:
    row[new] = row[orig]
    del row[orig]

for f in listdir("raw/"):
  print(f)
  isTsv = f.lower().endswith(".tsv")

  # New TSV files are UTF-16 (with BOM); legacy CSV files use the default encoding
  with open("raw/" + f, "r", encoding="utf-16" if isTsv else None, newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t" if isTsv else ",")
    for row in reader:
      replaceKey("Schedule Type", "Sched Type")
      # ...existing replaceKey calls continue unchanged

  # with open("raw/" + f, "r") as csvfile:
  #   reader = csv.DictReader(csvfile)
  #   for row in reader:
  #     # The unified field for course subject (eg: "CS") will be called "Subject"
      replaceKey("Course Subject", "Subject")
      replaceKey("ï»¿Subject", "Subject")

      # The unified field for course number (eg: 225) will be called "Number"
      replaceKey("Course", "Number")
      replaceKey("Course ", "Number")
      replaceKey("Course Number", "Number")

      # Term and Year
      if isTsv:
        term, year = row["Term"].split(" ")
        shortTerm = term[0:2].lower()

        row["Term"] = term
        row["Year"] = year
        row["YearTerm"] = f"{year}-{shortTerm}"
      else:
        if f[0:2] == "sp": row["Term"] = "Spring"
        elif f[0:2] == "su": row["Term"] = "Summer"
        elif f[0:2] == "fa": row["Term"] = "Fall"
        elif f[0:2] == "wi": row["Term"] = "Winter"        

        row["Year"] = f[2:6]
        if row["Term"] == "Winter":
          row["Year"] = str(int(row["Year"]) + 1)

        row["YearTerm"] = row["Year"] + "-" + f[0:2]

      # Remove data not included in the final output
      for key in list(row):
        if key not in fieldnames:
          del row[key]

      # Include only real data
      # Suppressed rows in the TSV format have empty grade columns
      if row["A+"] not in ("N/A", ""):
        # Add "Students" column:
        row["Students"] = \
          int(row["A+"]) + int(row["A"]) + int(row["A-"]) + \
          int(row["B+"]) + int(row["B"]) + int(row["B-"]) + \
          int(row["C+"]) + int(row["C"]) + int(row["C-"]) + \
          int(row["D+"]) + int(row["D"]) + int(row["D-"]) + \
          int(row["F"])

        allRows.append(row)


allRows = sorted(allRows, key=lambda k: k['Year'], reverse=True) 

with open("uiuc-gpa-dataset.csv", "w") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames,  lineterminator='\n')

  writer.writerow(dict((fn,fn) for fn in fieldnames))
  for row in allRows:
    writer.writerow(row)