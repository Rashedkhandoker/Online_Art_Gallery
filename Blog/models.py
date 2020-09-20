from django.db import models
from Profile.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, default="")
    bloggers_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title

class Post(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        unique_together=(('email', 'blog_id'),)