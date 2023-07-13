from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=0)
    booking_date = models.DateField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=False)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title
