# University of Illinois' GPA Dataset

As a response to Freedom of Information Act requests (FOIA #16-456, and others) for *"the grade distributions by percent and/or letter grade, for every class [...] at the University of Illinois at Urbana-Champaign"*.  This repository contains a record of all of the data from the above FOIA requests in a clean, documented CSV format.

[Download the full dataset as a single CSV file](https://raw.githubusercontent.com/wadefagen/datasets/master/gpa/uiuc-gpa-dataset.csv)

## Data Format

The first row of the CSV file contains column headers. Every row after the first contains data. Sample:

| Year | Term | YearTerm | Subject | Number | Course Title | A+ | A | A- | B+ | B | B- | C+ | C | C- | D+ | D | D- | F | W | Primary Instructor |
| ---- | ---- | -------- | ------- | ------ | ------------ | -- | - | -- | -- | - | -- | -- | - | -- | -- | - | -- | - | - | ------------------ |
| 2019 | Fall | 2019-fa | AAS | 100 | Intro Asian American Studies | 20 | 6 | 1 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Boonsripaisal, Simon |
| ... |
| 2017 | Fall | 2017-fa | CS | 225 | Data Structures | 114 | 47 | 27 | 6 | 28 | 17 | 14 | 18 | 13 | 12 | 9 | 12 | 16 | 2 | Fagen-Ulmschnei, Wade A |
| 2017 | Fall | 2017-fa | CS | 225 | Data Structures | 121 | 40 | 27 | 20 | 29 | 16 | 14 | 24 | 4 | 12 | 14 | 16 | 14 | 4 | Fagen-Ulmschnei, Wade A |
| ... |

*Note that long names for "Primary Instructor" are truncated by the University of Illinois in this dataset.*

## Projects Using this Dataset

1. [GPAs of Every Course at The University of Illinois](http://waf.cs.illinois.edu/discovery/gpa_of_every_course_at_illinois/), 
2. [Every Gen Ed at UIUC, by GPA](http://waf.cs.illinois.edu/discovery/every_gen_ed_at_uiuc_by_gpa/)
3. [Grade disparity between sections at UIUC](http://waf.cs.illinois.edu/discovery/grade_disparity_between_sections_at_uiuc/)

*If you create a project with this dataset, I'd love to link it here!  Send a PR with your project added to this list!*

## Data Source

All data contains in this repository is data contained in public documents released in response to FOIA requests.  Some data was excluded by The University of Illinois to adhere to privacy laws.  A table detailing the FOIA request for each term of data is provided.

### Exclusion of Data

From FOIA #2018-150:

> Please be advised that certain information has been withheld under section 140/7(1)(a) that exempts from disclosure “[i]nformation specifically prohibited from disclosure by federal or State law or rules and regulations implementing adopted under federal or State law.” Specifically, the Family Educational Rights and Privacy Act (FERPA) (20 U.S.C. §1232g) protects the privacy of student education records and prohibits the release of any information from a student’s education record without the consent of the eligible student. In this case, grade distributions are not displayed when a section has low enrollment or when all students in the class have the same grade. Because of the low enrollment in those classes or because all the students in a class received the same grade, the grade data could identify a student.  Thus, such information was not provided to you as it would not only violate FERPA, but it would also be invasion of personal privacy under Section 7(1)(c) of FOIA which exempts from disclosure “personal information.” 

Based on analysis, courses with 20 or fewer students were excluded (the smallest course in the dataset has 21 students).

### Table of FOIA Responses

| Year | Spring       | Summer        | Fall         | Winter        |
| ---- | ------------ | ------------- | ------------ | ------------- |
| 2019 | ✔ (19-766)   | ✔ (19-766)   | ✔ (20-207)   | ✔ (20-207)   |   
| 2018 | ✔ (18-907)   | ✔ (19-202)   | ✔ (19-202)   | ✔ (19-766)   |   
| 2017 | ✔ (2018-150) | ✔ (18-907)   | ✔ (2018-150) | ✔ (18-907)   |   
| 2016 | ✔ (2016-456) | ✔ (2017-042) | ✔ (2017-213) | ✔ (18-907)   |
| 2015 | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) |
| 2014 | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) |
| 2013 | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) | ---           |
| 2012 | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) | ---           |
| 2011 | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) | ---           |
| 2010 | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) | ---           |
