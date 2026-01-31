from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=254, unique=True)
    location = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    SENIORITY_CHOICES = [
        ('JR', 'Junior'),
        ('MID', 'Mid-Level'),
        ('SR', 'Senior'),
        ('MGR', 'Manager'),
    ]

    name = models.CharField(max_length=254, db_index=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    job_title = models.CharField(max_length=254, default='Specialist')
    seniority = models.CharField(max_length=3, choices=SENIORITY_CHOICES, default='JR')
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_of_joining = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.job_title})'
