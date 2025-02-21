from django.db import models

class Movie(models.Model):
    moive_name = models.CharField(max_length=200, null=False)
    language = models.CharField(max_length=75, null=False)
    gener = models.CharField(max_length=100, null=False)
    rating = models.FloatField()

class Show(models.Model):
    movie = models.CharField(Movie, on_delete=models.CASCADE)
    time = models.TimeField()
    price = models.FloatField()

class Booking(models.Model):
    user = models.CharField(max_length=50, null=False)
    show = models.CharField(max_length=100, null=False)
    seat = models.CharField(max_length=50, null=False)
    booking_time = models.DateTimeField()
    total_price = models.FloatField()
    is_paid = models.BooleanField(default=False)