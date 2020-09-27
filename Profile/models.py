from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    Full_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    contact_no = models.CharField(max_length=100, blank=True)
    Profile_picture =models.ImageField(upload_to='images/pro_pic/',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


