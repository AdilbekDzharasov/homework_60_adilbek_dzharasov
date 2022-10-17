from django.contrib import admin
from market_app.models.product import Product
from market_app.models.cart import ProductInCart


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

