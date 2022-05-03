from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    #give me all this info when I load a flight
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    #display filter horizontally
    filter_horizontal = ("flights",)

admin.site.register(Airport)
#register this flight but use flightAdmin settings
#now it will not only show origin and destination, but all 4 things as well
admin.site.register(Flight, FlightAdmin)
#use passengerAdmin class
admin.site.register(Passenger, PassengerAdmin)