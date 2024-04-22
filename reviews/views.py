from django.shortcuts import render, reverse, redirect, get_object_or_404
from products.models import Product
from .forms import ReviewForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Review


# Add review view
@login_required()  # Requires user authentication
def add_review(request, product_id):
    """ 
    Allows users to add a review for a product.

    Parameters:
    - request: The HTTP request object.
    - product_id: The ID of the product for which the review is being added.

    Returns:
    - Redirects to the product detail page after adding the review.
    """
    # Retrieve the product object or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)
    
    # If the request method is POST, process the form submission
    if request.method == "POST":
        form = ReviewForm(request.POST)
        author = request.user
        
        # If the form data is valid, save the review and update product rating
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = author
            review.save()
            
            # Calculate and update the product's average rating
            if product.reviews.exists():
                product.rating = round(product.reviews.aggregate(
                    Avg('rating'))['rating__avg'] or 0)
            else:
                product.rating = round(review.rating)

            product.save()

            # Display success message and redirect to product detail page
            messages.success(request, _("Product review added."))
            return redirect('product-detail', product_id=product.id)
        else:
            # If form data is invalid, display error message
            messages.error(request, _("Form invalid, please try again."))
    else:
        # If request method is not POST, create a blank form
        form = ReviewForm()
    
    # Prepare context data for rendering the template
    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'reviews/add_review.html', context)



# Edit review view
@login_required()  # Requires user authentication
def edit_review(request, review_id):
    """
    Allows users to edit their own reviews.

    Parameters:
    - request: The HTTP request object.
    - review_id: The ID of the review to be edited.

    Returns:
    - Renders the edit review form template or redirects to the user 
    profile page.
    """

    # Retrieve the review object or return a 404 error if not found
    review = get_object_or_404(Review, pk=review_id)
    product = review.product  # Get the product associated with the review
    next = request.GET.get('next', '') # Get URL for redirect
    # Check if the current user is the owner of the review
    if request.user != review.user:
        # If not the owner, display an error message and redirect to 
        # profile page
        messages.error(request, 'You can only edit your own reviews.')
        return redirect(next)

    # If the request method is POST, process the form submission
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)

        # If the form data is valid, save the review and update product rating
        if form.is_valid():
            form.save()

            # Calculate and update the product's average rating
            product.rating = round(product.reviews.aggregate(
                Avg('rating'))['rating__avg'] or 0)
            product.save()

            # Display success message and redirect to profile page after 
            # successful edit
            messages.success(request, 'Review successfully edited!')
            return redirect(reverse('product-detail', args=[product.id]))

        else:
            # If form data is invalid, display error message
            messages.error(request, "Form invalid, please try again.")

    else:
        # If request method is not POST, populate the form with existing 
        # review data
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing... "{review.title}"')

    # Prepare context data for rendering the template
    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """ 
    Deletes a review.
    
    Parameters:
    - request: The HTTP request object.
    - review_id: The ID of the review to be deleted.

    Returns:
    - Redirects to the user profile page after deleting the review.
    """
    # Retrieve the review object or return a 404 error if not found
    review = get_object_or_404(Review, pk=review_id)
    product = review.product  # Get the product associated with the review
    next = request.GET.get('next', '')

    # Check if the current user is the owner of the review
    if not request.user.is_superuser:
        if request.user != review.user:
        # If not the owner, display an error message and redirect to 
        # profile page
            messages.error(request, 'You can only delete your own reviews.')
            return redirect(next)

    # Delete the review
    review.delete()

    # Update product rating after deleting the review
    if product.reviews.exists():  
        # Calculate and update the product's average rating
        product.rating = round(product.reviews.aggregate(
            Avg('rating'))['rating__avg'] or 0)
    else:
        # If no reviews left, set product rating to 0
        product.rating = 0

    # Save the updated product rating to the database
    product.save()

    # Display success message and redirect to profile page
    messages.success(request, 'Review successfully deleted!')
    return redirect(next)

