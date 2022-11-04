from django.urls import path
from . import views

urlpatterns = [
    path('lodgings/', views.LodgingView().as_view()),
    path('lodgings/<str:pk>/', views.LodgingDetailView().as_view()),
]