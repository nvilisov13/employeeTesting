from django.shortcuts import render, redirect
from .forms import EmployeesTestForm, QuestionsForm, AnswerQuestionsForm, EmployeesForm, NominatedTestsForm
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
            form.save()
            return redirect('add_questions')
    else:
        form = EmployeesTestForm()
    header_template = {'title': 'Добавление теста', 'head': 'Добавление нового теста для сотрудников',
                       'next_form': 'Вопросов'}
    return render(request, 'add_data_db.html', {'form': form, 'header_template': header_template})


def add_questions(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestionsForm()
    header_template = {'title': 'Добавление вопросов', 'head': 'Добавление вопросов', 'next_form': 'Ответов на вопросы'}
    return render(request, 'add_data_db.html', {'form': form, 'header_template': header_template})


def add_answers_questions(request):
    if request.method == 'POST':
        form = AnswerQuestionsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AnswerQuestionsForm()
    header_template = {'title': 'Добавление ответов', 'head': 'Добавление ответов на вопросы',
                       'next_form': 'Новых тестов для сотрудников'}
    return render(request, 'add_data_db.html', {'form': form, 'header_template': header_template})


def add_employees(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_nominated_test')
    else:
        form = EmployeesForm()
    header_template = {'title': 'Добавление сотрудника', 'head': 'Добавление новых сотрудников для прохождения тестов',
                       'next_form': 'Назначение новых тестов сотрудникам'}
    return render(request, 'add_data_db.html', {'form': form, 'header_template': header_template})


def add_nominated_test(request):
    if request.method == 'POST':
        form = NominatedTestsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_employees')
    else:
        form = NominatedTestsForm()
    header_template = {'title': 'Назначение теста', 'head': 'Назначение тестов для сотрудников',
                       'next_form': 'Добавление новых сотрудников для прохождения тестов'}
    return render(request, 'add_data_db.html', {'form': form, 'header_template': header_template})


def take_test(request):
    tests_employees = EmployeesTest.objects.all()
    return render(request, 'show_tests.html', {'tests_employees': tests_employees})


def test(request, id_test):
    return render(request, 'test.html', {'test': id_test})
