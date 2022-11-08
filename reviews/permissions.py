from rest_framework.permissions import BasePermission, IsAuthenticated
from accounts.permissions import IsHostOrAdmin, IsGuest


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.method == "GET"
