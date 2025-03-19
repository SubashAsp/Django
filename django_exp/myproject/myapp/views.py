from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
from rest_framework import generics
from django.contrib.auth import get_user_model
from .forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def message(request):
	return HttpResponse('Welcome to the view.')

class NameList(generics.ListCreateAPIView):
	queryset = Name.objects.all()
	serializer_class = NameSerializer


class NameDetail(generics.RetrieveUpdateDestroyAPIView):
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
	
user = get_user_model()

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

@api_view(["GET", "POST"])
def product_view(request):
	if request.method == "GET":
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)
	
	elif request.method == "POST":
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)


@api_view(["GET"])
def product_search(request):
	product_id=request.GET.get("id", None)
	if product_id is not None:
		product=Product.objects.filter(id=product_id)
	else:
		return Response({"Product Id is required"})
	
	serializer=ProductSerializer(product, many=True)
	return Response(serializer.data)
	

@api_view(["POST"])
def product_create(request):
	serializer=ProductSerializer(data=request.POST)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors)


def meta_info(request):
    data = {
        "CONTENT_LENGTH": request.META.get("CONTENT_LENGTH", "Not Provided"),
        "CONTENT_TYPE": request.META.get("CONTENT_TYPE", "Not Provided"),
        "HTTP_ACCEPT": request.META.get("HTTP_ACCEPT", "Not Provided"),
        "HTTP_ACCEPT_ENCODING": request.META.get("HTTP_ACCEPT_ENCODING", "Not Provided"),
        "HTTP_ACCEPT_LANGUAGE": request.META.get("HTTP_ACCEPT_LANGUAGE", "Not Provided"),
        "HTTP_HOST": request.META.get("HTTP_HOST", "Not Provided"),
        "HTTP_REFERER": request.META.get("HTTP_REFERER", "Not Provided"),
        "HTTP_USER_AGENT": request.META.get("HTTP_USER_AGENT", "Not Provided"),
        "QUERY_STRING": request.META.get("QUERY_STRING", "Not Provided"),
        "REMOTE_ADDR": request.META.get("REMOTE_ADDR", "Not Provided"),
        "REMOTE_HOST": request.META.get("REMOTE_HOST", "Not Provided"),
        "REMOTE_USER": request.META.get("REMOTE_USER", "Not Provided"),
        "REQUEST_METHOD": request.META.get("REQUEST_METHOD", "Not Provided"),
        "SERVER_NAME": request.META.get("SERVER_NAME", "Not Provided"),
        "SERVER_PORT": request.META.get("SERVER_PORT", "Not Provided"),
    }
    return JsonResponse(data)