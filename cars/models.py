from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)  # modelo
    brand = models.CharField(max_length=200)  # marca
    factory_year = models.IntegerField(blank=True, null=True)  # ano de fabricação
    model_year = models.IntegerField(blank=True, null=True)  # ano do carro
    value = models.FloatField(blank=True, null=True)  # valor do carro
