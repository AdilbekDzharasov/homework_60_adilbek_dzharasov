from django.shortcuts import render, redirect, get_object_or_404
from market_app.models import Product
from market_app.forms import ProductForm


def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'image': product.image,
            'categories': product.categories,
            'remainder': product.remainder,
            'price': product.price
        })
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.image = form.cleaned_data['image']
            product.categories = form.cleaned_data['categories']
            product.remainder = form.cleaned_data['remainder']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('product_detail', pk=product.pk)
        else:
            return render(request, 'product_update.html', context={'form': form, 'product': product})

