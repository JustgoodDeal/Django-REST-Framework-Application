from rest_framework import permissions

class CrudForManagersPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser or (request.user.is_authenticated and request.user.role == 'Manager'):
            return True
        return False