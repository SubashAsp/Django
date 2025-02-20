from django.urls import path
from .views import BookListCreateAPIView
from . import views

urlpatterns = [
	path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
	path("", views.index, name="index"),
]
