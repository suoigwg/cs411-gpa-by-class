from bs4 import BeautifulSoup
from common import write_to_file, read_json_from_file, DATA_FOLDER
import urllib3
import os

BASE_URL = "https://courses.illinois.edu/schedule/2020/spring"
COURSE_MAP_FILE_PATH = DATA_FOLDER + "course_map.txt"
PREREQ_FILE_PATH = DATA_FOLDER + "prereqs.txt"


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


if __name__ == "__main__":
    http = urllib3.PoolManager()
    course_codes = get_course_codes(http)
    if not os.path.exists(COURSE_MAP_FILE_PATH):
        print('Course map does not exist')
        course_map = get_course_numbers(course_codes, http)
        write_to_file(course_map, COURSE_MAP_FILE_PATH)
    else:
        print('Course map exists')
        course_map = read_json_from_file(COURSE_MAP_FILE_PATH)
    if not os.path.exists(PREREQ_FILE_PATH):
        prereqs = get_all_prereqs(course_map, http)
        write_to_file(prereqs, PREREQ_FILE_PATH)
    else:
        print('Prereq file already exists')
