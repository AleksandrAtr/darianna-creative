from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.contrib import messages


def product_detail(request, product_id):
    """
    Display the detail page for a specific product.

    Args:
        request (HttpRequest): The request object.
        product_id (int): The primary key of the product to be displayed.

    Returns:
        HttpResponse: The rendered product detail page.
        If the product with the specified product_id does not exist, a 404 
        error page is returned.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all().order_by('-created_on')

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store.

    Requires the user to be logged in as a superuser.

    Returns:
        HttpResponse: The rendered add product page.
        If the user is not a superuser, redirects to the home page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. '
                           'Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store.

    Requires the user to be logged in as a superuser.

    Args:
        request (HttpRequest): The request object.
        product_id (int): The primary key of the product to be edited.

    Returns:
        HttpResponse: The rendered edit product page.
        If the user is not a superuser, redirects to the home page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product-detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. '
                           'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store.

    Requires the user to be logged in as a superuser.

    Args:
        request (HttpRequest): The request object.
        product_id (int): The primary key of the product to be deleted.

    Returns:
        HttpResponse: Redirects to the home page after deleting the product.
        If the user is not a superuser, redirects to the home page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('home'))
