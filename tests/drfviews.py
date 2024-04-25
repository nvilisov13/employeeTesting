from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import EmployeesTest, Questions, AnswerQuestions, Employees, NominatedTests
from .serializers import EmployeesTestSerializer, QuestionsSerializer, AnswerQuestionsSerializer, EmployeesSerializer, \
    NominatedTestsSerializer
from rest_framework import viewsets


class EmployeesTestViewSet(viewsets.ModelViewSet):
    queryset = EmployeesTest.objects.all()
    serializer_class = EmployeesTestSerializer
    permission_classes = (IsAuthenticated,)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=True)
    def question_count(self, request, pk=None):
        question_count = Questions.objects.filter(TestNum=pk).count()
        return Response({'QuestionCount': question_count})

    @action(methods=['get'], detail=True)
    def questions_test(self, request, pk=None):
        questions = Questions.objects.filter(TestNum=pk)
        questions_list = {counter + 1: (qns.TextQuestion, qns.ImageQuestion.url if qns.ImageQuestion != '' else None)
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
    permission_classes = (IsAuthenticated,)


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=True)
    def nom_tests(self, request, pk=None):
        nominated_tests = NominatedTests.objects.filter(Employee=pk)
        nominated_tests_list = {}
        for counter, nts in enumerate(nominated_tests):
            nominated_tests_list = {counter: {'id': nts.id, 'MarksTest': nts.MarksTest,
                                              'SinceDateTime': nts.SinceDateTime, 'DuringDateTime': nts.DuringDateTime,
                                              'Employee_id': nts.Employee_id, 'Test_id': nts.Test_id}
                                    }
        return Response(nominated_tests_list)


class NominatedTestsViewSet(viewsets.ModelViewSet):
    queryset = NominatedTests.objects.all()
    serializer_class = NominatedTestsSerializer
    permission_classes = (IsAuthenticated,)
