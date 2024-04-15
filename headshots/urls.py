from django.urls import path
from . import views

# Define URL patterns for the headshots app
urlpatterns = [
    path('headshots', views.photo_studio_products, name='headshots')
]