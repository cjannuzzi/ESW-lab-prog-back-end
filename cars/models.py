from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)  # cada ID único
    name = models.CharField(max_length=200)  # nome da marca

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)  # modelo
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name="car_brand"
    )  # marca
    factory_year = models.IntegerField(blank=True, null=True)  # ano de fabricação
    model_year = models.IntegerField(blank=True, null=True)  # ano do carro
    plate = models.CharField(max_length=10, blank=True, null=True)  # placa do carro
    value = models.FloatField(blank=True, null=True)  # valor do carro
    photo = models.ImageField(
        upload_to="cars/", blank=True, null=True
    )  # adiciona a imagem do carro

    def __str__(self):
        return self.model
