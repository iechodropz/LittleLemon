from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=0)
    booking_date = models.DateField()


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=False)
    inventory = models.SmallIntegerField()
