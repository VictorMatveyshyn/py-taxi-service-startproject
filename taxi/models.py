from django.db import models

class Manufactirer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f'{self.name} ({self.country})"
class Driver(AbctractUser):
    license_number = models.CharField(max_length=63, unique=True)

class Car(models.Model):
    model = models.CharField(max_length=63)
    manufactirer = models.ForeignKey(Manufactirer)
    driver = models.ForeignKey(Driver)