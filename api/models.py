from datetime import date
from django.db import models


class Color(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class CarBrand(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class CarModel(models.Model):
    title = models.CharField(max_length=200)
    car_brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(default=date.today)