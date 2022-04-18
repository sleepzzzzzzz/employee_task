from django.contrib import admin
from django.db.models import Sum
from django.urls import reverse
from django.utils.html import format_html

from employees.models import Employee, Position, PaidSalary


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'link_manager', 'salary', 'total_paid_salary')
    list_display_links = ('id', 'full_name')
    search_fields = ('first_name', 'last_name', 'patronymic')
    list_filter = ('position', 'position__level')

    @staticmethod
    def total_paid_salary(obj: Employee):
        total_amount = obj.salaries.aggregate(total_amount=Sum('amount')).get('total_amount')
        return total_amount

    def link_manager(self, obj: Employee):
        if obj.manager:
            link = reverse("admin:employees_employee_change", args=[obj.manager.id])
            return format_html('<a href="{}">{}</a>', link, obj.manager)
        else:
            return None

    link_manager.short_description = 'Manager'


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(PaidSalary)
class PaidSalaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'amount', 'created_at')
    list_display_links = ('id', 'employee')
    search_fields = ('employee__first_name', 'employee__last_name', 'employee__patronymic')
