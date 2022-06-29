from dataclasses import fields
from random import choices
from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    title = serializers.CharField()
    image = serializers.ImageField()
    degree = serializers.IntegerField()
    course_type = serializers.ChoiceField(choices=(('online','online'),
                                                'offline','offline'))
    class Meta:
        model=Student
        fields = '__all__'