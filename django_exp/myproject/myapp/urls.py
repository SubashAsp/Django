from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.message, name='message'),
    path('names/', NameList.as_view(), name='name-list'),
    path('index/', index, name='product'),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('filters/', filter, name='filter'),
    path('contact/', contact_view, name= 'contact'),
    path('signups/', signup_view, name='signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)