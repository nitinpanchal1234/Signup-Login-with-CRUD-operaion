from django.shortcuts import render, redirect
from .models import Signup
from .models import Employee
from django.http import HttpResponse, HttpResponseBadRequest
# from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')
def signup_action(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        signup_data = Signup.objects.create(name=name, email=email, password=password, mobile=mobile)

        emp_data = Employee.objects.all()
        dict = {
            'emp_data' : emp_data
        }
        return render(request, 'login.html', dict)
    
def login(request):
    return render(request, 'login.html')
def login_action(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            login_data = Signup.objects.get(email=email, password=password)
            emp_data_1 = [login_data]
            dict_1 = {
                'emp_data_1' : emp_data_1
            }
            return render(request, 'show.html', dict_1)
        except Signup.DoesNotExist:
            return HttpResponse('User does not found please signup and login again')
            redirect('/login')

def add_emp(request):
    return render(request, 'add_emp.html')
def add_emp_action(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        salary = request.POST['salary']
        bonus = request.POST['bonus']

        add_emp_data = Employee.objects.create(name=name, email=email, password=password, mobile=mobile, salary=salary, bonus=bonus )

        emp_data = Employee.objects.all()
        dict = {
            'emp_data' : emp_data
        }
        return render(request, 'view_all_emp.html', dict)
    
def view_all_emp(request):
    emp_data = Employee.objects.all()
    dict = {
        'emp_data' : emp_data
    }
    return render(request, 'view_all_emp.html', dict)

def update_emp(request, id):
    emp_data = Employee.objects.get(id=id)
    dict = {
        'emp_data' : emp_data
        }
    return render(request, 'update_emp.html', dict)
def update_emp_action(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        salary = request.POST['salary']
        bonus = request.POST['bonus']

        add_emp_data = Employee.objects.get(id=id)

        add_emp_data.name = name
        add_emp_data.email = email
        add_emp_data.password = password
        add_emp_data.mobile = mobile
        add_emp_data.salary = salary
        add_emp_data.bonus = bonus
        add_emp_data.save()

        emp_data = Employee.objects.all()
        dict = {
            'emp_data' : emp_data
            }
        return render(request, 'view_all_emp.html', dict)

def delete_emp(request, id):
    if request.method == 'POST':
        add_emp_data = Employee.objects.get(id=id)
        add_emp_data.delete()

        emp_data = Employee.objects.all()
        dict = {
            'emp_data' : emp_data
        }
        return render(request, 'view_all_emp.html', dict)








