from django.db import models


class Courses(models.Model):
    subject = models.CharField(max_length=5)
    number = models.IntegerField()
    title = models.CharField(max_length=100)

    class Meta:
        unique_together = ["subject", "number"]


class GPA(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    year = models.IntegerField()
    term = models.CharField(max_length=10)
    professor = models.CharField(max_length=50)
    gpa = models.FloatField()
    class_size = models.IntegerField()

    class Meta:
        unique_together = ["course", "year", "term", "professor"]
