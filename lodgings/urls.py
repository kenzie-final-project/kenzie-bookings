from django.urls import path
from .views import LodgingsDetailView, LodgingsView

urlpatterns = [
    path('lodgings/', LodgingsView.as_view()),
    path('lodgings/<int:pk>', LodgingsDetailView.as_view())
]
