from rest_framework import viewsets
from apis.models import Classroom
from apis.serializers import ClassroomSerializer
from apis.filters import ClassroomFilter
from django_filters.rest_framework import DjangoFilterBackend

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter
