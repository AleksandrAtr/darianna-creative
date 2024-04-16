
def bag_contents(request):
    """
    Calculate the contents of the shopping bag.

    Args:
        request: The HTTP request object.

    Returns:
        dict: A dictionary containing bag items, total price, product count,
              delivery cost, and grand total.
    """
    bag_items = []  # List to store items in the bag
    total = 0  # Total price of items in the bag
    product_count = 0  # Number of products in the bag
    delivery = 0  # Delivery cost

    # Calculate grand total by adding delivery cost and total price
    grand_total = delivery + total

    # Prepare context dictionary with bag details
    context = {
        'bag_items': bag_items,  # List of items in the bag
        'total': total,  # Total price of items in the bag
        'product_count': product_count,  # Number of products in the bag
        'delivery': delivery,  # Delivery cost
        'grand_total': grand_total,  # Grand total including delivery cost
    }

    return context  # Return the context dictionary
