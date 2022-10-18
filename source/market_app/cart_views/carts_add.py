from django.shortcuts import get_object_or_404, redirect
from market_app.models.cart import ProductInCart
from market_app.models import Product


def cart_add_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    qty = 1
    try:
        cart_product = ProductInCart.objects.get(product=product)
        cart_product.quantity += qty
        if cart_product.quantity <= product.remainder:
            cart_product.save()
    except ProductInCart.DoesNotExist:
        if qty <= product.remainder:
            ProductInCart.objects.create(product=product, quantity=qty)
    return redirect('home')

