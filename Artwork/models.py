from django.db import models
from Profile.models import User
from Event.models import Exhibition,Competition

# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=100,default="")
    status = models.CharField(max_length=100,default="")
    medium = models.CharField(max_length=100,default="")
    category = models.CharField(max_length=100,default="")

    email=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Arrange(models.Model):
    a_id = models.ForeignKey(Artwork,on_delete=models.CASCADE)
    e_id = models.ForeignKey(Exhibition,on_delete=models.CASCADE)
    c_id = models.ForeignKey(Competition,on_delete=models.CASCADE)

    class Meta:
        unique_together=(('a_id','e_id','c_id'),)











