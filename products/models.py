from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)

# model for categories
class Category(models.Model):
    """
    Category Model
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ String representation of Category name """
        return self.name

    def get_friendly_name(self):
        """ Model Method to return friendly_name """
        return self.friendly_name
    
# product model
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, 
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, 
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_size = models.BooleanField()
    

    def __str__(self):
        return self.name
    
