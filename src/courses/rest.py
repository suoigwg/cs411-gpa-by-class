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
