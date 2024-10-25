from rest_framework import routers, serializers, viewsets
from apis.models import Student
from apis.serializers import StudentSerializer
from apis.filters import StudentFilter
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter