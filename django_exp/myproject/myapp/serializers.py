from rest_framework import serializers
from .models import Name, Product

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"