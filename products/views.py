from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product, Category
from .forms import ProductForm
from django.contrib import messages

# Create your views here.
def product_detail(request, product_id):
    
    """
    Display the detail page for a specific product.

    Args:
        request: HttpRequest object representing the request made by the user.
        product_id: The primary key of the product to be displayed.

    Returns:
        HttpResponse: The HTTP response containing the rendered product detail 
        page.
        If the product with the specified product_id does not exist, a 404 
        error page is returned.
    """

    # Retrieve the product object with the given product_id from the database
    product = get_object_or_404(Product, pk=product_id)

    # Prepare the context to pass the product data to the template
    context = {
        'product': product,
    }

     # Render the product detail page with the product data
    return render(request, 'products/product_detail.html', context)

def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, ('Failed to add product. Please ensure the form is valid.'))
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)