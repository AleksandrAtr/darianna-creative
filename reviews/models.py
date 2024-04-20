from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """ 
    Review Model 
    Represents a review for a product.
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True, blank=True,
        # Reverse relation name to access reviews from Product model
        related_name="reviews",  
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        # Reverse relation name to access reviews from User model
        related_name="reviews"  
    )
    
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    content = models.TextField(
        max_length=750
    )
    rating = models.IntegerField(
        validators=[
            # Validator to ensure rating is not greater than 5
            MaxValueValidator(5, message="Must be between 0-5"),  
            MinValueValidator(0, message="Must be between 0-5")  
        ],
        default=0,
        blank=False,
        null=False
    )
    
    created_on = models.DateField(
        # Automatically set to the current date when a review is created
        auto_now_add=True,  
        blank=False,
        null=False
    )

    def __str__(self):
        """ 
        String representation of Review title 
        This method returns the title of the review when 
        an instance of Review is converted to a string.
        """
        return self.title
