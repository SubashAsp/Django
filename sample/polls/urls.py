from django.urls import path
from .views import *

urlpatterns = [
    path("index/", index, name="index"),
    
    path('books/', BookList.as_view(), name='book-list-create'),
    
    path('movies/', movie_list, name='movie-list'),
    path('movies/<int:pk>/', movie_detail, name='movie-detail'),

    path('products/', products_list, name='product-list'),

    # path('items/', ItemListCreateAPIView.as_view(), name='item-list'),
    # path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail'),

    path('colleges/', ColllegeList.as_view(), name='college-list'),
    path('colleges/<int:pk>/', CollegeDetail.as_view(), name='college-detail'),
    
    path('schools/', SchoolList.as_view(), name='school-list'),
    path('schools/<int:pk>/', SchoolDetail.as_view(), name='school-detail'),
]
