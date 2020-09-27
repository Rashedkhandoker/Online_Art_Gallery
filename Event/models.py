from django.db import models


# Create your models here.

class Exhibition(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return self.id


class Competition(models.Model):

    date = models.DateTimeField()

    def __str__(self):
        return self.id
