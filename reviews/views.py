from django.shortcuts import render, reverse, redirect, get_object_or_404
from products.models import Product
from .forms import ReviewForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Create your views here.


@login_required()
def add_review(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        author = request.user
        
        if form.is_valid():
            # Save the review form
            review = form.save(commit=False)
            review.product = product
            review.user = author
            review.save()
            
            if product.reviews.count() > 0:
                product.rating = round(
                    product.reviews.aggregate(
                            Avg('rating'))['rating__avg'])
            else:
                product.rating = 0
            product.save()
            
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

