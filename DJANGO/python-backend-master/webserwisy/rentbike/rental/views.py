from django.shortcuts import render
import requests
from .models import BikeType, Bike, Reservation

def home(request):
    bike_types = BikeType.objects.all()
    bikes = Bike.objects.all()

    context = {'title': str("Wypożyczalnia rowerów"),
               'description': str("Rowery można wypożyczyć jedynie na pojedyncze doby!"),
               'offer_description': str("Do wypożyczenia mamy następujące rowery:"),
               'biketypes': bike_types,
               'bikes': bikes,
               }

    return render(request, 'rental/index.html', context)

def bike_type(request, bike_type_id):
    bike_type = BikeType.objects.get(id = bike_type_id)

    return render(request, 'rental/biketypes.html', {'bike_type': bike_type})

def bike(request, bike_id):
    bike = Bike.objects.get(id = bike_id)

    return render(request, 'rental/bike.html', {'bike' : bike})