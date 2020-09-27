
from django.db import models
from Profile.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, default="")
    bloggers_name = models.CharField(max_length=100, default="")
    blog = models.TextField(max_length=1000, default="")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title

