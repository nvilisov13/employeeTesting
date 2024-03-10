from django.shortcuts import render
from .models import EmployeesTest


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logout.html')


def home(request):
    return render(request, 'index.html')


def add_test(request):
    return render(request, 'add_test_form/add_test.html')


def add_test_form(request):
    if request.method == 'POST':
        name_test = request.POST.get('NameTest').strip()
        description_test = request.POST.get('DescriptionTest').strip()
        if name_test != '':
            employees_test = EmployeesTest()
            employees_test.NameTest = name_test
            employees_test.DescriptionTest = description_test
            employees_test.save()
    return render(request, 'add_test_form/add_test.html')
