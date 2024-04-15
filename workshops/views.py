from django.shortcuts import render
from products.models import Product, Category
# Create your views here.


def workshop_products(request):
    """
    A view function to display products belonging to the "workshops" 
    category.

    Args:
        request: HttpRequest object representing the request made by the client.

    Returns:
        HttpResponse: A response containing the rendered HTML content of the 
        headshots template, with the filtered products passed to the template 
        context.
    """

    # Retrieve the "workshops" category
    workshops_category = Category.objects.get(name='workshops')

    # Filter products belonging to the "workshops" category
    workshop_products = Product.objects.filter(
        category=workshops_category )

    # Pass the filtered products to the template context
    context = {
        'products': workshop_products
    }

    # Render the template with the filtered products
    return render(request, 'workshops/workshops.html', context)


