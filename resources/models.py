from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Country(models.Model):
    name= models.CharField(max_length=100, unique=True)


