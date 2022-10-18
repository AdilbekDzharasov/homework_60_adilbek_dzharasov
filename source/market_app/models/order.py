from django.db import models
from django.utils import timezone


class Order(models.Model):
    products = models.ManyToManyField('market_app.Product', related_name='orders', verbose_name='Products',
                                      through='market_app.OrderProduct', through_fields=['order', 'product'])
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    phone = models.CharField(max_length=30, null=False, blank=False, verbose_name='Phone')
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name='Address')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Date of creation')

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.address}'


class OrderProduct(models.Model):
    order = models.ForeignKey('market_app.Order', related_name='order_products', on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey('market_app.Product', related_name='products_order', on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')

    def str(self):
        return f'{self.product.name} - {self.order.name}'

