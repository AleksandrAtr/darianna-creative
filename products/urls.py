# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('product-detail/<product_id>/', views.product_detail, name='product-detail'),
    path('add/', views.add_product, name='add_product'),
]
