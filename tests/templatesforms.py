from django.shortcuts import render
from .forms import EmployeesTestForm


def add_employees_test(request):
    if request.method == 'POST':
        form = EmployeesTestForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeesTestForm()
    return render(request, 'add_test_form/add_employees_test.html', {'form': form})
