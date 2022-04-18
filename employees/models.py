from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='first name')
    last_name = models.CharField(max_length=64, verbose_name='last name')
    patronymic = models.CharField(max_length=64, verbose_name='patronymic', null=True, blank=True)
    start_date = models.DateTimeField(verbose_name='employment start date')
    salary = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    position = models.ForeignKey(
        to='Position',
        on_delete=models.SET_NULL,
        verbose_name='current position',
        null=True,
    )
    manager = models.ForeignKey(
        to='Employee',
        on_delete=models.SET_NULL,
        verbose_name='manager',
        null=True,
        blank=True
    )

    @property
    def full_name(self):
        if self.patronymic:
            name = f'{self.last_name} {self.first_name} {self.patronymic}'
        else:
            name = f'{self.first_name} {self.last_name}'

        return name

    def __str__(self):
        return self.full_name


class Position(models.Model):
    name = models.CharField(max_length=64, unique=True)
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class PaidSalary(models.Model):
    amount = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name='salaries')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee} - ${self.amount}'

    class Meta:
        verbose_name_plural = "paid salaries"
