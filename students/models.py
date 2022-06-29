from email.mime import image
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    degree = models.PositiveSmallIntegerField()
    course_type = models.CharField(max_length=20,choices=(('online','online'),
                                            ('offline','offline')))