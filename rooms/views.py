from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateDestroyAPIView

from .models import Room
from ..lodgings.models import Lodging
from .serializers import RoomSerializer
from .mixins import SerializerMixin
from .permissions import IsOwnerOrAdmin

    
class ListRoomview(SerializerMixin, ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class CreateRoomView(SerializerMixin, CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def perform_create(self, serializer):
        return serializer.save(lodging_id=self.kwargs.get('lodging_id'))

class RetrieveRoomView(RetrieveAPIView):    
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class DetailRoomView(UpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
