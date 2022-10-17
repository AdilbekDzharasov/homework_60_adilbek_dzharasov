from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from market_app.models.cart import ProductInCart


class ProductInCartDeleteView(DeleteView):
    model = ProductInCart
    success_url = reverse_lazy('home_cart')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def cart_delete(request, pk):
    product_cart = get_object_or_404(ProductInCart, pk=pk)
    if product_cart.quantity > 1:
        product_cart.quantity -= 1
        product_cart.save()
    elif product_cart.quantity == 1:
        product_cart.delete()
    return redirect('home_cart')

