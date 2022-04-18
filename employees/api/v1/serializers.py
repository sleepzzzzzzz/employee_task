from rest_framework import serializers

from employees.models import Employee, Position, PaidSalary


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class PaidSalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = PaidSalary
        fields = '__all__'
