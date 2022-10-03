from django.urls import path

from market_app.views.base import products_view
from market_app.views.products_add import product_view
from market_app.views.products_add import add_view
from market_app.views.products_delete import delete_view
from market_app.views.products_update import update_view


urlpatterns = [
    path('', products_view, name='home'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('products/add/', add_view, name='product_add'),
    path('products/delete/<int:pk>', delete_view, name='product_delete'),
    path('products/update/<int:pk>', update_view, name='product_update')
]

