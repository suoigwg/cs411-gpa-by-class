from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Course, Gpa, Professor, User
from .serializers import CourseSerializer, GpaSerializer, ProfessorSerializer, UserSerializer

def home_view(*args, **kwargs): # *args, **kwargs
    #print(args, kwargs)
    #print(request.user)
	return HttpResponse("<h1>UIUC GPA History and Class Prereq Visualizer</h1>")

@csrf_exempt
def gpa_by_year_dept(request):
	if request.method == 'GET':
		year = request.data.get('year')
		dept = request.data.get('dept')
		if year and dept:
			gpa_sub = Gpa.objects.filter(year = year, course__subject = dept)
			if gpa_sub.exists():
				serializer = GpaSerializer(gpa_sub, many=True)
				JsonResponse(serializer.data, safe = False, status = 200)
			else:
				return JsonResponse(serializer.errors, status = 400)
	return JsonResponse(serializer.errors, status = 400)

# GPAService:
# GET /api/coursegpa/
# Input: {subject, number}
# Response: [List of GPA info] + (professor_name, subject, number)
@csrf_exempt
def gpa_list(request):
    if request.method == 'GET':
    	subject = request.data.get('subject')
    	courseno = request.data.get('number')
    	gpa_sub = Gpa.objects.filter(courseid = course_sub, course__subject = subject, course__courseno = courseno).values_list('professor__professor_name')        
    	serializer = GpaSerializer(gpa_sub, many=True)
    	return JsonResponse(serializer.data, safe = False, status = 200)
    else:
    	return JsonResponse(serializer.errors, status = 400)

# @csrf_exempt
# def gpa_new(request):
# 	if request.method == 'POST'
# 	return Response("Get gpa new post request")

# @csrf_exempt
# def gpa_updated(request):
# 	if request.method == 'POST'
# 		return Response("Get gpa updated post request")
# 	else
# 		return JSONResponse(serializer.errors, status = 400)

# @csrf_exempt
# def gpa_deleted(request):
# 	if request.method == 'POST'

# 		return Response("Get gpa deleted post request")

# # Get /api/courseNumbers/
# # Input: None
# # Response: [List of course Numbers] (CS411, CS233, ..)
@csrf_exempt
def course_num_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe = False, status = 200)
    else:
    	return JsonResponse(serializer.errors, status = 400)

# # ProfessorService:
# # Get /api/professorNames/
# # Input: None
# # Response: [List of professor names]
@csrf_exempt
def professor_list(request):
    if request.method == 'GET':
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return JsonResponse(serializer.data, safe = False, status = 200)
    else:
    	return JsonResponse(serializer.errors, status = 400)
