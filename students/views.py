from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import StudentSerializer
from .models import Student



# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Student
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Student.objects.all()
