from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from .SQL import *


@api_view(['GET'])
def getGPAByDeptAndYear(request, dept, year):
    cursor = connection.cursor()
    cursor.execute(GPA_BY_YEAR_AND_DEPT, [year, dept])
    columns = [col[0] for col in cursor.description]
    return Response([
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ])


@api_view(['GET'])
def getAllDpetAbbr(request):
    cursor = connection.cursor()
    cursor.execute(GET_ALL_DEPT_ABBR)
    abbr = cursor.fetchall()
    flatten = lambda abbr: [item for sublist in abbr for item in sublist]
    return Response(flatten(abbr))


@api_view(['GET'])
def getCourseGPA(request, course):
    cursor = connection.cursor()
    sub = ''
    no = ''
    for i in range(len(course)):
        if str.isdigit(course[i]):
            no += course[i]
        else:
            sub += course[i]
    sub = sub.upper()
    cursor.execute(GET_COURSE_GPA, [sub, no])
    columns = [col[0] for col in cursor.description]
    return Response([
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ])
