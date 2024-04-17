from django.shortcuts import render, redirect, get_object_or_404
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
    # Get the redirect URL from POST data
    redirect_url = request.POST.get('redirect_url')
    
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
    return redirect(redirect_url)