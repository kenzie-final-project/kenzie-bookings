from rest_framework.permissions import BasePermission


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
