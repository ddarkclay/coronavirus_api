from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated


class SafeGetMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated
