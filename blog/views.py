from django.shortcuts import render, redirect
from .models import BlogPost


def blog_post_list(request):
    """
    View function to display a list of blog posts.

    Args:
        request: HttpRequest object representing the request made by the user.

    Returns:
        HttpResponse: Response object containing the rendered blog.html 
        template with a context containing all blog posts.
    """
    # Retrieve all blog posts from the database
    posts = BlogPost.objects.all()
    
    # Prepare context data for rendering the template
    context = {
        'posts': posts,
    }

    # Render the blog.html template with the context data
    return render(request, 'blog/blog.html', context)
