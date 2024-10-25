from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import SchoolViewSet
from apis.views.v1.classroom import ClassroomViewSet
from apis.views.v1.student import StudentViewSet
from apis.views.v1.teacher import TeacherViewSet


router = DefaultRouter()
# Register view sets with Router
router.register(r'schools', SchoolViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
