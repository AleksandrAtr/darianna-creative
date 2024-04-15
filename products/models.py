from django.db import models

# Define category model representing different product categories.
class Category(models.Model):
    """
    A model to represent a product category.

    Attributes:
        name (CharField): The name of the category.
        friendly_name (CharField): A user-friendly name for the category 
        (optional).
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


# Define product model representing items available for sale.
class Product(models.Model):
    """
    A model to represent a product available for sale.

    Attributes:
        category (ForeignKey): A reference to the Category model representing 
        the product category.
        sku (CharField): A unique stock keeping unit (SKU) code for the product.
        name (CharField): The name of the product.
        description (TextField): A detailed description of the product.
        rating (DecimalField): The rating of the product (if available).
        image_url (URLField): The URL of the product image.
        image (ImageField): An image file representing the product.
        price (DecimalField): The price of the product.
        has_size (BooleanField): Indicates whether the product has size options.
    """

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
