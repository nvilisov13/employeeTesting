from .models import EmployeesTest
from .serializers import EmployeesTestSerializer
from rest_framework import viewsets


class EmployeesTestViewSet(viewsets.ModelViewSet):
    queryset = EmployeesTest.objects.all()
    serializer_class = EmployeesTestSerializer
