from django.urls import path
from .views import BookListCreateAPIView, movie_list
from . import views

urlpatterns = [
	path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
	path("", views.index, name="index"),
    path('movies/', movie_list, name='movie_list'),
]
