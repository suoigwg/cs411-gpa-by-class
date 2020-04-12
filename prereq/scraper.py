from bs4 import BeautifulSoup
import urllib3
import os
import json

BASE_URL = "https://courses.illinois.edu/schedule/2020/spring"
DATA_FOLDER = "data/"
COURSE_MAP_FILE_NAME = "course_map.txt"
PREREQ_FILE_NAME = "prereqs.txt"


def get_soup(url, browser):
    response = browser.request('GET', url)
    return BeautifulSoup(response.data, 'html.parser')


def get_table_data(soup):
    table = soup.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    columns = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        columns.append(cols)
    return columns


def get_course_codes(browser):
    soup = get_soup(BASE_URL, browser)
    data = get_table_data(soup)
    return [elem[0] for elem in data]


def get_course_numbers(codes, browser):
    course_map = {}
    for code in codes:
        url = BASE_URL + f'/{code}'
        soup = get_soup(url, browser)
        data = get_table_data(soup)
        numbers = [elems[0].split(' ')[1] for elems in data]
        course_map[code] = numbers
    return course_map


def get_prereqs_for_course(course_code, course_number, browser):
    url = BASE_URL + f'/{course_code}/{course_number}'
    soup = get_soup(url, browser)
    content = soup.find_all('p')
    for tag in content:
        paragraph = tag.text
        index = paragraph.find('Prerequisite')
        if index > -1:
            return paragraph[index:]
    return None


def get_prereqs_for_dept(dept, numbers, browser):
    prereq_map = {}
    for course_no in numbers:
        print(f'Number: {course_no}')
        prereq = get_prereqs_for_course(dept, course_no, browser)
        if prereq:
            course = ' '.join([dept, course_no])
            prereq_map[course] = prereq
    return prereq_map


def get_all_prereqs(course_map, browser):
    prereqs = []
    for dept, numbers in course_map.items():
        print(f'Dept: {dept}')
        prereq_map = get_prereqs_for_dept(dept, numbers, browser)
        prereqs.append(prereq_map)
    return prereqs


def write_to_file(content, path, replace=False):
    if not replace and os.path.exists(path):
        print(f'{path} already exists')
        return
    else:
        print(f'Writing: {path}')
        with open(path, 'w') as f:
            f.write(json.dumps(content))


def read_json_from_file(path):
    if os.path.exists(path):
        print(f'Reading: {path}')
        with open(path, 'r') as f:
            content = f.read()
            return json.loads(content)
    else:
        print(f'File: {path} does not exist')


if __name__ == "__main__":
    http = urllib3.PoolManager()
    course_codes = get_course_codes(http)
    course_map_path = DATA_FOLDER + COURSE_MAP_FILE_NAME
    if not os.path.exists(course_map_path):
        print('Course map does not exist')
        course_map = get_course_numbers(course_codes, http)
        write_to_file(course_map, course_map_path)
    else:
        print('Course map exists')
        course_map = read_json_from_file(course_map_path)
    prereqs = get_all_prereqs(course_map, http)

    prereq_file_path = DATA_FOLDER + PREREQ_FILE_NAME
    write_to_file(prereqs, prereq_file_path)
