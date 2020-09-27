from django.db import models
from Profile.models import User
from Event.models import Exhibition, Competition
from django.contrib.auth.models import User


# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="")
    medium = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    art_description = models.TextField(max_length=100, null=True)
    art = models.ImageField(upload_to='images/art/', blank=False)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Arrange(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.SET_NULL, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True)
