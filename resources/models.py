from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    province_id = models.IntegerField()

class Country(models.Model):
    name= models.CharField(max_length=100, unique=True)


