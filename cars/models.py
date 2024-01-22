from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
