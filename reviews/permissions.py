from rest_framework.permissions import BasePermission, IsAuthenticated
from accounts.permissions import IsHostOrAdmin, IsGuest


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.method == "GET"


class IsOwnerOrAll(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if request.method == "GET" and user.is_authenticated is False:
            return True

        return bool(
            user.is_authenticated and
            (
                user.is_superuser or
                (user.is_host is False) or
                (user.is_host is True and request.method == "GET")
            )
        )
