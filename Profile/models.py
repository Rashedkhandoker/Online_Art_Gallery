from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


