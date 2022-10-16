from django.db import models
from django.db.models import TextChoices
from market_app.managers import ProductManager


class CategoriesChoices(TextChoices):
    OTHERS = 'OTHER', 'Other'
    FURNITURE = 'FURNITURE', 'Furniture'
    SPORTS = 'SPORT', 'Sport'
    COMPUTERS = 'COMPUTERS', 'Computer'
    CLOTHES = 'CLOTHES', 'Clothes'
    ACCESSORIES = 'ACCESSORIES', 'Accessories'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Detail description')
    image = models.CharField(max_length=3000, null=True, blank=True, verbose_name='Image')
    categories = models.CharField(max_length=100, choices=CategoriesChoices.choices, default=CategoriesChoices.OTHERS, verbose_name='Categories')
    remainder = models.PositiveIntegerField(null=False, blank=False, verbose_name='Remainder')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Date of change')

    objects = ProductManager()

    def __str__(self):
        return f"{self.name} - {self.categories}"

