from enum import unique

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Airports(models.Model):
    airport_name = models.CharField(max_length=20)

    def __str__(self):
        return self.airport_name


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=30)
    departure_city = models.ForeignKey(Airports, on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name="departure")
    arrival_city = models.ForeignKey(Airports, on_delete=models.SET_NULL, blank=True, null=True, related_name="arrival")
    departure_date = models.DateField()
    departure_time = models.TimeField()
    seats_count = models.IntegerField(default=100)
    fare = models.PositiveIntegerField(null=False, default=1500)


GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
)


class Passenger(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField(default=20)


class Tickets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ref_no = models.CharField(unique=True, max_length=8)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
