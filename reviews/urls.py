from django.urls import path

from .views import ListReviewFromLodgings, RetrieveUpdateDestroyReview

urlpatterns = [
    path("lodgings/<id_lodgings>/rooms/<id_room>/reviews/<pk>", ListReviewFromLodgings.as_view()),
    path("lodgings/<id_lodgings>/reviews/<pk>", RetrieveUpdateDestroyReview.as_view())
]
