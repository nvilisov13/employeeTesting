from django.shortcuts import render, redirect
from .forms import EmployeesTestForm, QuestionsForm
from .models import EmployeesTest


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logout.html')


def home(request):
    return render(request, 'index.html')


def add_tests_employees(request):
    if request.method == 'POST':
        form = EmployeesTestForm(request.POST)
        if form.is_valid():
            tests_employees = form.save()
            return redirect('add_questions', test_employees_id=tests_employees.id)
    else:
        form = EmployeesTestForm()
    header_template = {'title': 'Добавление теста', 'head': 'Добавление нового теста для сотрудников'}
    return render(request, 'add_data_db.html', {'form': form, 'header_template': header_template})


def add_questions(request, test_employees_id):
    test_employees = EmployeesTest.objects.get(id=test_employees_id)
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.instance.test_employees = test_employees
            form.save()
    else:
        form = QuestionsForm()
    header_template = {'title': 'Добавление вопросов', 'head': 'Добавление вопросов'}
    return render(request, 'add_data_db.html', {'form': form, 'header_template': header_template})
