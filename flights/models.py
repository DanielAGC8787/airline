from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    #ForeignKey connects this table to airport table
    #relatedName specifies how to get all the flights from an airport since origin only specifies how to get airport from a flight
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") # if airport is deleted from airport table, all flights from that airport will also delete
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
    def is_valid_flight(self):
        return self.origin != self.destination and self.duration >= 0

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    #represent many to many relationship
    #use related name to get all passengers from flight

    def __str__(self):
        return f"{self.first} {self.last}"