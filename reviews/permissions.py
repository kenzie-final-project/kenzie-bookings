from rest_framework.permissions import BasePermission, IsAuthenticated
from accounts.permissions import IsHostOrAdmin


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.method == "GET"


class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated is False or request.user.is_host is False)
