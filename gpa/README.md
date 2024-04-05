# University of Illinois' GPA Dataset

As a response to Freedom of Information Act requests (FOIA #16-456, and others) for *"the grade distributions by percent and/or letter grade, for every class [...] at the University of Illinois at Urbana-Champaign"*.  This repository contains a record of all of the data from the above FOIA requests in a clean, documented CSV format.

[Download the full dataset as a single CSV file](https://raw.githubusercontent.com/wadefagen/datasets/master/gpa/uiuc-gpa-dataset.csv)

## Data Format

The first row of the CSV file contains column headers. Every row after the first contains data. Sample:

| Year | Term | YearTerm | Subject | Number | Course Title | Sched Type | A+ | A | A- | B+ | B | B- | C+ | C | C- | D+ | D | D- | F | W | Primary Instructor |
| ---- | ---- | -------- | ------- | ------ | ------------ | ---------- | -- | - | -- | -- | - | -- | -- | - | -- | -- | - | -- | - | - | ------------------ |
| 2024 | Winter | 2024-wi | ADV | 150 | Introduction to Advertising | ONL | 22 | 18 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Hall, Steven R |
| ... |
| 2017 | Fall | 2017-fa | CS | 225 | Data Structures |  | 114 | 47 | 27 | 6 | 28 | 17 | 14 | 18 | 13 | 12 | 9 | 12 | 16 | 2 | Fagen-Ulmschnei, Wade A |
| 2017 | Fall | 2017-fa | CS | 225 | Data Structures |  | 121 | 40 | 27 | 20 | 29 | 16 | 14 | 24 | 4 | 12 | 14 | 16 | 14 | 4 | Fagen-Ulmschnei, Wade A |
| ... |

*Note that long names for "Primary Instructor" are truncated by the University of Illinois in this dataset.*

## Projects Using this Dataset

1. [GPAs of Every Course at The University of Illinois](http://waf.cs.illinois.edu/discovery/gpa_of_every_course_at_illinois/), 
2. [Every Gen Ed at UIUC, by GPA](http://waf.cs.illinois.edu/discovery/every_gen_ed_at_uiuc_by_gpa/)
3. [Grade disparity between sections at UIUC](http://waf.cs.illinois.edu/discovery/grade_disparity_between_sections_at_uiuc/)
4. ~~[GPA++](https://chinmayamahesh.me/gpa)~~ *(No longer active as of April 2024)*
5. [Grade Distributions at UIUC](https://coursegrades.web.illinois.edu/)

*If you create a project with this dataset, I'd love to link it here!  Send a PR with your project added to this list!*

## Data Source

All data contains in this repository is data contained in public documents released in response to FOIA requests.  Some data was excluded by The University of Illinois to adhere to privacy laws.  A table detailing the FOIA request for each term of data is provided.

### Exclusion of Data

From FOIA #2018-150:

> Please be advised that certain information has been withheld under section 140/7(1)(a) that exempts from disclosure “[i]nformation specifically prohibited from disclosure by federal or State law or rules and regulations implementing adopted under federal or State law.” Specifically, the Family Educational Rights and Privacy Act (FERPA) (20 U.S.C. §1232g) protects the privacy of student education records and prohibits the release of any information from a student’s education record without the consent of the eligible student. In this case, grade distributions are not displayed when a section has low enrollment or when all students in the class have the same grade. Because of the low enrollment in those classes or because all the students in a class received the same grade, the grade data could identify a student.  Thus, such information was not provided to you as it would not only violate FERPA, but it would also be invasion of personal privacy under Section 7(1)(c) of FOIA which exempts from disclosure “personal information.” 

Based on analysis, courses with 20 or fewer students were excluded (the smallest course in the dataset has 21 students).

### Table of FOIA Responses

| Year | Winter        | Spring       | Summer        | Fall         |
| ---- | ------------- | ------------ | ------------- | ------------ |
| 2024 | ✔ (24-438)   | &mdash;  | &mdash;  | &mdash;   | &mdash;   |
| 2023 | ✔ (23-456)   | ✔ (23-1295)  | ✔ (23-1295)  | ✔ (24-438)   |
| 2022 | ✔ (22-297)   | ✔ (22-297r2) | ✔ (22-297r2) | ✔ (23-456)   |
| 2021 | ✔ (21-356)   | ✔ (21-729)   | ✔ (22-297)   | ✔ (22-297)   |
| 2020 | ✔ (20-207)   | ✔ (20-875)   | ✔ (20-875)   | ✔ (21-356)   |
| 2019 | ✔ (19-766)   | ✔ (19-766)   | ✔ (19-766)   | ✔ (20-207)   |
| 2018 | ✔ (18-907)   | ✔ (18-907)   | ✔ (19-202)   | ✔ (19-202)   |
| 2017 | ✔ (18-907)   | ✔ (2018-150) | ✔ (18-907)   | ✔ (2018-150) |
| 2016 | ✔ (2016-456) | ✔ (2016-456) | ✔ (2017-042) | ✔ (2017-213) |
| 2015 | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) |
| 2014 | &mdash;*     | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) |
| 2013 | &mdash;*     | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) |
| 2012 | &mdash;*     | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) |
| 2011 | &mdash;*     | ✔ (2016-456) | &mdash;       | ✔ (2016-456) |
| 2010 | &mdash;*     | ✔ (2016-456) | ✔ (2016-456) | ✔ (2016-456) |

*: University of Illinois did not have a winter term before 2014.  Winter term semesters are labeled based on the year they end (ex: Winter 2022-2023 term is labeled as "Winter 2023").

### Dataset Format Changes

#### April 5, 2024

- The "Winter" semester was re-labeled to match the University of Illinois' course catalog term for winter semesters.  Previously, Winter 2022-2023 was labeled as Winter 2022 in this dataset.  Now, Winter 2022-2023 is labeled as Winter 2023 and matches the course catalog.
- Previously, "LIS ###" courses were labeled in the dataset to "IS ###" to match a course catalog change that keep continuity between courses through rubric changes.  This practice was not continued across other rubric changes and make it a bit of an awkward special case.  The special-case was removed and courses before 2017 are now "LIS ###" (as they were taught) instead of being changed to "IS ###".
- Summer 2011 was a copy of Fall 2011 and was removed from the dataset. ([#14](https://github.com/wadefagen/datasets/issues/14))