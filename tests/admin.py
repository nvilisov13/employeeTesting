from django.contrib import admin
from .models import EmployeesTest, Questions, AnswerQuestions, Employees, NominatedTests


@admin.register(EmployeesTest)
class EmployeesTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameTest', 'DescriptionTest')
    search_fields = ['NameTest']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    fields = ('TextQuestion', 'ImageQuestion', 'TestNum')
    list_display = ('id', 'TextQuestion', 'ImageQuestion', 'test_name')
    list_filter = ['TestNum__NameTest']
    search_fields = ['TestNum__NameTest']

    @admin.display(description='Номер теста', ordering='TestNum__NameTest')
    def test_name(self, obj):
        return obj.TestNum.NameTest


@admin.register(AnswerQuestions)
class AnswerQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'TextAnswer', 'MarkAnswer', 'Question')


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'LastName', 'FirstName', 'Phone')


@admin.register(NominatedTests)
class NominatedTestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'MarksTest', 'DateTimePassing', 'TravelTime', 'Employee', 'Test')
