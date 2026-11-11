from django.shortcuts import render
from product.models import ProductModel

# Create your views here.

def home(request):
    all_product=ProductModel.objects.filter(is_delete=False,is_availble=True)
    print(all_product)
    return render(request,'home.html',{'all_product':all_product})


def about(request):
    return render(request,'about.html')