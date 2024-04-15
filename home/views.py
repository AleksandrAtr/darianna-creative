from django.shortcuts import render

# Create your views here.

def index(request):
    """
    A view function to render the index page.

    Args:
        request: HttpRequest object representing the request made by the client.

    Returns:
        HttpResponse: A response containing the rendered HTML content of the index page.
    """

    return render(request, 'home/index.html')