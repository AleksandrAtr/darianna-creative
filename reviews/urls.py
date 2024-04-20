from django.urls import path
from . import views

# Define URL patterns for the home app
urlpatterns = [
    path('', views.add_review, name='add_review')
]