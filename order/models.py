from django.db import models
from django.contrib.auth.models import User
from product.models import ProductModel

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

class OrderModel(models.Model):
    STATUS_CHOICES=(
        ('Pending','Pending'),
        ('Confirmed','Comfirmed'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order=models.ForeignKey(OrderModel,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveBigIntegerField()
