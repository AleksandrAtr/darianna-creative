from django.urls import path
from . import views
from products.views import product_detail

# Define URL patterns for the headshots app
urlpatterns = [
    path('', views.workshop_products, name='workshop'),
    path('product_detail/<product_id>/', product_detail, name='product_detail'),
]