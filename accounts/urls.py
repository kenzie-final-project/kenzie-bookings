from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import ListCreateAccountView

urlpatterns = [
    path("login/", ObtainAuthToken.as_view()),
    path("accounts/", ListCreateAccountView.as_view()),

]