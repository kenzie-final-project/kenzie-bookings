from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrAdmin
from .serializers import AccountSerializer, AccountListSerializer
from .mixins import SerializerMixin
from .models import Account


class ListCreateAccountView(SerializerMixin, ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    serializer_map = {
        "GET": AccountListSerializer,
        "POST": AccountSerializer
    }


class DetailedAccountView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
