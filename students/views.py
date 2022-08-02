from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser




# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Student
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Student.objects.all()
    parser_classes = (MultiPartParser, FormParser)



class CourseViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Course
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Course.objects.all()



class CourseTeacherViewSet(viewsets.ModelViewSet):
    class Meta:
        model = CourseTeacher
    serializer_class = TeacherCourseSerializer
    permission_classes = [permissions.AllowAny]
    queryset = CourseTeacher.objects.all()


class CourseStudentViewSet(viewsets.ModelViewSet):
    class Meta:
        model = CourseTeacher
    serializer_class = StudentCourseSerializer
    permission_classes = [permissions.AllowAny]
    queryset = CourseStudent.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Student
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Teacher.objects.all()
def index(request):
    return render(request,'index.html')