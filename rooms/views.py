from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Room
from .serializers import RoomSerializer
from .mixins import SerializerMixin
from .permissions import IsLodgingOwner, IsHost
from lodgings.models import Lodging
import ipdb


class RoomView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny, IsLodgingOwner]

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        lodging = get_object_or_404(Lodging, id=self.kwargs.get('lodging_id'))
        rooms = Room.objects.filter(lodging=lodging)
        return rooms

    def perform_create(self, serializer):
        lodging = Lodging.objects.get(id=self.kwargs.get('lodging_id'))
        return serializer.save(lodging=lodging)


class RoomDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny, IsLodgingOwner]

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
