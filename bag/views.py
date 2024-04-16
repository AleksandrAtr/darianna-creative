from django.shortcuts import render, redirect

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
    # Get quantity of the product to add from POST data
    quantity = int(request.POST.get('quantity')) 
    # Get the redirect URL from POST data
    redirect_url = request.POST.get('redirect_url')
    # Get the current bag from the session  
    bag = request.session.get('bag', {})  

    # Add or update the quantity of the specified product in the bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # Update the bag in the session
    request.session['bag'] = bag  

    # Redirect to the URL specified in the 'redirect_url' POST parameter
    return redirect(redirect_url)