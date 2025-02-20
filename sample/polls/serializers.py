from rest_framework import serializers
from .models import Book, Movies

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields='__all__'

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movies
		fields = '__all__'
