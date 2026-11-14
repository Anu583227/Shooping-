from django.shortcuts import render,redirect
from .models import Address
from .forms import AddForm
from cart.models import CartModel

# Create your views here.

def checkout(request):
    cart=CartModel.objects.filter(user=request.user)
    addres=Address.objects.filter(user=request.user)
    grand_total=sum(i.total_price for i in cart)
    print(grand_total)
    return render(request,'checkout.html',{'cart':cart,'addres':addres,'grand_total':grand_total})

def order_(request):
    return render(request,'order_.html')

def add_address(request):
    if request.method =='POST':
        form =AddForm(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.user=request.user
            a.save()
            return redirect('checkout')
    else:
        form = AddForm()
    return render(request,'add_address.html',{'form':form})

def address(request):
    addresses=Address.objects.filter(user=request.user)
    return render(request,'address.html',{'addresses':addresses})

def delete_address(request,pk):
    add=Address.objects.get(id=pk)
    add.delete()
    return redirect('add_address')

def update_add(request,pk):
    data=Address.objects.get(id=pk)
    if request.method=='POST':
        form=AddForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('address')
    form=AddForm(instance=data)
    return render(request,'update_add.html',{'form':form})