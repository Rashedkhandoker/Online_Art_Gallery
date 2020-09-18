from django.db import models

# Create your models here.
class Artworks(models.Model):
    title=models.CharField(max_length=100,default="")
    status=models.CharField(max_length=100,default="")
    medium=models.CharField(max_length=100,default="")
    category=models.CharField(max_length=100,default="")

    def __str__(self):

        return self.title




