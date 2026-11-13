from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    mobile=models.IntegerField()
    addres_line=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.PositiveBigIntegerField()
    is_default=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
