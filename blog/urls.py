from django.urls import path
from . import views

# Define URL patterns for the home app
urlpatterns = [
    path('', views.blog_post_list, name='blog'),
]