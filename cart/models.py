from django.db import models
from django.contrib.auth.models import User
from product.models import ProductModel

# Create your models here.

class CartModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    prduct=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    product_count=models.PositiveBigIntegerField(default=1)
    total_price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)