from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import EmployeesTest, Questions, AnswerQuestions, Employees, NominatedTests


@admin.register(EmployeesTest)
class EmployeesTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameTest', 'DescriptionTest')
    search_fields = ['NameTest']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    fields = ['TextQuestion', 'ImageQuestion', 'ImageQuestionPost', 'TestNum']
    readonly_fields = ['ImageQuestionPost']
    list_display = ('id', 'TextQuestion', 'ImageQuestionPost', 'test_name')
    list_filter = ['TestNum__NameTest']
    search_fields = ['TestNum__NameTest']

    @admin.display(description='Номер теста', ordering='TestNum__NameTest')
    def test_name(self, obj):
        return obj.TestNum.NameTest

    @admin.display(description='Изображение вопроса', ordering='ImageQuestion')
    def ImageQuestionPost(self, question: Questions):
        if question.ImageQuestion:
            return mark_safe(f"<img src='{question.ImageQuestion.url}' width=100px")
        else:
            return "Без изображения"


@admin.register(AnswerQuestions)
class AnswerQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'TextAnswer', 'MarkAnswer', 'Question')


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'LastName', 'FirstName', 'Phone', 'TelegramID')


@admin.register(NominatedTests)
class NominatedTestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'MarksTest', 'SinceDateTime', 'DuringDateTime', 'Employee', 'Test')
