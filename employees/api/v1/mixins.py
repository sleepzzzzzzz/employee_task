from employees.api.v1.permissions import IsAdminOrReadOnly


class ManagerPermissionMixin:

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            return [permission() for permission in [IsAdminOrReadOnly]]
        else:
            return super().get_permissions()