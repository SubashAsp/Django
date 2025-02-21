from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movies
from .serializers import MovieSerializer

# Create your views here.
def index(request):
	return HttpResponse("Hello, World. You're at the polls index.")

class BookListCreateAPIView(generics.ListCreateAPIView):
	books = Book.objects.all()
	serializer = BookSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
		if request.method == 'GET':
			movies = Movies.objects.all()
			serializer = MovieSerializer(movies, many=True)
			return Response(serializer.data)
		elif request.method == 'POST':
			serializer = MovieSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors)
