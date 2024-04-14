from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)

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
    
    
class Product(models.Model):
    PRODUCT_TYPES = ( 
        ('artsale', 'Art sale'),
        ('photosession', 'Photography session'),
        ('workshop', 'Workshop'),
    )
    
    category = models.ForeignKey('Category', null=True, blank=True, 
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, 
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=PRODUCT_TYPES)

    def __str__(self):
        return self.name
    
    def get_type_display_name(self):
        for value, display_name in self.PRODUCT_TYPES:
            if value == self.type:
                return display_name
        return None
    
class ArtSale(models.Model):
    PRINT_SIZE = ( 
        ('6x9', '6 by 9'),
        ('11x17', '11 by 17'),
        ('23x35', '23 by 35'),
        ('polaroid', 'Polaroid'),
    )

    product = models.OneToOneField(Product, on_delete=models.CASCADE, 
                                   primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=100, choices=PRINT_SIZE)
    
class PhotographySession(models.Model):
    PHOTOSESSION_TYPE = (
        ('45MIN', 'Express Portrait Session (45 minutes)'),
        ('120MIN', 'Extended Portrait Session (120 minutes)'),
        ('360MIN', 'Intensive Portrait Session (360 minutes)'),
    )
    
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    session_type = models.CharField(max_length=6, choices=PHOTOSESSION_TYPE)


class Workshop(models.Model):
    WORKSHOP_TYPE = (
        ('HALF-DAY', 'Half-Day Workshop'),
        ('ONE-DAY', 'One-Day Workshop'),
        ('TWO-DAY', 'Two-Day Workshop'),
    )
    
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    session_type = models.CharField(max_length=8, choices=WORKSHOP_TYPE)



