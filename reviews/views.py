from django.shortcuts import render

# Create your views here.
def add_review(request):
    return render(request, 'reviews/add_review.html')