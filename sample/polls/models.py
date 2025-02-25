from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=100, null=True)
	author = models.CharField(max_length=100, null=True)
	published_date = models.DateField()

	def __str__(self):
            return self.title or 'Untitled'


class Movies(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length = 200, null=False)
	director = models.CharField(max_length = 200, null=False)
     
	def __str__(self):
          return self.name
     

class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
             
        
# class Item(models.Model):
#     name = models.CharField(max_length=100, blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     bill_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#          return self.name


class School(models.Model):
     name = models.CharField(max_length=50, null=False)
     age = models.IntegerField()
     department = models.CharField(max_length=100, null=False)
     
     def __str__(self):
            return self.name  
     
class College(models.Model):
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField()
    department = models.CharField(max_length=100, null=False)

    def __str__(self):
         return self.name
    
class Singer(models.Model):
     name = models.CharField(max_length=50)
     age = models.IntegerField()

     def __str__():
          return
     
class Song(models.Model):
     title = models.CharField(max_length=50)
     singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

     def __str__(self):
          return self.title