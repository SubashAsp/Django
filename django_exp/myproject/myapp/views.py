from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Name
from .serializers import NameSerializer
from rest_framework import generics
from .forms import *

# Create your views here.
def message(request):
	return HttpResponse('Welcome to the view.')

class NameList(generics.ListCreateAPIView):
	queryset = Name.objects.all()
	serializer_class = NameSerializer

def index(request):
	return render(request, "index.html", {'name':"Subash"})

def signup(request):
	return render(request, 'signup.html')

def home(request):
	context = {"user": "subash thiru", "items": ['Python', 'Django', 'Template', 'Filters', 'Language'], 'current_year':2025, 'numbers':[1, 2, 3, 4, 5], 'number':7, 'date':2025-3-7,}
	people=[
    	{"name": "Subash", "age": 22},
    	{"name": "Karthi", "age": 24},
    	{"name": "Suganth", "age": 26},
    	{"name": "Logu", "age": 28}]
	context.update(people)
	return render(request, 'home.html', context)

def filter(request):
	context = {"user": "subash thiru", "items": ['Python', 'Django', 'Template', 'Filters', 'Language'], 'current_year':2025, 'numbers':[1, 2, 3, 4, 5], 'number':7, 'date':2025-3-7,'people': [
    	{"name": "Subash", "age": 22},
    	{"name": "Karthi", "age": 24},
    	{"name": "Suganth", "age": 26},
    	{"name": "Logu", "age": 28}]}
	
	return render(request, 'filters.html', context)

def contact_view(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			print(f'Message from {name} ({email}): {message}')
			return render(request, 'thankyou.html')
	else:
		form = ContactForm()
		return render(request, 'form.html', { 'form': form })
	
def signup_view(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(form.cleaned_data['password'])
			user.save()
			return redirect('home')
	else:
		form = SignupForm()
	return render(request, 'signin.html', {'form': form})