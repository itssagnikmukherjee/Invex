from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    supplier = models.CharField(max_length=100)
    date = models.DateField()
    isVisible = models.BooleanField(default=True)
    image_url = models.CharField(max_length=255,null=True, blank=True)
    class Meta:
        db_table = 'products'

class picfile(models.Model):
    fname = models.CharField(max_length=100)
    furl = models.ImageField()
    class Meta():
        db_table = 'pictures'