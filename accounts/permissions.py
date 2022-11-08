from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user_id = view.kwargs['pk']

        return bool(
            request.user and
            (
             request.user.is_staff or
             request.user.id == user_id
            )
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
