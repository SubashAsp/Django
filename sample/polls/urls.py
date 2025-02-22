from django.urls import path
from .views import *

urlpatterns = [
    path("index/", index, name="index"),
    
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    
    path('movies/', movie_list, name='movie-list'),
    path('movies/<int:pk>/', movie_detail, name='movie-detail'),
    path('products/', products_list, name='product-list'),
    path('items/', ItemListCreateAPIView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail'),
]
