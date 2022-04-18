from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission class allows actions only for staff users
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsManagerPermission(permissions.BasePermission):
    """
    Permission check whether employee has position lvl 0 or 1
    """

    def has_permission(self, request, view):
        return request.user.employee.position.level in range(0, 2)
