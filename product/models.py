from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    cname=models.CharField(max_length=100)
    cimg=models.ImageField(upload_to='category')
    is_delete=models.BooleanField(False)
    created_at=models.DateTimeField(auto_now_add=True)


class ProductModel(models.Model):
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    price=models.IntegerField()
    pdesc=models.TextField()
    quntity=models.IntegerField()
    pimg=models.ImageField(upload_to='product')
    create_at=models.DateTimeField(auto_now_add=True)
    is_delete=models.BooleanField(False)
    is_availble=models.BooleanField(True)
