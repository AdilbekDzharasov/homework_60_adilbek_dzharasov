from django import forms
from market_app.models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'categories', 'remainder', 'price')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")

