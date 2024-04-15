from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'rating',
        'image',
        'price'
    )

admin.site.register(Product, ProductsAdmin)
admin.site.register(Category)

