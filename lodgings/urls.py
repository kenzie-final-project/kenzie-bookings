from django.urls import path

from .views import LodgingsView, LodgingsDetailView

urlpatterns = [
    path("lodgings/", LodgingsView.as_view()),
    path("lodgings/<int:pk>/", LodgingsDetailView.as_view())
]