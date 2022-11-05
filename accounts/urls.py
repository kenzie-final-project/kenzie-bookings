from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import ListCreateAccountView, DetailedAccountView

urlpatterns = [
    path("login/", ObtainAuthToken.as_view()),
    path("accounts/", ListCreateAccountView.as_view()),
    path("accounts/<uuid:pk>", DetailedAccountView.as_view())
]
