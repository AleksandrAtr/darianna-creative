from django.contrib import admin
from .models import Product, Category

# Register your models here.

# Define a custom admin class for the Product model.
class ProductsAdmin(admin.ModelAdmin):
    """
    Admin class to customize the display of Product model in the Django admin 
    interface.
    """
    
    list_display = (
        'sku',
        'name',
        'category',
        'rating',
        'image',
        'price'
    )


# Define a custom admin class for the Category model.
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class to customize the display of Category model in the Django admin 
    interface.
    """
    
    list_display = (
        'friendly_name',
        'name'
    )   

# Register the Product model with the ProductsAdmin options in the Django admin 
# interface.
admin.site.register(Product, ProductsAdmin)
admin.site.register(Category,CategoryAdmin)

