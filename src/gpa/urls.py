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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', views.user_login),
    path('users/register', views.user_register),
    path('api/courses/', views.course_by_subject),
    path('api/subjects/', views.subject_list),
    path('api/courseNumbers/', views.course_num_list),
    path('api/gpa/', views.gpa_by_year_dept),
    path('api/coursegpa/', views.gpa_list),
    # path('coursegpa/new', views.gpa_new),
    # path('coursegpa/updated', views.gpa_updated),
    # path('coursegpa/deleted', views.gpa_deleted),
    path('api/professorNames/', views.professor_list), 
]
