from django.db import models
from django.db.models import TextChoices
from django.core.validators import MaxValueValidator, MinValueValidator


class CategoriesChoices(TextChoices):
    OTHERS = 'OTHER', 'Other'
    FURNITURE = 'FURNITURE', 'Furniture'
    SPORTS = 'SPORT', 'Sport'
    COMPUTERS = 'COMPUTERS', 'Computer'
    CLOTHES = 'CLOTHES', 'Clothes'
    ACCESSORIES = 'ACCESSORIES', 'Accessories'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    image = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Изображение')
    categories = models.CharField(max_length=100, choices=CategoriesChoices.choices, default=CategoriesChoices.OTHERS, verbose_name='Категория')
    remainder = models.PositiveIntegerField(null=False, blank=False, verbose_name='Остаток')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.name} - {self.categories}"

