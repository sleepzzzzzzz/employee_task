from rest_framework.routers import DefaultRouter

from employees.api.v1.views import EmployeeViewSet, PaidSalaryViewSet, PositionViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet, 'employee')
router.register('salaries', PaidSalaryViewSet, 'salary')
router.register('positions', PositionViewSet, 'position')

urlpatterns = router.urls
