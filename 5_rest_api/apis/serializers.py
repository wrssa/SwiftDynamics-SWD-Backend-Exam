from rest_framework import serializers
from .models import School, Classroom, Teacher, Student

#code here

class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['name', 'name_abbr', 'address', 'classroom_count', 'teacher_count', 'student_count']
    
    #count of classroom
    def get_classroom_count(self, obj):
        return obj.classrooms.count()
    
    #count of teacher
    def get_teacher_count(self, obj):
        sum = 0
        for classroom in obj.classrooms.all():
            sum += classroom.teachers.count()
        return sum

    #count of student
    def get_student_count(self, obj):
        sum = 0
        for classroom in obj.classrooms.all():
            sum += classroom.students.count()
        return sum

class ClassroomSerializer(serializers.ModelSerializer):
    #classroom detail in detail want to know list of teachers and students
    teachers = serializers.StringRelatedField(many=True, read_only=True)
    students = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Classroom
        fields = ['school', 'grade', 'section', 'teachers', 'students', 'id']

class TeacherSerializer(serializers.ModelSerializer):
    classroom = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ['name', 'lastname', 'gender', 'classroom', 'school']

class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Student
        fields = ['name', 'lastname', 'gender', 'classroom', 'school']
