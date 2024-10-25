from django_filters import FilterSet, CharFilter, ChoiceFilter
from .models import School, Classroom, Teacher, Student

class SchoolFilter(FilterSet):
#school list can filter with name
    name = CharFilter(lookup_expr='icontains')
    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(FilterSet):
    #classroom list can filter with school
    school = CharFilter(field_name='school__name', lookup_expr='icontains')

    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(FilterSet):
    #teacher list can filter with school, classroon, firstname, lastname, gender
    school = CharFilter(field_name='school__name', lookup_expr='icontains')
    name = CharFilter(lookup_expr='icontains')
    lastname = CharFilter(lookup_expr='icontains')
    gender = ChoiceFilter(choices=[('M', 'Male'), ('F', 'Female')])
    classroom = CharFilter(field_name='classrooms__school__name', lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'name', 'lastname', 'gender']

class StudentFilter(FilterSet):
    #student list can filter with school, classroon, firstname, lastname, gender
    school = CharFilter(field_name='school__name', lookup_expr='icontains')
    name = CharFilter(lookup_expr='icontains')
    lastname = CharFilter(lookup_expr='icontains')
    gender = ChoiceFilter(choices=[('M', 'Male'), ('F', 'Female')])
    classroom = CharFilter(field_name='classroom__school__name', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'name', 'lastname', 'gender']
