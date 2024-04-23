from django.shortcuts import render
from products.models import Product, Category
from django.http import Http404
# Create your views here.


def workshop_products(request):
    try:
        # Retrieve the "workshops" category
        workshops_category = Category.objects.get(name='workshops')
        
        # Filter products belonging to the "workshops" category
        workshop_products = Product.objects.filter(category=workshops_category)
        
        # Pass the filtered products to the template context
        context = {'products': workshop_products}
        
        # Render the template with the filtered products
        return render(request, 'workshops/workshops.html', context)
    
    except Category.DoesNotExist:
        # Handle the case where the category does not exist
        raise Http404("The 'workshops' category does not exist.")

