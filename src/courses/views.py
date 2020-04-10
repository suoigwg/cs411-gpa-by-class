from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Course, Gpa, Professor, User
from .serializers import CourseSerializer, GpaSerializer, ProfessorSerializer, UserSerializer, SubjectSerializer, CourseNoSerializer, ProfessorNameSerializer, CourseNoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

# SQL queries
USER_LOGIN = """select Username, IsAdmin
from User
where Username = %s and Password = %s;
"""

USER_EXIST = """select *
from User
where Username = %s
"""

USER_REGISTER = """INSERT INTO User(Username, Password, IsAdmin)
VALUES(%s, %s, %s);
"""

GPA_BY_YEAR_AND_DEPT = """select *
from GPA
         join Course C on GPA.CourseId = C.CourseId
         join Professor P on GPA.ProfessorId = P.ProfessorId
where Year = %s
  and Subject = %s;
"""

GET_ALL_DEPT_ABBR = """
SELECT distinct (Subject) FROM Course;
"""

GET_COURSE_GPA = """
select *
from GPA
         join Course C on GPA.CourseId = C.CourseId
         join Professor P on GPA.ProfessorId = P.ProfessorId
where Subject = %s
  and CourseNo = %s
;
"""

GPA_EXIST = """
SELECT *
FROM Gpa
WHERE GPAId = %s
"""

GPA_NEW = """
INSERT INTO Gpa(Term, Value, CourseId, Classsize, Year, ProfessorId, GPAId)
VALUES(%s, %s, %s, %s, %s, %s, %s)
"""

GPA_UPDATE = """
UPDATE Gpa
SET Term = %s, Value = %s, CourseId = %s, Classsize = %s, Year = %s, ProfessorId = %s
WHERE GPAId = %s
"""

GPA_DELETE = """
DELETE FROM Gpa
WHERE GPAID = %s
"""

GET_COURSE_GPA = """
select *
from GPA
         join Course C on GPA.CourseId = C.CourseId
         join Professor P on GPA.ProfessorId = P.ProfessorId
where Subject = %s
  and CourseNo = %s
;
"""

COURSE_EXIST = """
SELECT *
FROM Course
WHERE CourseId = %s
"""

COURSE_NEW = """
INSERT INTO Course(CourseNo, Subject, Title)
VALUES(%s, %s, %s)
"""

COURSE_UPDATE = """
UPDATE Course
SET CourseNo = %s, Subject = %s, Title = %s
WHERE CourseId = %s
"""

COURSE_DELETE = """
DELETE FROM Course
WHERE CourseId = %s
"""

# UserService:
# POST /users/login/
# Input: {username, password}
# Response: 200 or 400
# {username, isAdmin}
@api_view(['POST'])
def user_login(request):
	username = request.data.get('username')
	password = request.data.get('password')
	cursor = connection.cursor()
	cursor.execute(USER_LOGIN, [username, password])
	rows = cursor.fetchall()
	if len(rows) == 0:
		return Response("Incorrect username or password", status = 400)
	columns = [col[0] for col in cursor.description]
	return Response([
		dict(zip(columns, row))
		for row in rows
		])

# POST /users/register/
# Input: {username, password, isAdmin}
# Response: 200 or 400
@api_view(['POST'])
def user_register(request):
	username = request.data.get('username')
	password = request.data.get('password')
	isAdmin = request.data.get('isAdmin')
	#check if user exist
	cursor = connection.cursor()
	cursor.execute(USER_EXIST, [username])
	rows = cursor.fetchall()
	if len(rows) > 0:
		return Response("Username exists.", status = 400)
    #register
	else:
		cursor = connection.cursor()
		cursor.execute(USER_REGISTER, [username, password, isAdmin])
		return Response("Successfully registered.", status = 200)

# CoursesService:
# GET /api/courses/
# Input: {subject}
# Response: [List of courses]
@csrf_exempt
def course_by_subject(request):
	if request.method == 'GET':
		subject = request.GET.get('subject')
		course_sub = Course.objects.filter(subject = subject).distinct()
		serializer = CourseSerializer(course_sub, many=True)
		return JsonResponse(serializer.data, safe = False, status = 200)
		# if serializer.is_valid():
		# 	serializer.save()
		# 	return JsonResponse(serializer.data, safe = False, status = 200)
		# else:
		# 	return JsonResponse(serializer.errors, safe = False, status = 400)
	return HttpResponse("Incorrect request method", status = 400)

# Get /api/subjects/
# Input: None
# Response: [List of subject codes]
@api_view(['GET'])
def getAllDpetAbbr(request):
    cursor = connection.cursor()
    cursor.execute(GET_ALL_DEPT_ABBR)
    abbr = cursor.fetchall()
    flatten = lambda abbr: [item for sublist in abbr for item in sublist]
    return Response(flatten(abbr))

# # Get /api/courseNumbers/
# # Input: Subject
# # Response: [List of course Numbers] (411, 233, ..)
@csrf_exempt
def course_num_list(request):
    if request.method == 'GET':
    	subject = request.GET.get('subject')
    	coursenos = list(Course.objects.filter(subject = subject).values_list('courseno', flat= True).distinct())
    	return JsonResponse(coursenos, safe = False, status = 200)
        # if serializer.is_valid():
        # 	return JsonResponse(serializer.data, status = 200)
        # else:
        # 	return JsonResponse(serializer.errors, status = 400)
    return HttpResponse("Incorrect request method", status = 400)

# Get /api/gpa/
# Input: {year, dept}
# Output: [{course+gpa+professor}, ]
@api_view(['GET'])
def getGPAByDeptAndYear(request):
	year = request.GET.get('year')
	dept = request.GET.get('dept')
	cursor = connection.cursor()
	cursor.execute(GPA_BY_YEAR_AND_DEPT, [year, dept])
	columns = [col[0] for col in cursor.description]
	return Response([
		dict(zip(columns, row))
		for row in cursor.fetchall()
		])

# GPAService:
# GET /api/coursegpa/
# Input: {subject, number}
# Response: [List of GPA info] + (professor_name, subject, number)
@api_view(['GET'])
def getCourseGPA(request):
    cursor = connection.cursor()
    sub = request.GET.get('subject')
    no = request.GET.get('number')
    cursor.execute(GET_COURSE_GPA, [sub, no])
    columns = [col[0] for col in cursor.description]
    return Response([
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ])

@api_view(['POST'])
def gpa_new(request):
	term = request.POST.get('term')
	value = request.POST.get('value')
	courseid = request.POST.get('courseid')
	classsize = request.POST.get('classsize')
	year = request.POST.get('year')
	professorid = request.POST.get('professorid')
	gpaid = request.POST.get('gpaid')
	# check if gpaid exists
	cursor = connection.cursor()
	cursor.execute(GPA_EXIST, [gpaid])
	if cursor.rowcount > 0:
		return Response("Duplicated Gpaid", status = 400)
	cursor = connection.cursor()
	cursor.execute(GPA_NEW, [term, value, courseid, classsize, year, professorid, gpaid])
	return Response("New record added", status = 200)

@api_view(['POST'])
def gpa_update(request):
	term = request.POST.get('term')
	value = request.POST.get('value')
	courseid = request.POST.get('courseid')
	classsize = request.POST.get('classsize')
	year = request.POST.get('year')
	professorid = request.POST.get('professorid')
	gpaid = request.POST.get('gpaid')
	# check if gpaid exists
	cursor = connection.cursor()
	cursor.execute(GPA_EXIST, [gpaid])
	if cursor.rowcount == 0:
		return Response("Record id does not exist", status = 400)
	cursor = connection.cursor()
	cursor.execute(GPA_UPDATE, [term, value, courseid, classsize, year, professorid, gpaid])
	return Response("Gpa record updated.", status = 200)

@api_view(['POST'])
def gpa_delete(request):
	gpaid = request.POST.get('gpaid')
	# check if gpaid exists
	cursor = connection.cursor()
	cursor.execute(GPA_EXIST, [gpaid])
	if cursor.rowcount > 0:
		return Response("Record id does not exist", status = 200)
	cursor = connection.cursor()
	cursor.execute(GPA_DELETE, [gpaid])
	return Response("Gpa record deleted.", status = 200)

@api_view(['POST'])
def course_new(request):
	courses = request.data.get('courses')
	cursor = connection.cursor()
	for course in courses:
		#courseid = course.get('courseid')
		courseno = course.get('courseno')
		subject = course.get('subject')
		title = course.get('title')
        # check if courseid exists
		cursor = connection.cursor()
		#cursor.execute(COURSE_EXIST, [courseid])
		#if cursor.rowcount > 0:
			#return Response("Duplicated CourseId", status = 400)
		cursor.execute(COURSE_NEW, [courseno, subject, title])
	return Response("New record added", status = 200)

@api_view(['POST'])
def course_update(request):
	courses = request.data.get('courses')
	cursor = connection.cursor()
	for course in courses:
		courseid = course.get('courseid')
		courseno = course.get('courseno')
		subject = course.get('subject')
		title = course.get('title')
        # check if gpaid exists
		#cursor = connection.cursor()
		#cursor.execute(COURSE_EXIST, [courseid])
		#if cursor.rowcount == 0:
			#return Response("Record id does not exist", status = 400)
		cursor.execute(COURSE_UPDATE, [courseno, subject, title, courseid])
	return Response("Course record updated.", status = 200)

@api_view(['POST'])
def course_delete(request):
	courses = request.data.get('courses')
	cursor = connection.cursor()
	for course in courses:
		courseid = course.get('courseid')
	# check if gpaid exists
	#cursor = connection.cursor()
	#cursor.execute(COURSE_EXIST, [courseid])
	#if cursor.rowcount > 0:
		#return Response("Record id does not exist", status = 200)
		cursor.execute(COURSE_DELETE, [courseid])
	return Response("Gpa record deleted.", status = 200)	

# # ProfessorService:
# # Get /api/professorNames/
# # Input: None
# # Response: [List of professor names]
@csrf_exempt
def professor_list(request):
    if request.method == 'GET':
        professors = list(Professor.objects.values_list('name', flat = True)).distinct()
        return JsonResponse(professors, safe = False, status = 200)
        # if serializer.is_valid():
        # 	return JsonResponse(serializer.data, status = 200)
        # else:
        # 	return JsonResponse(serializer.errors, status = 400)
    return HttpResponse("Incorrect request method", status = 400)