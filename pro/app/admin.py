from django.contrib import admin
from .models import Signup
from .models import Employee
# Register your models here.

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password', 'mobile']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password', 'mobile', 'salary', 'bonus']
