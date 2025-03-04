from rest_framework import serializers
from .models import *

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
	
# class ItemSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Item
# 		fields='__all__'


class CollegeSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=50)
	age = serializers.IntegerField()
	department = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return College.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.age = validated_data.get('age', instance.age)
		instance.department = validated_data.get('department', instance.department)
		instance.save()
		return instance


class SchoolSerializer(serializers.Serializer):

	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=50)
	age = serializers.IntegerField()
	department = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return School.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.age = validated_data.get('age', instance.age)
		instance.department = validated_data.get('department', instance.department)
		instance.save()
		return instance
	
class SingerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Singer
		fields = ["id", "name", "age"]

class SongSerializer(serializers.ModelSerializer):
	singer = SingerSerializer()

	class Meta:
		model = Song
		fields = ['id', 'title', 'singer']

	def create(self, validated_data):
		singer_data = validated_data.pop('singer')
		singer, _ = Singer.objects.get_or_create(**singer_data)
		song = Song.objects.create(singer=singer, **validated_data)
		return song


class NameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Name
		fields = '__all__'