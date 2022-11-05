from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Request, Response, status
from .permissions import IsOwnerOrReadOnly
from .models import Review
from rooms.models import Room
from lodgings.models import Lodging
from .serializers import ReviewSerializer
# Create your views here.
class ListReviewFromLodgings(APIView):
    def get(self,request,lodging_id):
        lodging = get_object_or_404(Lodging, id=lodging_id)
        rooms = Room.objects.filter(lodging=lodging)
        reviews = Review.objects.filter(room__in=rooms)
        serializer = ReviewSerializer(reviews,many=True)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data)
        

class RetrieveUpdateDestroyReview(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects
