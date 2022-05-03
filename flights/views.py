from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger


# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id) #get flight that corresponds to id
    return render(request, "flights/flight.html", {
        "flight":flight,
        "flight_id":flight_id,
        "passengers": flight.passengers.all(),
        #return all passengers except the ones that are already on the flight (all of them)
        "non_passengers": Passenger.objects.exclude(flights = flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        #get me a flight with this ID
        flight = Flight.objects.get(pk=flight_id) # pk is the primary key that i will use to get the passenger
        #get passenger whose pk is equal to whetever was submitted in this form and whos name is "passemger"
        passenger = Passenger.objects.get(pk =int(request.POST["passenger"])) #form will be submitted with field passenger
        #this will add a new row into a table that keeps track of passengers on that flight
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args={flight_id}))
    return render()