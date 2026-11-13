from django.shortcuts import render,redirect
from product.models import ProductModel
from .models import CartModel

# Create your views here.

def cart(request):
    cart_item=CartModel.objects.filter(user=request.user)
    TA=0
    for i in cart_item:
        TA+=i.total_price
    return render(request,'cart.html',{'cart_item':cart_item,'TA':TA})

def add_to_cart(request,pk):
    item=ProductModel.objects.get(id=pk)
    try:
        cart_item=CartModel.objects.get(prduct=item.id)
        cart_item.product_count +=1
        cart_item.total_price += item.price
        cart_item.save()
        return redirect('cart')
    except:
        CartModel.objects.create(
            user=request.user,
            prduct=item,
            total_price=item.price
        )
        return redirect('cart')

def remove(request,pk):
    item=CartModel.objects.get(id=pk).delete()
    return redirect('cart')

def plus(request,pk):
    data=CartModel.objects.get(id=pk)
    data.product_count +=1
    data.total_price +=data.prduct.price
    data.save()
    return redirect('cart')

def minus(request,pk):
    data=CartModel.objects.get(id=pk)
    if data.product_count >1:
        data.product_count -=1
        data.total_price -= data.prduct.price
        data.save()
    else:
        data.delete()
    return redirect('cart')
