from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
