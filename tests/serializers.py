from .models import EmployeesTest, Questions, AnswerQuestions
from rest_framework import serializers


class EmployeesTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesTest
        fields = ('NameTest', 'DescriptionTest')


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('TextQuestion', 'ImageQuestion')


class AnswerQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestions
        fields = ('TextAnswer', 'MarkAnswer', 'Question')
