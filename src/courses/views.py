from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Course, Gpa, Professor, User
from .serializers import CourseSerializer, GpaSerializer, ProfessorSerializer, UserSerializer, SubjectSerializer, CourseNoSerializer, ProfessorNameSerializer, CourseNoSerializer

# UserService:
# POST /users/login/
# Input: {username, password}
# Response: 200 or 400
# {username, isAdmin}
@csrf_exempt
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = User.objects.filter(username = username, password = password)
		serializer = UserSerializer(user)
		return JSONResponse(serializer.data, safe = False, status = 200)
		# if user.is_valid():
		# 	serializer.save()
		# 	return JSONResponse(serializer.data, status = 200)
		# else:
		# 	return JSONReponse(serializer.data, status = 400)
	return HttpResponse("Incorrect request method", safe = False, status = 400)

# POST /users/register/
# Input: {username, password, isAdmin}
# Response: 200 or 400
@csrf_exempt
def user_register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		if len(User.objects.filter(username = username)) > 0:
			return HttpResponse("Username exists.", status = 400)
		password = request.POST.get('password')
		isAdmin = request.POST.get('isAdmin')
		new_user = User(username = username, password = password, isadmin = isAdmin)
		new_user.save()
		return HttpResponse("Successfully registered.", status = 200)

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
@csrf_exempt
def subject_list(request):
	if request.method == 'GET':
		subjects = Course.objects.order_by('subject').values('subject').distinct()
		serializer = SubjectSerializer(subjects, many=True)
		return JsonResponse(serializer.data, safe = False, status = 200)
		# if serializer.is_valid():
		# 	return JsonResponse(serializer.data, status = 200)
		# else:
		# 	return JsonResponse(serializer.errors, status = 400)
	return HttpResponse("Incorrect request method", status = 400)

# # Get /api/courseNumbers/
# # Input: None
# # Response: [List of course Numbers] (CS411, CS233, ..)
@csrf_exempt
def course_num_list(request):
    if request.method == 'GET':
        courses = Course.objects.values('subject', 'courseno')
        serializer = CourseNoSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe = False, status = 200)
        # if serializer.is_valid():
        # 	return JsonResponse(serializer.data, status = 200)
        # else:
        # 	return JsonResponse(serializer.errors, status = 400)
    return HttpResponse("Incorrect request method", status = 400)

# Get /api/gpa/
# Input: {year, dept}
# Output: [{course+gpa+professor}, ]
@csrf_exempt
def gpa_by_year_dept(request):
	if request.method == 'GET':
		year = request.GET.get('year')
		dept = request.GET.get('dept')
		course_sub = Course.objects.filter(subject = dept).values('courseid')			
		gpa_sub = Gpa.objects.filter(year = year, courseid__in = course_sub)
		serializer = GpaSerializer(gpa_sub, many=True)
		return JsonResponse(serializer.data, safe = False, status = 200)
			# if serializer.is_valid():
			# 	return JsonResponse(serializer.data, status = 200)
			# else:
			# 	return JsonResponse(serializer.errors, status = 400)
	return HttpResponse("Incorrect request method", status = 400)

# GPAService:
# GET /api/coursegpa/
# Input: {subject, number}
# Response: [List of GPA info] + (#professor_name,# subject, number)
@csrf_exempt
def gpa_list(request):
    if request.method == 'GET':
    	subject = request.GET.get('subject')
    	courseno = request.GET.get('number')
    	course_sub = Course.objects.filter(subject = subject, courseno = courseno).values('courseid')
    	gpa_sub = Gpa.objects.filter(courseid__in = course_sub)       
    	gpa_serializer = GpaSerializer(gpa_sub, many=True)
    	return JsonResponse(gpa_serializer.data, safe = False, status = 200)
    	# if serializer.is_valid() and pro_name_serializer.is_valid():
    	# 	return JsonResponse(gpa_serializer.data + pro_name_serializer.data, safe = False, status = 200)
    	# else:
    	# 	return JsonResponse(serializer.errors, status = 400)
    return HttpResponse("Incorrect request method", status = 400)	

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


# # ProfessorService:
# # Get /api/professorNames/
# # Input: None
# # Response: [List of professor names]
@csrf_exempt
def professor_list(request):
    if request.method == 'GET':
        professors = Professor.objects.values('name')
        serializer = ProfessorNameSerializer(professors, many=True)
        return JsonResponse(serializer.data, safe = False, status = 200)
        # if serializer.is_valid():
        # 	return JsonResponse(serializer.data, status = 200)
        # else:
        # 	return JsonResponse(serializer.errors, status = 400)
    return HttpResponse("Incorrect request method", status = 400)