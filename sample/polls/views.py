from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Book, Movies, Product, Item
from .serializers import BookSerializer, MovieSerializer, ProductSerializer, ItemSerializer

# Create your views here.
def index(request):
	return HttpResponse("Hello, World. You're at the polls index.")

class BookListCreateAPIView(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class= BookSerializer


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
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    movies = get_object_or_404(Movies, pk=pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movies)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movies.delete()
        return Response({"message": "Movie deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
	

@api_view(['GET', 'POST'])
def products_list(request):
	if request.method == 'GET':
		item = Product.objects.all()
		serializer = ProductSerializer(item, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
	
class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
