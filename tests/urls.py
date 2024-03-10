from django.urls import path, include
from . import views, templatesforms
from django.contrib.auth import views as auth_views
from . import drfviews
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'drf_employees_test', drfviews.EmployeesTestViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('add_employees_test', templatesforms.add_employees_test, name='add_employees_test'),
    path('add_test', views.add_test, name='add_test'),
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls')),
    path('add_test_form', views.add_test_form, name='add_test_form'),
]
