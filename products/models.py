from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_image', blank=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return f'{self.name} | {self.category.name}'

