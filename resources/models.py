from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

class SoftSkillName(models.Model):
    name= models.CharField(max_length=100, unique=True)

class SkillName(models.Model):
    name = models.CharField(max_length=100, unique=True)