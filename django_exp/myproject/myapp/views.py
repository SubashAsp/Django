from django.shortcuts import render
from django.http import HttpResponse
from .models import Name
from .serializers import NameSerializer
from rest_framework import generics

# Create your views here.
def message(request):
	return HttpResponse('Welcome to the view.')

class NameList(generics.ListCreateAPIView):
	queryset = Name.objects.all()
	serializer_class = NameSerializer

def product(request):
	return render(request, "index.html")

def signup(request):
	return render(request, 'signup.html')