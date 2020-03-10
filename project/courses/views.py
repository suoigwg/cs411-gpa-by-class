from django.shortcuts import render
from rest_framework import generics
from .serializers import CoursesSerializer
from .models import Courses


class CoursesView(generics.ListCreateAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
