from rest_framework import generics, status, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView

# Create your views here.
def index(request):
	return HttpResponse("Hello, World. You're at the polls index.")

class BookList(generics.ListCreateAPIView):
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


# class ItemListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
	
# class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer


class ColllegeList(APIView):
	
	def get(self, request):
		college = College.objects.all()
		serializer = CollegeSerializer(college, many=True)
		return Response(serializer.data)
	def post(self, request):
		serializer = CollegeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollegeDetail(APIView):
	def get_object(self, pk):
		try:
			return College.objects.get(pk=pk)
		except College.DoesNotExist:
			return None

	def get(self, request, pk):
		college = self.get_object(pk)
		if not college:
			return Response({"Collage not found"}, status=status.HTTP_404_NOT_FOUND)
		serializer = CollegeSerializer(college)
		return Response(serializer.data)

	def put(self, request, pk):
		college = self.get_object(pk)
		if not college:
			return Response({"Collage not found"}, status=status.HTTP_404_NOT_FOUND)
		serializer = CollegeSerializer(college, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		college = self.get_object(pk)
		if not college:
			return Response({"Collage not found"}, status=status.HTTP_404_NOT_FOUND)
		college.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class SchoolList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
	
class SchoolDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer
	
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
