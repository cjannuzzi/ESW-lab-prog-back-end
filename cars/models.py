from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)  # cada ID único
    name = models.CharField(max_length=200)  # nome da marca


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)  # modelo
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name="car_brand"
    )  # marca
    factory_year = models.IntegerField(blank=True, null=True)  # ano de fabricação
    model_year = models.IntegerField(blank=True, null=True)  # ano do carro
    value = models.FloatField(blank=True, null=True)  # valor do carro

    def __str__(self):
        return self.model
