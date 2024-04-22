from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blog_posts"  
    )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2500)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(
        BlogPost, 
        related_name='images', 
        on_delete=models.CASCADE
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"Image for {self.blog_post.title}"
