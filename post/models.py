from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=False)
    context = models.TextField()

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    context = models.TextField()

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
