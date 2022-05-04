from django.db import models

class BikeType(models.Model):
    type = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.type


class Bike(models.Model):
    serial_number = models.CharField(max_length = 200)
    bike_type = models.ForeignKey(BikeType, on_delete = models.CASCADE)

    def __str__(self):
        return self.serial_number

class Reservation(models.Model):
    bike = models.ForeignKey(Bike, on_delete = models.CASCADE)
    date_field = models.CharField(max_length = 200)
    client = models.CharField(max_length = 200)

    def __str__(self):
        return self.client