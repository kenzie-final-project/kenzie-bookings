from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.views import APIView, Request, Response, status
from .permissions import IsOwnerOrReadOnly, IsGuest, IsHostOrAdmin, IsAuthenticated
from .models import Review
from rooms.models import Room
from lodgings.models import Lodging
from .serializers import ReviewSerializer
# Create your views here.


class ListReviewFromLodgings(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    serializer_class = ReviewSerializer
    """ def get(self, request, lodging_id):
        lodging = get_object_or_404(Lodging, id=lodging_id)
        rooms = Room.objects.filter(lodging=lodging)
        reviews = Review.objects.filter(room__in=rooms)
        serializer = ReviewSerializer(data=reviews, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data) """
    def get_queryset(self):
        lodging = get_object_or_404(Lodging, id=self.kwargs.get('lodging_id'))
        rooms = Room.objects.filter(lodging=lodging)
        reviews = Review.objects.filter(room__in=rooms)
        return reviews


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
        room_id = self.kwargs.get('room_id')
        return self.queryset.filter(room_id=room_id)

    def perform_create(self, serializer):
        room_id = self.kwargs.get('room_id')
        user = self.request.user
        return serializer.save(room_id=room_id, user=user)


class ListReview (ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsGuest]
    serializer_class = ReviewSerializer
    queryset = Review.objects

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.filter(user_id=user.id)
