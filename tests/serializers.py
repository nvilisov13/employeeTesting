from .models import EmployeesTest
from rest_framework import serializers


class EmployeesTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesTest
        fields = ('__all__')
