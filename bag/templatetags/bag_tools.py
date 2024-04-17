from django import template

# Import the template library from Django
register = template.Library()

# Register the filter with the name 'calc_subtotal'
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal of a product.

    This filter calculates the subtotal of a product by multiplying its price by the quantity.

    Args:
        price: The price of the product.
        quantity: The quantity of the product.

    Returns:
        float: The subtotal of the product.
    """
    # Calculate and return the subtotal
    return price * quantity