from django.shortcuts import render
from market_app.models import Product, CategoriesChoices


def products_view(request):
    products = Product.objects.filter(remainder__gte=1).order_by('categories', 'name')
    context = {
        "products": products,
        "choices": CategoriesChoices.choices
    }
    return render(request, "home.html", context)

