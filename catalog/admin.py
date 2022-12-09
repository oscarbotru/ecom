from django.contrib import admin

from catalog.models import Product

# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'count']
    list_filter = ['price', 'count']
