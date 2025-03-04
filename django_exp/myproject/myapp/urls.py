from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.message, name='message'),
    path('names/', NameList.as_view(), name='name-list'),
    path('products/', product, name='product'),
    path('signup/', signup, name='signup'),
]
