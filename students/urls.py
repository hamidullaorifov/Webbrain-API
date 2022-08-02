from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('students',StudentViewSet,basename='student')
router.register('teachers',TeacherViewSet,basename='teacher')
router.register('courses',CourseViewSet,basename='course')
router.register('courseteacher',CourseTeacherViewSet,basename='courseteacher')
router.register('coursestudent',CourseStudentViewSet,basename='coursestudent')
urlpatterns = router.urls