from django.db import models


# Create your models here.
class YearRate(models.Model):
    start = models.IntegerField(default=2010)
    end = models.IntegerField(default=2023)
    rate = models.FloatField()


class TypeRate(models.Model):
    type = models.CharField(max_length=20)
    rate = models.FloatField()


class EnergieRate(models.Model):
    energie = models.CharField(max_length=20)
    rate = models.FloatField()


class DistRate(models.Model):
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=5)
    rate = models.FloatField()


class Bonus(models.Model):
    passager = models.IntegerField(default=1)
    bonus = models.FloatField()


class TauxEmprunt(models.Model):
    start = models.FloatField(default=0)
    end = models.FloatField(default=10)
    rate = models.FloatField(default=0)
