from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

    filter_backends=[
        filters.SearchFilter,
    ]
    search_fields=['name']


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    filter_backends=[
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['department', 'seniority', 'is_active']
    search_fields = ['name', 'email', 'job_title']
    ordering_fields = ['salary', 'date_of_joining', 'name']