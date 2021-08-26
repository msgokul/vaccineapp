from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Taluk(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class People(models.Model):

    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    taluk = models.ForeignKey(Taluk, on_delete=models.SET_NULL, blank=True, null=True)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField()

    def __int__(self):
        return self.id

