from django.urls import path

from .views import ListReviewFromLodgings, RetrieveUpdateDestroyReview, RoomReview, ListReview

urlpatterns = [
    path("lodgings/<lodging_id>/rooms/<room_id>/reviews/<pk>/", RetrieveUpdateDestroyReview.as_view()),
    path("lodgings/<lodging_id>/rooms/<room_id>/reviews/", RoomReview.as_view()),
    path("lodgings/<lodging_id>/reviews/", ListReviewFromLodgings.as_view()),
    path("reviews/", ListReview.as_view())
]
