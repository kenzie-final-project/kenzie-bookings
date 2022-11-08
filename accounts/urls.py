from django.urls import path

from .views import ListCreateAccountView, DetailedAccountView, LoginView

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("accounts/<uuid:pk>", DetailedAccountView.as_view()),
    path("accounts/", ListCreateAccountView.as_view())
]
