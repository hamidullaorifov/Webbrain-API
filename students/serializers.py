from django.forms.models import model_to_dict
from pkg_resources import require
from .models import *
from rest_framework import serializers
from django.conf import settings



class TeacherCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTeacher
        fields = '__all__'

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudent
        fields = '__all__'



class TeacherSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    
    def get_courses(self,obj):
        courses = [model_to_dict(cs.course,fields=['id','name','type']) for cs in CourseTeacher.objects.filter(teacher=obj)]
        return courses
    class Meta:
        model=Teacher
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    degree = serializers.IntegerField()
    courses = serializers.SerializerMethodField()
    
    def get_courses(self,obj):
        courses = [model_to_dict(cs.course,fields=['id','name','type']) for cs in CourseStudent.objects.filter(student=obj)]
        return courses

    class Meta:
        model=Student
        fields = '__all__'
