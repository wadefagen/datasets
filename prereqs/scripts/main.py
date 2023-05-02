import pandas as pd
from pathlib import Path
import re
import json

'''
Potential formats include:
- One of CS 233, CS 240 or CS 340; CS 374 or ECE 374; one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, BIOE 210.
- One of ABE 361, CHBE 421, TAM 335; or credit or concurrent registration in ME 370.
- Concurrent enrollment in or completion of ACE 345, ACE 346, ACE 444, and ACE 449.
- MATH 225, MATH 257, or MATH 415; MATH 285, MATH 284, MATH 286, or MATH 441; and TAM 212.
'''

def extract_prerequisites(text):
    segments = text.split(";")
    output = set()
    sameas_list = []
    for segment in segments:
        # Get position of first class name e.g ACE 345
        # print(segment)
        first_match = re.search(r'[A-Z]{2,4}\s\d{3}', segment)
        if first_match is None:
            continue
        _, end = first_match.span()

        is_concurrent = "concurrent" in segment.lower()
        is_or = "one of" in segment.lower() or "or" in segment[end:].lower()
        is_sameas = "same as" in segment.lower()
        courses_list = re.findall(r'([A-Z]{2,4}\s\d{3})', segment)
        courses_list = [c.replace('\xa0', ' ') for c in courses_list]
        if is_sameas:
            sameas_list.extend(courses_list)
        elif is_or:
            or_clause = []
            for course in courses_list:
                or_clause.append((course, is_concurrent))
            output.add(tuple(or_clause))
        else:
            for course in courses_list:
                output.add(((course, is_concurrent),))
    return output, sameas_list


if __name__ == '__main__':
    terms = ['2023-sp', '2022-fa']
    courses = pd.concat([pd.read_csv(Path('..', '..', 'course-catalog', 'data', f'{term}.csv')) for term in terms])
    OUTPUT_PATH_CSV = Path('..', 'data', 'uiuc-prerequisites.csv')
    OUTPUT_PATH_JSON = Path('..', 'data', 'uiuc-prerequisites.json')
    course_dict = {}
    courses.fillna('', inplace=True)
    for index, row in courses.iterrows():
        description = row['Description']
        name_formatted = f'{row["Subject"]} {row["Number"]}'
        if name_formatted not in course_dict:
            course_dict[name_formatted] = set()
        if "Prerequisite" in description:
            start = description.find("Prerequisite")
            end = description.find(".", start)
            prereq_text = description[start:end]
            prereqs, sameas_list = extract_prerequisites(prereq_text)
            course_dict[name_formatted].update(prereqs)
            for sameas in sameas_list:
                if sameas not in course_dict:
                    course_dict[sameas] = set()
                course_dict[sameas].update(prereqs)

    # Update cross-listed courses
    for index, row in courses.iterrows():
        description = row['Description']
        name_formatted = f'{row["Subject"]} {row["Number"]}'

        # Check if description like See CS 233
        code = re.search(r'See\s([A-Z]{2,4}\s\d{3})', description)
        if code is not None:
            crosslisted_as = code.group(1)
        
            if crosslisted_as in course_dict:
                course_dict[name_formatted].update(course_dict[crosslisted_as])

    # Convert course tuples to json objects after removing duplicates using sets
    # print(course_dict['UP 494'])
    for course, prereqs in course_dict.items():
        prereq_list = []
        for prereq in prereqs:
            new_prereq = []
            for (course_name, is_concurrent) in prereq:
                new_prereq.append({
                    "course": course_name,
                    "is_concurrent": is_concurrent
                })
            prereq_list.append(new_prereq)
        course_dict[course] = prereq_list
    # https://stackoverflow.com/questions/8230315/how-to-json-serialize-sets
    class SetEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, set):
                return list(o)
            return json.JSONEncoder.default(self, o)

    # course_dict -> CSV

    import pandas as pd

    df = pd.DataFrame()
    bigCourseId = []
    lilCourseId = []
    Concurrent = []
    PrereqNumber = []
    for key in course_dict: # CS374
        for i in range(len(course_dict[key])): #iterate through all []s in key's list
            course_arr = course_dict[key][i] #one prereq array 
            for j in range(len(course_arr)):
                bigCourseId.append(key)
                lilCourseId.append(course_arr[j]['course'])         
                Concurrent.append(course_arr[j]['is_concurrent'])
                PrereqNumber.append(i)

    df['CourseName'] = bigCourseId
    df['PrereqName'] = lilCourseId
    df['ConcurrentAllowed'] = Concurrent
    df['PrereqGroupNum'] = PrereqNumber

    df.to_csv(OUTPUT_PATH_CSV, index = False)
    with open(OUTPUT_PATH_JSON, 'w', encoding='utf-8') as f:
        json.dump(course_dict, f, indent=2, cls=SetEncoder)