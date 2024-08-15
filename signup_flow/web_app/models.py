from django.db import models
import datetime

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100 , unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(datetime.datetime.now())
    updated_at = models.DateTimeField(datetime.datetime.now())

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(datetime.datetime.now())
    updated_at = models.DateTimeField(datetime.datetime.now())

class Records(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, default="")
    category = models.ForeignKey(Category, max_length=100, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    qty = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default="")
    created_at = models.DateTimeField(datetime.datetime.now())
    updated_at = models.DateTimeField(datetime.datetime.now())
