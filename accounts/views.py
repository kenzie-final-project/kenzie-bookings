from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrAdmin
from .serializers import AccountSerializer
from .models import Account


class ListCreateAccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class DetailedAccountView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
