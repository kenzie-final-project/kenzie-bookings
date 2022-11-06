from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView, Request, Response, status
from accounts.permissions import IsOwnerOrAdmin
from .permissions import IsOwnerOrReadOnly
from .models import Review
from rooms.models import Room
from lodgings.models import Lodging
from .serializers import ReviewSerializer
# Create your views here.


class ListReviewFromLodgings(APIView):
    def get(self, request, lodging_id):
        lodging = get_object_or_404(Lodging, id=lodging_id)
        rooms = Room.objects.filter(lodging=lodging)
        reviews = Review.objects.filter(room__in=rooms)
        serializer = ReviewSerializer(reviews, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)


class RetrieveUpdateDestroyReview(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects


class RoomReview (ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects

    def get_queryset(self):
        room_id = self.kwargs["room_id"]
        return self.queryset.filter(lodging=room_id)

    def post(self, request: Request, room_id):
        room = get_object_or_404(Room, id=room_id)
        request.data["room"] = room
        request.data["user"] = request.user
        serializer = ReviewSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)


class ListReview (ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    serializer_class = ReviewSerializer
    queryset = Review.objects

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.filter(user_id=user.id)
