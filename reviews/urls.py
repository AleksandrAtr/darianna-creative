from django.urls import path
from . import views

# Define URL patterns for the home app
urlpatterns = [
    path('add_review/<int:product_id>', views.add_review, name='add_review'),
]