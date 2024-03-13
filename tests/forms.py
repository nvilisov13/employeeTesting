from django import forms
from .models import EmployeesTest, Questions, AnswerQuestions, Employees, NominatedTests


class EmployeesTestForm(forms.ModelForm):
    class Meta:
        model = EmployeesTest
        fields = ['NameTest', 'DescriptionTest']


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['TextQuestion', 'ImageQuestion', 'TestNum']


class AnswerQuestionsForm(forms.ModelForm):
    class Meta:
        model = AnswerQuestions
        fields = ['TextAnswer', 'MarkAnswer', 'Question']


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['LastName', 'FirstName', 'Phone']


class NominatedTestsForm(forms.ModelForm):
    class Meta:
        model = NominatedTests
        fields = ['Employee', 'Test']
