from django.contrib import admin
from .models import Student,Course,Teacher,CourseStudent,CourseTeacher
# Register your models here.


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(CourseTeacher)
admin.site.register(CourseStudent)