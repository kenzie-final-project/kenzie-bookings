from django.urls import path

from .views import ListReviewFromLodgings, RetrieveUpdateDestroyReview, RoomReview, ListReview

urlpatterns = [
    path("lodgings/<id_lodgings>/rooms/<id_room>/reviews/<pk>/", RetrieveUpdateDestroyReview.as_view()),
    path("lodgings/<id_lodgings>/reviews/", ListReviewFromLodgings.as_view()),
    path("lodgings/<id_lodgings>/rooms/<id_room>/reviews/", RoomReview.as_view()),
    path("reviews/", ListReview.as_view())
]
