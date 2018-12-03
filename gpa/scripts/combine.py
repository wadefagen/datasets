import csv

from os import listdir
from os.path import isfile, join

allRows = []
fieldnames = ["Year", "Term", "YearTerm", "Subject", "Number", "Course Title", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F", "W", "Primary Instructor"]

def replaceKey(orig, new):
  if orig in row:
    row[new] = row[orig]
    del row[orig]

for f in listdir("raw/"):
  print(f)
  with open("raw/" + f, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      # The unified field for course subject (eg: "CS") will be called "Subject"
      replaceKey("Course Subject", "Subject")
      replaceKey("ï»¿Subject", "Subject")

      # The unified field for course number (eg: 225) will be called "Number"
      replaceKey("Course", "Number")
      replaceKey("Course ", "Number")
      replaceKey("Course Number", "Number")

      # Term and Year
      if f[0:2] == "sp": row["Term"] = "Spring"
      elif f[0:2] == "su": row["Term"] = "Summer"
      elif f[0:2] == "fa": row["Term"] = "Fall"
      elif f[0:2] == "wi": row["Term"] = "Winter"

      row["Year"] = f[2:6]
      row["YearTerm"] = f[2:6] + "-" + f[0:2]

      # Remove data not included in the final output
      for key in list(row):
        if key not in fieldnames:
          del row[key]

      # changing LIS course name to IS to match 2017 name change
      if row["Subject"] == "LIS":
        row["Subject"] = "IS"
        
      # Include only real data
      if row["A+"] != "N/A":
        allRows.append(row)


allRows = sorted(allRows, key=lambda k: k['Year'], reverse=True) 

with open("uiuc-gpa-dataset.csv", "w") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames,  lineterminator='\n')

  writer.writerow(dict((fn,fn) for fn in fieldnames))
  for row in allRows:
    writer.writerow(row)