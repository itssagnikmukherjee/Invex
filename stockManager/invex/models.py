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
    class Meta:
        db_table = 'products'