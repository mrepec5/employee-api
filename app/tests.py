from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Department, Employee


class EmployeeApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

        self.department = Department.objects.create(name="IT", location="Warsaw")
        self.employee = Employee.objects.create(
            name="Jan Testowy",
            email="jan@test.pl",
            department=self.department,
            job_title="Dev",
            salary=8000.00,
            date_of_joining="2024-01-01"
        )

        self.employee_list_url = reverse('employee-list')

    def test_models_string_representation(self):
        self.assertEqual(str(self.department), "IT")
        self.assertEqual(str(self.employee), "Jan Testowy (Dev)")

    def test_api_security_rejects_anonymous(self):
        response = self.client.get(self.employee_list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_list_employees_authenticated(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.employee_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['department_name'], "IT")

    def test_create_employee(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "name": "Anna Nowa",
            "department": self.department.id,
            "date_of_joining": "2024-02-01",
            "job_title": "HR",
            "seniority": "JR"
        }

        response = self.client.post(self.employee_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)