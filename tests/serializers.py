from .models import EmployeesTest, Questions, AnswerQuestions, Employees, NominatedTests
from rest_framework import serializers


class EmployeesTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesTest
        fields = ('id', 'NameTest', 'DescriptionTest')


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('TextQuestion', 'ImageQuestion')


class AnswerQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestions
        fields = ('TextAnswer', 'MarkAnswer', 'Question')


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'FirstName', 'LastName', 'Phone', 'TelegramID')


class NominatedTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NominatedTests
        fields = ('MarksTest', 'SinceDateTime', 'DuringDateTime', 'Employee', 'Test')
