from django.views.generic import DetailView
from market_app.models.product import Product


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product.html'

