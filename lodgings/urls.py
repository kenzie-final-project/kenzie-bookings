from django.urls import path
from .views import LodgingDetailView, LodgingView

urlpatterns = [
    path('lodgings/', LodgingView.as_view()),
    path('lodgings/<int:pk>/', LodgingDetailView.as_view()),
]
