
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.shortcuts import get_object_or_404

from .models import Room
from lodgings.models import Lodging
from .serializers import RoomSerializer
from .mixins import SerializerMixin
from .permissions import IsOwnerOrAdmin


class ListRoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ListLodgingRoomsView(APIView):
    def get(self, request, lodging_id):
        lodging = get_object_or_404(Lodging, id=lodging_id)
        rooms = Room.objects.filter(lodging=lodging)
        serializer = RoomSerializer(rooms, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status.HTTP_200_OK)
    
class CreateRoomView(SerializerMixin, CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Room.objects
    serializer_class = RoomSerializer

    def post(self, request: Request, lodging_id):
        room = get_object_or_404(Lodging, id=lodging_id)
        
        request.data["lodging"] = room
        request.data["user"] = request.user

        serializer = RoomSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status.HTTP_201_CREATED)

class RetrieveRoomView(APIView):
    def get(self, request, lodging_id):
        lodging = get_object_or_404(Lodging, id=lodging_id)
        rooms = Room.objects.filter(lodging=lodging, id=request.pk)
        serializer = RoomSerializer(rooms, many=False)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status.HTTP_200_OK)

class UpdateRoomView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    
    queryset = Room.objects
    serializer_class = RoomSerializer

class DestroyRoomView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
