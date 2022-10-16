from django.urls import reverse
from django.views.generic import CreateView
from market_app.models.product import Product
from market_app.forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_add.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('home')

