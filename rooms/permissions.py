from rest_framework import permissions
from lodgings.models import Lodging
from django.shortcuts import get_object_or_404
from .models import Room
import ipdb


class IsLodgingOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        lodging = get_object_or_404(Lodging, id=view.kwargs['lodging_id'])
        return request.user.is_authenticated and lodging.host == request.user


class IsHost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated
            and request.user.is_host
        )
