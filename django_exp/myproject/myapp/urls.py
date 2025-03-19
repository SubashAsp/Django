from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.message, name='message'),
    path('names/', NameList.as_view(), name='name-list'),
    path("names/<int:pk>", NameDetail.as_view(), name='name-detail'),
    path('index/', index, name='product'),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('filters/', filter, name='filter'),
    path('contact/', contact_view, name= 'contact'),
    path('signups/', signup_view, name='signup'),
    path('products/', product_view, name="product-view"),
    path('metainfo/', meta_info, name='meta-info'),
    path('search/', product_search, name='product-search'),
    path('create/', product_create, name='product-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)