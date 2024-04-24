from django.shortcuts import render, redirect, reverse, \
    get_object_or_404, HttpResponse
from products.models import Product
# Create your views here.


def view_bag(request):
    """
    A view that renders the bag contents page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered bag contents page.
    """
    return render(request, 'bag/bag.html')  # Render the bag contents page


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag.

    Args:
        request: The HTTP request object.
        item_id (int): The ID of the product to add to the bag.

    Returns:
        HttpResponseRedirect: Redirects to the URL specified in the 
        'redirect_url' POST parameter.
    """
    product = get_object_or_404(Product, pk=item_id)
    # Get quantity of the product to add from POST data
    quantity = int(request.POST.get('quantity')) 
    
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Get the current bag from the session  
    bag = request.session.get('bag', {})  

    # Check if the product has a size variant
    if size:
        # Check if the product is already in the bag
        if item_id in list(bag.keys()):
            # Check if the size variant is already in the bag
            if size in bag[item_id]['items_by_size'].keys():
                # Increment the quantity of the size variant
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # Add the size variant to the bag with the specified quantity
                bag[item_id]['items_by_size'][size] = quantity
        else:
            # Add the product to the bag with the size variant and quantity
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        # Check if the product is already in the bag
        if item_id in list(bag.keys()):
            # Increment the quantity of the product
            bag[item_id] += quantity
        else:
            # Add the product to the bag with the specified quantity
            bag[item_id] = quantity

    # Update the bag in the session
    request.session['bag'] = bag  

    # Redirect to the URL specified in the 'redirect_url' POST parameter
    return redirect(reverse('product-detail', args=[product.id]))


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount.

    This function adjusts the quantity of a product in the shopping bag based 
    on the user's input. If the quantity is set to zero or less, the product 
    is removed from the bag.

    Args:
        request: The HTTP request object.
        item_id (int): The ID of the product to adjust.

    Returns:
        HttpResponseRedirect: Redirects to the bag view page.
    """

    # Retrieve the quantity and size of the product from the request
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    
    # Retrieve the shopping bag from the session or create a new one if it
    # doesn't exist
    bag = request.session.get('bag', {})

    # Adjust the quantity of the product in the bag
    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    # Update the shopping bag in the session
    request.session['bag'] = bag
    
    # Redirect to the bag view page
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag.

    This function removes the specified item from the shopping bag.

    Args:
        request: The HTTP request object.
        item_id (int): The ID of the product to remove.

    Returns:
        HttpResponse: Returns status 200 if successful, status 500 if an 
        error occurs.
    """

    try:
        # Retrieve the size of the product from the request
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        
        # Retrieve the shopping bag from the session or create a new one if 
        # it doesn't exist
        bag = request.session.get('bag', {})

        # Remove the specified item from the shopping bag
        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        # Update the shopping bag in the session
        request.session['bag'] = bag
        
        # Return status 200 to indicate successful removal
        return HttpResponse(status=200)

    except Exception as e:
        # Return status 500 if an error occurs
        return HttpResponse(status=500)
