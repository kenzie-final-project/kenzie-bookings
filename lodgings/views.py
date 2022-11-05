from rest_framework import generics
from .models import Lodging
from .serializers import LodgingSerializer
from accounts.serializers import Account
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


class LodgingsView(generics.ListCreateAPIView):
    queryset = Lodging.objects.all()
    serializer_class = LodgingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        host = Account(self.request.user)
        serializer.save(host=host)


class LodgingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lodging.objects.all()
    serializer_class = LodgingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]