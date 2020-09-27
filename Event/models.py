from django.db import models


# Create your models here.

class Exhibition(models.Model):
    exh_id = models.CharField(max_length=100,default="")
    date = models.DateTimeField()

    def __str__(self):
        return self.exh_id


class Competition(models.Model):
    com_id = models.CharField(max_length=100,default="")
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.com_id
