from django.shortcuts import render, get_object_or_404
from products.models import Product
from .forms import ReviewForm

# Create your views here.
def add_review(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)
    
    form = ReviewForm()
    
    template = 'reviews/add_review.html'

    context = {
        'form': form,
        'product': product,
    }
    print(context)

    return render(request, template, context)

