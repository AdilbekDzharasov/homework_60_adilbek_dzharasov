from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum, F


class ProductInCart(models.Model):
    product = models.ForeignKey(
        to='market_app.Product',
        related_name='product',
        on_delete=models.CASCADE,
        verbose_name='Product'
    )
    quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name='Quantity')

    def get_sum(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_total():
        total = ProductInCart.objects.aggregate(total=Sum(F("quantity") * F("product__price")))
        return total['total']

    def __str__(self):
        return f"{self.product}"

