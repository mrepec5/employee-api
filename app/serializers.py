from rest_framework import serializers
from app.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields = ['id', 'name', 'location']


class EmployeeSerializer(serializers.ModelSerializer):
    department_name=serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model=Employee
        fields = [
            'id',
            'name',
            'email',
            'department',
            'department_name',
            'job_title',
            'seniority',
            'salary',
            'date_of_joining',
            'is_active'
        ]
