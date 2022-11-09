from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Response
from .permissions import IsOwnerOrAdmin, IsSafeOnlyAdmin
from .serializers import AccountSerializer, AccountListSerializer
from .mixins import SerializerMixin
from .models import Account


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'uuid': user.id})


class ListCreateAccountView(SerializerMixin, ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSafeOnlyAdmin]
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
