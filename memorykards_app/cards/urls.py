from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
    ),
    path(
        "novo",
        views.CardCreateView.as_view(),
        name="card-create"
    ),
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),
    path(
        "nivel/<int:box_num>",
        views.BoxView.as_view(),
        name="nivel"
    ),
]