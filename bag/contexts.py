from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product

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
    delivery = settings.STANDARD_DELIVERY  # Delivery cost
    
    # Retrieve the 'bag' dictionary from the session, 
    # or initialize an empty dictionary if it doesn't exist
    bag = request.session.get('bag', {})

    # Iterate over each key-value pair in the 'bag' dictionary
    for item_id, item_data in bag.items():
        # Check if the item_data is an integer, indicating a single product 
        # without size variants
        if isinstance(item_data, int):
            # Retrieve the product object from the database based on the item_id
            product = get_object_or_404(Product, pk=item_id)
            
            # Calculate the total price by multiplying the quantity 
            # of the product with its price, and add it to the existing total
            total += item_data * product.price
            
            # Increment the product count by the quantity of the current product
            product_count += item_data
            
            # Append a dictionary containing item_id, quantity, 
            # and the Product object to the 'bag_items' list
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            # Retrieve the product object from the database based on the 
            # item_id
            product = get_object_or_404(Product, pk=item_id)
            # Iterate over each size variant and its quantity in the item_data
            for size, quantity in item_data['items_by_size'].items():
                # Calculate the total price by multiplying the quantity 
                # of the product with its price, and add it to the existing 
                # total
                total += quantity * product.price
                # Increment the product count by the quantity of the current 
                # product
                product_count += quantity
                # Append a dictionary containing item_id, quantity, 
                # the Product object, and the size variant to 
                # the 'bag_items' list
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

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
