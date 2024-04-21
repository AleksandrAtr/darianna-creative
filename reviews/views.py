from django.shortcuts import render, reverse, redirect, get_object_or_404
from products.models import Product
from .forms import ReviewForm
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.
def add_review(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)
    author = request.user if request.user.is_authenticated else "Anonymous"
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            # Save the review form
            review = form.save(commit=False)
            review.product = product
            review.user = author
            review.save()
            
            messages.success(request, _("New product review added."))
            return redirect('product-detail', product_id=product.id)
        else:
            messages.error(request, _("Form invalid, please try again."))
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'reviews/add_review.html', context)

