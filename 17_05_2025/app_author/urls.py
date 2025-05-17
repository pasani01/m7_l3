from django.urls import path

from .views import (
    AuthorCreateView,
    AuthorListView,
    AuthorDetailView,

)
urlpatterns = [
    path('authors/create', AuthorCreateView.as_view(), name='author-list-create'),
    path('authors/', AuthorListView.as_view(), name='author-List'),
    path('authors/<slug:slug>/', AuthorDetailView.as_view(), name='author-detail'),
]