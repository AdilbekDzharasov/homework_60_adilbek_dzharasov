from django import forms
from django.forms import widgets
from market_app.models import CategoriesChoices


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=3000, required=False, label='Detail description', widget=widgets.Textarea)
    image = forms.CharField(max_length=3000, required=False, label='Image', widget=widgets.Textarea)
    categories = forms.ChoiceField(required=True, choices=CategoriesChoices.choices, label='Categories')
    remainder = forms.IntegerField(min_value=0, required=True, label='Remainder')
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label='Price')

