from .models import Course, Gpa, Professor, User, CoursePrereqModel
from rest_framework import serializers

class CoursePrereqModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CoursePrereqModel
        fields=('Course','Prereq','AvgGpa')
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('courseid', 'courseno', 'subject', 'title')
    # normal serializer:    
    # courseid = serializers.IntegerField(read_only = True)
    # courseno = serializers.IntegerField()
    # subject = serializers.CharField(style={'base_template': 'textarea.html'})
    # title = serializers.CharField(style={'base_template': 'textarea.html'})
    # def create(self, validated_data):
    #     return Course.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.courseid = validated_data.get('courseid', instance.title)
    #     instance.courseno = validated_data.get('courseno', instance.courseno)
    #     instance.subject = validated_data.get('subject', instance.subject)
    #     instance.title = validated_data.get('title', instance.title)
class CourseNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('subject', 'courseno')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('subject',)

class CourseNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('courseno',)

class GpaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpa
        fields = ('term', 'value', 'courseid', 'classsize', 'year', 'professorid', 'gpaid')

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('name', 'department', 'professorid')

class ProfessorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('name',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'isadmin')