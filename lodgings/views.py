from rest_framework import generics
from .models import Lodging
from .serializers import LodgingSerializer
from accounts.serializers import Account


class LodgingsView(generics.ListCreateAPIView):
    queryset = Lodging.objects.all()

    def perform_create(self, serializer):
        host = Account(self.request.user)
        serializer.save(host=host)