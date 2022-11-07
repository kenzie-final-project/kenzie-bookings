from rest_framework import permissions
import ipdb

class IsLodgingOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.lodging.host == request.user

class IsHost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated
            and request.user.is_host
        )
