from django.shortcuts import render
from products.models import Product, Category
# Create your views here.


def photo_studio_products(request):
    """
    A view function to display products belonging to the "photo-studio" 
    category.

    Args:
        request: HttpRequest object representing the request made by the client.

    Returns:
        HttpResponse: A response containing the rendered HTML content of the 
        headshots template, with the filtered products passed to the template 
        context.
    """

    # Retrieve the "photo-studio" category
    photo_studio_category = Category.objects.get(name='photo_studio')

    # Filter products belonging to the "photo-studio" category
    photo_studio_products = Product.objects.filter(
        category=photo_studio_category)

    # Pass the filtered products to the template context
    context = {
        'products': photo_studio_products
    }

    # Render the template with the filtered products
    return render(request, 'headshots/headshots.html', context)


