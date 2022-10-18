from django.urls import path
from market_app.products_views.base import HomeView
from market_app.products_views.products_detail import ProductDetailView
from market_app.products_views.products_add import ProductCreateView
from market_app.products_views.products_delete import ProductDeleteView
from market_app.products_views.products_update import ProductUpdateView
from market_app.cart_views.base_cart import CartHomeView
from market_app.cart_views.carts_delete import cart_delete, ProductInCartDeleteView
from market_app.cart_views.carts_add import cart_add_product


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('cart_home', CartHomeView.as_view(), name='home_cart'),
    path("cart_home/delete/<int:pk>/", cart_delete, name="product_cart_delete"),
    path("cart_home/delete_all/<int:pk>/", ProductInCartDeleteView.as_view(), name="cart_delete"),
    path("cart_home/add_product/<int:pk>/", cart_add_product, name="product_cart_add")
]

