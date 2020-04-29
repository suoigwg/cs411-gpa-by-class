import json
# parse into fixtures

if __name__ == '__main__':
    with open("db_course_preq.txt", "r") as ff:
        data = json.load(ff)
    result = []
    count = 0
    for i in data:
        count = count + 1
        dic = {}
        dic["model"] = "courses.CoursePrereqModel"
        dic["pk"] = count
        dic["fields"] = i
        result.append(dic)

    with open("db_course_preq.json", "w") as fz:
        json.dump(result, fz, indent=2, sort_keys=False)


