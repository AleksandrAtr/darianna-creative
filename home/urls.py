from django.urls import path
from . import views

# Define URL patterns for the home app
urlpatterns = [
    path('', views.index, name='home')
]