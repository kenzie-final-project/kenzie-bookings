from django.urls import path

from .views import ReviewDetailView, LodgingReviewView, ReviewView, GenericReviewView

urlpatterns = [
    path("lodgings/<lodging_id>/rooms/<room_id>/reviews/<pk>/", ReviewDetailView.as_view()),
    path("lodgings/<lodging_id>/rooms/<room_id>/reviews/", ReviewView.as_view()),
    path("lodgings/<lodging_id>/reviews/", LodgingReviewView.as_view()),
    path("reviews/", GenericReviewView.as_view())
]
