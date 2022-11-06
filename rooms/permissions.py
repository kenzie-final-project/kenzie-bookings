from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_host:
            return request.user.id == obj.user.id
        else:
            return False

