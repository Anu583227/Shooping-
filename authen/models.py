from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProfileModel(models.Model):
    profile_img=models.ImageField(upload_to='uploads/',default='patlu.jpg')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
