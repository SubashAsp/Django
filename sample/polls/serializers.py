from rest_framework import serializers
from .models import Book, Movies, Product, Item

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields='__all__'

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movies
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=Product
		fields='__all__'
	
class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model=Item
		fields='__all__'