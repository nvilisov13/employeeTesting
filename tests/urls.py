from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . import drfviews
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'drf_employees_test', drfviews.EmployeesTestViewSet)
router.register(r'drf_questions', drfviews.QuestionViewSet)
router.register(r'drf_answers_question', drfviews.AnswersQuestionViewSet)
router.register(r'drf_employees', drfviews.EmployeesViewSet)
router.register(r'drf_nominated_tests', drfviews.NominatedTestsViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('add_tests_employees', views.add_tests_employees, name='add_tests_employees'),
    path('add_questions', views.add_questions, name='add_questions'),
    path('add_answers_questions', views.add_answers_questions, name='add_answers_questions'),
    path('add_employees', views.add_employees, name='add_employees'),
    path('add_nominated_test', views.add_nominated_test, name='add_nominated_test'),
    path('take_test', views.take_test, name='take_test'),
    path('test/<int:id_test>', views.test),
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls')),
]
