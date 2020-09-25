from django.db import models

# Create your models here.


class PizzaModel(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)


class CustomerModel(models.Model):
    userid = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=15)


class OrderModel(models.Model):
    username = models.CharField(max_length=30)
    phoneno = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    ordereditems = models.CharField(max_length=240)
    status = models.CharField(max_length=15)