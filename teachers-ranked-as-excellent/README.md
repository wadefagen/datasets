# Teachers Ranked as Excellent at The University of Illinois

A collection of all "Teachers Ranked as Excellent" and "Illinois Student Government FLEX Award" records at UIUC from Fall 1993 to present in a clean, consistent CSV format.

[A single CSV containing all of the data can be downloaded here.][Single_CSV_Download]

[Single_CSV_Download]: https://raw.githubusercontent.com/wadefagen/datasets/master/teachers-ranked-as-excellent/highly-ranked-instructors.csv

- Latest Update: **October 29, 2026** (added ISG FLEX Awards for Fall 2025 - Summer 2026),
- Dataset Date Range:
  - Teachers Ranked as Excellent: Fall 1993 - Spring 2025
  - Illinois Student Government FLEX Award: Fall 2025 - Spring 2026

## Background

### Teachers Ranked as Excellent

Before Fall 2025, every semester students completed an [Instructor and Course Evaluation System (ICES)][ICES_CITL] questionnaire for each course they are enrolled.  The [Center for Innovation in Teaching and Learning (CITL)][MAIN_CITL] compiles this data into the list of "Teachers Ranked as Excellent" and publishes the names of those teaches in the local newspaper and [online as a PDF][TRE_CITL].

[TRE_CITL]: http://citl.illinois.edu/citl-101/measurement-evaluation/teaching-evaluation/teaching-evaluations-(ices)/teachers-ranked-as-excellent
[ICES_CITL]: http://citl.illinois.edu/citl-101/measurement-evaluation/teaching-evaluation/teaching-evaluations-(ices)
[MAIN_CITL]: http://citl.illinois.edu/

- Instructors and TAs who were ranked "Outstanding" (the highest honor) are denoted with `Outstanding` in the `ranking` column in the dataset.
- Instructors and TAs who were ranked "Excellent" are denoted with `Excellent` in the `ranking` column in the dataset.

### Illinois Student Government FLEX Award

In Fall 2025, the ICES questionnaire was replaced by the Feedback on the Learning Experience (FLEX) survey.  The "Teachers Ranked as Excellent" award was replaced by the Illinois Student Government (ISG) FLEX Award, which "recognizes instructors and TAs who achieve outstanding FLEX evaluation results".

- Instructors and TAs who were ranked are denoted with `ISG FLEX Award` in the `ranking` column in the dataset.


## Repository Contents

This repository contains a collection of all known lists of "Teachers Ranked as Excellent", dating back to 1993, in a consistent, documented CSV format.  Each semester can be found in the `csv` directory.

The goal of this repository is to provide an easy interface for the use of this data in data science projects.

### CSV Fields

| term | unit | lname | fname | role | ranking | course |
| ---- | ---- | ----- | ----- | ---- | ------- | ------ |
| fa2003 | ACCOUNTANCY | BALLOU | B | Instructor | Excellent | 304 |
| fa2003 | ACCOUNTANCY | CHANDLER | J | Instructor | Excellent | 304 |
| fa2003 | ACCOUNTANCY | DEREUS | M | TA | Excellent | 201 |
| ... |
| fa2018 | COMPUTER SCIENCE | FAGEN-ULMSCHNEIDER | W | Instructor | Outstanding | 225 |
| ... |

All CSVs contain eight fields, with field labels in the first row and data in all following rows.  The data contained in the fields are as follows:

- `term`: Two letter semester code (`sp`, `su`, `fa`, or `wi`) followed by a four digit year.
  * Examples: `sp2017`, `fa2013`, `su2012`.

- `unit`: The CITL-supplied headers for the unit teaching the course.
  * Examples: `ACCOUNTANCY`, `SOCIAL WORK`, `LINGUISTICS`, `NUCLEAR, PLASMA & RAD. ENGR.`

- `lname`: The last name of the teacher.
  * Examples: `FAGEN-ULMSCHNEIDER`, `FLANAGAN`, `FLECK`

- `fname`: The first letter of the first name of the teacher.
  * Examples: `W`, `K`, `M`

- `role`: `Instructor` or `TA`

- `ranking`: `Excellent` or `Outstanding`

- `course`: The course the teacher was ranked as excellent.  If no course is given, the `course` field is set to `?` (this includes cases when the raw data lists the course as `0`, `000`, or `999`).
  * Examples: `199`, `225`, `560`, `?`


#### Ranked as Excellent in Multiple Courses in One Semester

The same teacher may be ranked for multiple courses in a single semester.  In that case, the teacher will appear more than once in this dataset (this is different than how the source dataset presents this data).  For example:
```
sp2012,"NUCLEAR, PLASMA & RAD. ENGR.",AXFORD,R,Instructor,Excellent,447
sp2012,"NUCLEAR, PLASMA & RAD. ENGR.",AXFORD,R,Instructor,Excellent,521
```