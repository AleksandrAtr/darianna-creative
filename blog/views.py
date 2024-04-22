
from django.shortcuts import render, redirect
from .models import BlogPost

# Create your views here.
def blog_post_list(request):
    posts = BlogPost.objects.all()
    
        # Prepare context data for rendering the template
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


