from django.contrib import admin
from market_app.models.product import Product
from market_app.models.cart import ProductInCart
from market_app.models import Order
from market_app.models import OrderProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'categories', 'remainder', 'price']
    list_filter = ['id', 'name', 'description', 'categories', 'remainder', 'price', 'created_at']
    search_fields = ['id', 'name', 'categories']
    fields = ['id', 'name', 'description', 'image', 'categories', 'remainder',  'price']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity']
    list_filter = ['id', 'product', 'quantity']
    search_fields = ['id', 'product']
    fields = ['id', 'product', 'quantity']
    readonly_fields = ['id']


admin.site.register(ProductInCart, ProductInCartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'address']
    list_filter = ['id', 'products', 'name', 'phone', 'address']
    search_fields = ['id', 'products']
    fields = ['id', 'name', 'phone', 'address']
    readonly_fields = ['id']


admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']
    list_filter = ['id', 'order', 'product', 'quantity']
    search_fields = ['id', 'order', 'product']
    fields = ['id', 'order', 'product', 'quantity']
    readonly_fields = ['id']


admin.site.register(OrderProduct, OrderProductAdmin)

