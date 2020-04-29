from django.contrib import admin

from .models import Course, Gpa, Professor, User, CoursePrereqModel

admin.site.register(Course)
admin.site.register(Gpa)
admin.site.register(Professor)
admin.site.register(User)
admin.site.register(CoursePrereqModel)