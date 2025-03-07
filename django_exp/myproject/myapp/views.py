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

def index(request):
	return render(request, "index.html", {'name':"Karthi"})

def signup(request):
	return render(request, 'signup.html')

def home(request):
	context = {"user": "subash thiru", "items": ['Python', 'Django', 'Template', 'Filters', 'Language'], 'current_year':2025, 'numbers':[1, 2, 3, 4, 5], 'number':7, 'date':2025-3-7}
	return render(request, 'home.html', context)