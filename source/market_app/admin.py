from django.contrib import admin

from market_app.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'categories', 'remainder', 'price']
    list_filter = ['id', 'name', 'description', 'categories', 'remainder', 'price', 'created_at']
    search_fields = ['id', 'name', 'categories']
    fields = ['id', 'name', 'description', 'image', 'categories', 'remainder',  'price']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)

