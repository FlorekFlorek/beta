
from django.contrib import admin
from django.urls import path
import rental.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rental.views.home),
    path('biketype/<int:bike_type_id>', rental.views.bike_type, name = "bike_type"),
    path('bike/<int:bike_type_id>', rental.views.bike, name = "bike")
]
