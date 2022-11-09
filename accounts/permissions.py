from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSafeOnlyAdmin(BasePermission):
    def has_permission(self, request, view):
        is_admin = request.user.is_superuser

        if (request.method in SAFE_METHODS) and is_admin is False:
            return False

        return True


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):

        return bool(
            request.user.is_authenticated and request.user == obj
        )


class IsHostOrAdmin(BasePermission):
    def has_permission(self, request, view):

        return bool(
            request.user and
            (
             request.user.is_host
            )
        )


class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated is False or request.user.is_host is False)


class IsHost(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated
            and request.user.is_host
        )


class IsGetAdminOrPost(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser and request.method == "GET" or request.method == "POST"