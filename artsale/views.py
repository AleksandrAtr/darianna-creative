from django.shortcuts import render
from products.models import Product, Category
from django.db.models import Q
# Create your views here.

def artsale_products(request):
    """
    View function to display products belonging to print categories in the art 
    sale section.

    Retrieves the categories for prints, filters products belonging to those 
    categories,
    and passes the filtered products to the template context.

    Args:
        request: HttpRequest object representing the request made by the user.

    Returns:
        HttpResponse: Response containing the rendered template with the 
        filtered products.

    Raises:
        Category.DoesNotExist: If any of the required categories does not 
        exist in the database.
    """
    # Get the categories for prints
    print_architecture_category = Category.objects.get(
        name='print_architecture')
    print_landscape_category = Category.objects.get(name='print_landscape')
    print_people_category = Category.objects.get(name='print_people')

    # Filter products belonging to the print categories
    print_products = Product.objects.filter(
        Q(category=print_architecture_category) |
        Q(category=print_landscape_category) |
        Q(category=print_people_category)
    )

    # Pass the filtered products to the template context
    context = {
        'products': print_products
    }

    # Render the template with the filtered products
    return render(request, 'artsale/artsale.html', context)