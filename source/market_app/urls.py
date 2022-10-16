from django.urls import path
from market_app.products_views.products_delete import delete_view
from market_app.products_views.products_update import update_view

from market_app.products_views.base import HomeView
from market_app.products_views.products_detail import ProductDetailView
from market_app.products_views.products_add import ProductCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/delete/<int:pk>', delete_view, name='product_delete'),
    path('products/update/<int:pk>', update_view, name='product_update')
]

