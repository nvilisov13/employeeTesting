from rest_framework.decorators import action
from rest_framework.response import Response

from .models import EmployeesTest, Questions, AnswerQuestions
from .serializers import EmployeesTestSerializer, QuestionsSerializer, AnswerQuestionsSerializer
from rest_framework import viewsets


class EmployeesTestViewSet(viewsets.ModelViewSet):
    queryset = EmployeesTest.objects.all()
    serializer_class = EmployeesTestSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    @action(methods=['get'], detail=True)
    def question_count(self, request, pk=None):
        question_count = Questions.objects.filter(TestNum=pk).count()
        return Response({'QuestionCount': question_count})

    @action(methods=['get'], detail=True)
    def questions_test(self, request, pk=None):
        questions = Questions.objects.filter(TestNum=pk)
        questions_list = {counter + 1: (qns.TextQuestion, qns.ImageQuestion if qns.ImageQuestion != '' else None)
                          for counter, qns in enumerate(questions)}
        return Response(questions_list)

    @action(methods=['get'], detail=True)
    def question_answers(self, request, pk=None):
        answer = AnswerQuestions.objects.filter(Question=pk)
        answers = {counter: (ans.TextAnswer, ans.MarkAnswer) for counter, ans in enumerate(answer)}
        return Response(answers)


class AnswersQuestionViewSet(viewsets.ModelViewSet):
    queryset = AnswerQuestions.objects.all()
    serializer_class = AnswerQuestionsSerializer
