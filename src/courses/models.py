from django.db import models
from djongo import models as m 
# from djongo.models.indexes import TextIndex

#djongo
class CoursePrereqModel(m.Model): #collection name
    Course=m.TextField()
    Prereq=m.TextField()
    AvgGpa=m.CharField(max_length=50)
    # class Meta:
    #     indexes = [
    #         TextIndex(fields=['Course'])
    #     ]

class Course(models.Model):
    courseid = models.AutoField(db_column='CourseId', primary_key=True)  # Field name made lowercase.
    courseno = models.IntegerField(db_column='CourseNo', blank=True, null=True)  # Field name made lowercase.
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course'

class Professor(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    department = models.TextField(db_column='Department', blank=True, null=True)  # Field name made lowercase.
    professorid = models.AutoField(db_column='ProfessorId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Professor'

class Gpa(models.Model):
    term = models.TextField(db_column='Term', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId', blank=True, null=True)  # Field name made lowercase.
    classsize = models.IntegerField(db_column='ClassSize', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    professorid = models.IntegerField(db_column='ProfessorId', blank=True, null=True)  # Field name made lowercase.
    gpaid = models.AutoField(db_column='GPAId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPA'

class User(models.Model):
    username = models.TextField(db_column='UserName', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    isadmin = models.IntegerField(db_column='IsAdmin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'