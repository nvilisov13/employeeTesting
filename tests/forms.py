from django import forms
from .models import EmployeesTest


class EmployeesTestForm(forms.ModelForm):
    class Meta:
        model = EmployeesTest
        fields = '__all__'
