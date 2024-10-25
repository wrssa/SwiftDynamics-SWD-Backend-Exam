from rest_framework import routers, serializers, viewsets
from apis.models import Teacher
from apis.serializers import TeacherSerializer
from apis.filters import TeacherFilter
from django_filters.rest_framework import DjangoFilterBackend

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter