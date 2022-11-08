from lodgings.models import Lodging
from rooms.models import Room


class SerializerMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


class UserTypeMixin:
    def get_serializer_class(self, *args, **kwargs):
        user = self.request.user
        if user.is_superuser is True:
            return self.serializer_map.get("admin", self.serializer_class)
        elif user.is_host is True:
            return self.serializer_map.get("host", self.serializer_class)
        else:
            return self.serializer_map.get("guest", self.serializer_class)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser is True:
            return self.queryset.all()
        elif user.is_host is True:
            lodgings = Lodging.objects.filter(host=user)
            rooms = Room.objects.filter(lodging__in=lodgings)
            return self.queryset.filter(room__in=rooms)
        else:
            return self.queryset.filter(user=user)
