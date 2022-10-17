from django.views.generic import ListView
from market_app.models.cart import ProductInCart


class CartHomeView(ListView):
    template_name = 'carts/home_cart.html'
    context_object_name = 'carts'
    model = ProductInCart

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['total'] = ProductInCart.get_total()
        return context

