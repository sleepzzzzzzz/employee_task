import django_filters

from employees.models import Employee


class EmployeeFilter(django_filters.FilterSet):

    class Meta:
        model = Employee
        fields = ['position__level']
