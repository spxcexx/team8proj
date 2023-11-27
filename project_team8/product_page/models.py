from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    in_stock = models.BooleanField()
    radiation = models.IntegerField()
    image = models.ImageField()

