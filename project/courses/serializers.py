from rest_framework import serializers
from .models import *


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'subject', 'number', 'title')


class GPASerializer(serializers.ModelSerializer):
    class Meta:
        model = GPA
        fields = ('id', 'course', 'year', 'term', 'professor', 'gpa', 'class_size')
