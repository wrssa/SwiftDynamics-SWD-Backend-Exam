from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    name_abbr = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Classroom(models.Model):
    # Classroom is in the school
    school = models.ForeignKey(School, related_name="classrooms", on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    section = models.CharField(max_length=1)
    id = models.CharField(max_length=3, primary_key=True, null=False)

    def __str__(self):
        return f"{self.grade}/{self.section}"

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'),('F','Female')])
    classroom = models.ManyToManyField(Classroom, related_name="teachers")
    school = models.OneToOneField(School, related_name="teacher", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'),('F','Female')])
    classroom = models.OneToOneField(Classroom, related_name="students", on_delete=models.CASCADE)
    school = models.OneToOneField(School, related_name="students", on_delete=models.CASCADE)

    def __str__(self):
        return self.name