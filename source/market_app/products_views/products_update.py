from django.urls import reverse
from django.views.generic import UpdateView
from market_app.forms import ProductForm
from market_app.models import Product


class ProductUpdateView(UpdateView):
    template_name = 'products/product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('home')

