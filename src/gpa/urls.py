"""gpa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from courses import views
from courses import rest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', views.user_login),
    path('users/register/', views.user_register),
    path('api/courses/', views.course_by_subject),
    path('api/subjects/', views.getAllDpetAbbr),
    path('api/courseNumbers/', views.course_num_list),
    path('api/gpa/', views.getGPAByDeptAndYear),
    path('api/avggpa/', views.getAvgGPA),
    path('api/coursegpa/', views.getCourseGPA),
    path('api/coursegpa/new/', views.gpa_new),
    path('api/coursegpa/updated/', views.gpa_update),
    path('api/coursegpa/deleted/', views.gpa_delete),
    path('api/courses/new/', views.course_new),
    path('api/courses/updated/', views.course_update),
    path('api/courses/deleted/', views.course_delete),
    path('api/professorNames/', views.professor_list),
    path('api/subjects/', rest.getAllDpetAbbr),
    path('api/prof/<str:prefix>', rest.searchInstructor),
    path('gpa/<int:year>/<str:dept>', rest.getGPAByDeptAndYear),
    path('gpa/<str:course>', rest.getCourseGPA),
    path('gpa/list/<int:year>', rest.getGPAByYear),
    path('gpa/avg/<int:year>', rest.getAvgGPA),
    path('gpa/instructor/<str:name>', rest.getInstructorGPA),
    path('api/courseprereq/',views.get_course_prereq),

]
