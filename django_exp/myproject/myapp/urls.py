from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.message, name='message'),
    path('names/', NameList.as_view(), name='name-list'),
    path('index/', index, name='product'),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
]
