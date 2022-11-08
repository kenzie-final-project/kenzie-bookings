from rest_framework import permissions
from accounts.permissions import IsHost


class IsLodgingOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.host == request.user
