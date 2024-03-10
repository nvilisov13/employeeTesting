from django.contrib import admin
from .models import EmployeesTest, Questions, AnswerQuestions, Employees, NominatedTests


class EmployeesTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'NameTest', 'DescriptionTest']


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'TextQuestion', 'ImageQuestion', 'TestNum']


class AnswerQuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'TextAnswer', 'MarkAnswer', 'Question']


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['id', 'LastName', 'FirstName', 'Phone']


class NominatedTestsAdmin(admin.ModelAdmin):
    list_display = ['id', 'MarksTest', 'DateTimePassing', 'TravelTime', 'Employee', 'Test']


admin.site.register(EmployeesTest, EmployeesTestAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(AnswerQuestions, AnswerQuestionsAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(NominatedTests, NominatedTestsAdmin)
