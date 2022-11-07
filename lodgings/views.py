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
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        host = Account(self.request.user)
        serializer.save(host=self.request.user)
    
    def get_queryset(self):
        route_parameter_state = self.request.GET.get("state")
        route_parameter_city = self.request.GET.get("city")
        route_parameter_category = self.request.GET.get("category")

        if route_parameter_state: 
            
            queryset = Lodging.objects.filter(state__icontains=route_parameter_state)
            return queryset 

        if route_parameter_city: 
            
            queryset = Lodging.objects.filter(city__icontains=route_parameter_city)
            return queryset 
        
        if route_parameter_category: 
            
            queryset = Lodging.objects.filter(category__icontains=route_parameter_category)
            return queryset 
        
        return super().get_queryset()


class LodgingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lodging.objects.all()
    serializer_class = LodgingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny, IsHost, IsLodgingOwner]
