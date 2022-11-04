from django.shortcuts import render
from rest_framework import generics
from .serializers import AccountSerializer
from .models import Account
# Create your views here.
class ListCreateAccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
