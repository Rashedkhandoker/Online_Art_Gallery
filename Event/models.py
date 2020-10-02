from django.db import models


# Create your models here.


class Competition(models.Model):
    title = models.CharField(max_length=100,default="")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)


    def __str__(self):
        return self.title
