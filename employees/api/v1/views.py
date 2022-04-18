from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from employees.api.v1.filters import EmployeeFilter
from employees.api.v1.mixins import ManagerPermissionMixin
from employees.api.v1.permissions import IsManagerPermission
from employees.api.v1.serializers import EmployeeSerializer, PaidSalarySerializer, PositionSerializer
from employees.models import Employee, PaidSalary, Position


class EmployeeViewSet(ManagerPermissionMixin, ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
    permission_classes = [IsAuthenticated, IsManagerPermission]


class PaidSalaryViewSet(ModelViewSet):
    queryset = PaidSalary.objects.all()
    serializer_class = PaidSalarySerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated, IsAdminUser]


class PositionViewSet(ManagerPermissionMixin, ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated, IsManagerPermission]
