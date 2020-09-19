from django.db import models
from Profile.models import User

# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=100,default="")
    status = models.CharField(max_length=100,default="")
    medium = models.CharField(max_length=100,default="")
    category = models.CharField(max_length=100,default="")

    def __str__(self):

        return self.title




