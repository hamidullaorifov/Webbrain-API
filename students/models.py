from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    # title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images",null=True,blank=True)
    degree = models.PositiveSmallIntegerField()
    # course_type = models.CharField(max_length=20,choices=(('online','online'),
    
    def __str__(self):
        return self.name+' '+self.surname                                       # ('offline','offline')))



class Teacher(models.Model):
    fullname = models.CharField(max_length=255)
    seniority = models.CharField(max_length=127)

    def __str__(self):
        return self.fullname



class Course(models.Model):
    name = models.CharField(max_length=200)
    # students = models.ManyToManyField(Student,related_name='cources',through='CourseStudent')
    # teachers = models.ForeignKey(CourseTeacher,related_name='cources',through='CourseTeacher')
    type = models.CharField(max_length=20,choices=(('online','online'),
                                                    ('offline','offline')))
    
    # teachers = models.ManyToManyField(Teacher,related_name='courses')                                   
    def __str__(self):
        return self.name

class CourseTeacher(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
class CourseStudent(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
