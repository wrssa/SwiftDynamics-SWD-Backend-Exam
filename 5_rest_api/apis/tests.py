from django.test import TestCase
from django.urls import reverse
from .models import School, Classroom, Teacher, Student

class SchoolViewSetTests(TestCase):
    def setUp(self):
        self.school = School.objects.create(name="Test access")
    
    def test_login_success(self):
        "---Test successful login---"
        response = self.client.post('v1', {
            'username': 'admin',
            'password': 'admin'
        })  # Send as form data
        self.assertEqual(response.status_code, 200)  # Check for success

    def test_create_school(self):
        url = reverse('v1/schools') 
        data = {'name': 'Mahidol University',
                'name_abbr': 'MU',
                'address': ' '}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # 201 = Created
        self.assertEqual(School.objects.count(), 2)  # Check if one more school is added
        self.assertEqual(School.objects.last().name, 'Mahidol University')

    def test_update_school(self):
        url = reverse('v1/schools', kwargs={'pk': self.school.name})
        data = {'name': 'Mahidol University',
                'name_abbr': 'MU',
                'address': 'Salaya Nakhonprathom, Thailand'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)  
        self.school.refresh_from_db()
        self.assertEqual(self.school.name, 'Updated School')

    def test_delete_school(self):
        url = reverse('v1/schools', kwargs={'pk': self.school.name})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)  # make sure getting 204 No Content
        self.assertEqual(School.objects.count(), 0)  # Check if the school is deleted

    def test_view_schools_list(self):
        url = reverse('v1/schools')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 OK
        # self.assertEqual(len(response.data), 1)

class ClassroomViewSetTests(TestCase):
    def setUp(self):
        self.school = School.objects.create(name="Test School")
        self.classroom = Classroom.objects.create(school=self.school, grade="1", section="2", id="102")

    def test_create_classroom(self):
        url = reverse('v1/classrooms')
        data = {
            'school': self.school.pk,
            'grade': '2',
            'section': '3',
            'id': '203'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # 201 = Created
        self.assertEqual(Classroom.objects.count(), 2)  # Check if one more classroom is added

    def test_update_classroom(self):
        url = reverse('v1/classrooms', kwargs={'pk': self.classroom.pk}) 
        data = {
            'school': self.school.pk,
            'grade': '3',
            'section': 'C'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)  
        self.classroom.refresh_from_db()
        self.assertEqual(self.classroom.grade, '3')

    def test_delete_classroom(self):
        url = reverse('v1/classrooms', kwargs={'pk': self.classroom.pk})  # Adjust based on your routing
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)  # 204 No Content
        self.assertEqual(Classroom.objects.count(), 0)  # Check if the classroom is deleted

    def test_view_classrooms_list(self):
        url = reverse('v1/classrooms')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TeacherViewSetTests(TestCase):
    def setUp(self):
        self.school = School.objects.create(name="Test School")
        self.teacher = Teacher.objects.create(name="Crybaby", lastname="Secret", gender="M", school=self.school)

    def test_create_teacher(self):
        url = reverse('v1/teachers') 
        data = {
            'name': 'John',
            'lastname': 'M',
            'gender': 'M',
            'school': self.school.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  
        self.assertEqual(Teacher.objects.count(), 2)  

    def test_update_teacher(self):
        url = reverse('v1/teachers', kwargs={'pk': self.teacher.pk})
        data = {
            'name': 'Crybaby',
            'lastname': 'Secret',
            'gender': 'F',
            'school': self.school.pk
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)  

    def test_delete_teacher(self):
        url = reverse('v1/teachers', kwargs={'pk': self.teacher.pk}) 
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Teacher.objects.count(), 0) 

    def test_view_teachers_list(self):
        url = reverse('v1/teachers') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) 


class StudentViewSetTests(TestCase):
    def setUp(self):
        self.school = School.objects.create(name="Test School")
        self.classroom = Classroom.objects.create(school=self.school, grade="1", section="7")
        self.student = Student.objects.create(name="Johnson", lastname="Baby", gender='F', classroom=self.classroom, school=self.school)

    def test_create_student(self):
        url = reverse('v1/students') 
        data = {
            'name': 'Warisa',
            'lastname': 'Kong',
            'gender': 'F',
            'classroom': self.classroom.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_update_student(self):
        url = reverse('v1/students', kwargs={'pk': self.student.pk})
        data = {
            'name': 'Johnson',
            'lastname': 'Babylove',
            'gender': 'F',
            'classroom': self.classroom.pk
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)  
        self.student.refresh_from_db() # recheck the edited lastname 
        self.assertEqual(self.student.lastname, 'Babylove')

    def test_delete_student(self):
        url = reverse('v1/students', kwargs={'pk': self.student.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)  
        self.assertEqual(Student.objects.count(), 0) 

    def test_view_students_list(self):
        url = reverse('v1/students') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 OK