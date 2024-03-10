from django import forms
from .models import EmployeesTest, Questions


class EmployeesTestForm(forms.ModelForm):
    class Meta:
        model = EmployeesTest
        fields = '__all__'


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'
