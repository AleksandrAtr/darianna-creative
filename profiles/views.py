from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile.

    Requires the user to be logged in.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered user profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. '
                           'Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
        # 'on_profile_page': True
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def order_history(request, order_number):
    """
    Display the order history of the user.

    Requires the user to be logged in.

    Args:
        request (HttpRequest): The request object.
        order_number (str): The order number.

    Returns:
        HttpResponse: The rendered order history page.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for Order Number: {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
