from django.urls import path
from . import views
from products.views import product_detail

# Define URL patterns for the headshots app
urlpatterns = [
    path('artsale', views.artsale_products, name='artsale'),
    path('product_detail/<product_id>/', product_detail, name='product_detail'),
]