from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
