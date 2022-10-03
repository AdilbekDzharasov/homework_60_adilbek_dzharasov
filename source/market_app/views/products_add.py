from django.shortcuts import render, redirect, get_object_or_404
from market_app.models import Product, CategoriesChoices
from market_app.forms import ProductForm


def add_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "product_add.html", context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                categories=form.cleaned_data['categories'],
                remainder=form.cleaned_data['remainder'],
                price=form.cleaned_data['price']
            )
            return redirect('product_detail', pk=product.pk)
        else:
            return render(request, 'product_add.html', context={'form': form})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product, "choices": CategoriesChoices.choices})

