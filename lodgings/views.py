from rest_framework import generics
from .models import Lodging
from .serializers import LodgingSerializer
from accounts.serializers import Account
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsLodgingOwner, IsHost


class LodgingView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsHost, IsLodgingOwner]
    queryset = Lodging.objects.all()
    serializer_class = LodgingSerializer

    def perform_create(self, serializer):
        host = Account(self.request.user)
        serializer.save(host=self.request.user)


class LodgingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lodging.objects.all()
    serializer_class = LodgingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLodgingOwner]
