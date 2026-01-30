from django.contrib import admin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'job_title', 'seniority', 'salary', 'is_active')
    list_filter = ('department', 'seniority', 'is_active')
    search_fields = ('name', 'email')