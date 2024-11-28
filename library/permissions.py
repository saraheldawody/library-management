from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
        Custom permission to allow only admins to create or update objects.
    """
    def has_permission(self, request, view):
        return bool(request.method in ['GET', 'HEAD', 'OPTIONS'] or request.user and request.user.is_staff)