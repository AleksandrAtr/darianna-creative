from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'user',
        'title',
        'rating',
        'created_on',
    )

admin.site.register(Review, ReviewAdmin)