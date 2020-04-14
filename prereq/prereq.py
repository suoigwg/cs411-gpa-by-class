import re
from common import read_json_from_file, write_to_file, DATA_FOLDER
from scraper import PREREQ_FILE_PATH

PARSED_PREREQ_PATH = DATA_FOLDER + 'parsed_prereq.txt'
COURSE_REGEX = r'[A-Z]{2,4}\s\d{3}'

KEYWORD_DICT = {
    '; or': 'or',
    ';': 'and',
    'One of': 'or',
    'Any of': 'or'
}


def remove_prereq_string(prereqs):
    for course, value in prereqs.items():
        prereqs[course] = value[len("Prerequisite: "):]


def get_prereq_from_string(string):
    result = {}
    if string.find('; or') > -1:
        prereqs = string.split('; or')
        temp = []
        for prereq in prereqs:
            res = get_prereq_from_string(prereq)
            if len(res) > 0:
                temp.append(res)
        if len(temp) == 1:
            return temp[0]
        else:
            result[KEYWORD_DICT['; or']] = temp
    elif string.find('; ') > -1:
        prereqs = string.split('; ')
        temp = []
        for prereq in prereqs:
            res = get_prereq_from_string(prereq)
            if len(res) > 0:
                temp.append(res)
        if len(temp) == 1:
            return temp[0]
        else:
            result[KEYWORD_DICT[';']] = temp
    elif string.find('One of') > -1 or string.find(' or ') > -1 or string.find('Any of') > -1:
        courses = re.findall(COURSE_REGEX, string)
        if len(courses) > 1:
            result['or'] = courses
        elif len(courses) > 0:
            return courses[0]
        else:
            return []
    elif string.find(' and ') > -1:
        courses = re.findall(COURSE_REGEX, string)
        if len(courses) > 1:
            result['and'] = courses
        elif len(courses) > 0:
            return courses[0]
        else:
            return []
    else:
        temp = re.findall(COURSE_REGEX, string)
        if len(temp) == 1:
            return temp[0]
        else:
            return temp
    return result


if __name__ == "__main__":
    prereqs = read_json_from_file(PREREQ_FILE_PATH)
    merged = {}
    for d in prereqs:
        merged.update(d)
    prereqs = merged
    remove_prereq_string(prereqs)

    courses_to_remove = []
    for course, value in prereqs.items():
        classes = re.findall(COURSE_REGEX, value)
        if len(classes) == 0:
            courses_to_remove.append(course)
    [prereqs.pop(course) for course in courses_to_remove]

    converted_prereq = {}
    for course, prereq in prereqs.items():
        converted_prereq[course] = get_prereq_from_string(prereq)

    for course in converted_prereq:
        print(course)
        print(prereqs[course])
        print(converted_prereq[course])
        print('')

    write_to_file(converted_prereq, PARSED_PREREQ_PATH)
