# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('product-detail/<product_id>/', views.product_detail, name='product-detail'),
    # Other URL patterns for products as needed
]
