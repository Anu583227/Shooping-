from django.shortcuts import render
from product.models import ProductModel,CategoryModel
from django.contrib import messages
from authen.views import pro

# Create your views here.

def home(request):
    trend_msg=False
    no_product=False
    if request.user.is_authenticated:
        profile=pro(request)
    else:
        profile=False
    all_product=ProductModel.objects.filter(is_delete=False,is_availble=True).order_by('?')
    category=[]
    # category=CategoryModel.objects.filter(cname=id)
    for i in CategoryModel.objects.all():
        if i not in category:
            category.append(i.cname)


    if 'cat' in request.GET:
        cat=request.GET['cat']
        cat_id=CategoryModel.objects.get(cname=cat)
        all_product=ProductModel.objects.filter(is_delete=False,is_availble=True,category=cat_id).order_by('?')
    elif 'name' in request.GET:
        name=request.GET['name']
        # name_id=CategoryModel.objects.get(cname=name)
        all_product=ProductModel.objects.filter(is_delete=False,is_availble=True,pname__icontains=name)

        if not all_product:
            messages.error(request, 'Product not found')
    elif 'tread' in request.GET:
        all_product=ProductModel.objects.filter(is_delete=False,is_availble=True,tranding=True)
        if all_product.count() ==0:
            trend_msg=True
            no_product=True
    elif 'offer' in request.GET:
        all_product=ProductModel.objects.filter(is_delete=False,is_availble=True,offer=True)
        if all_product.count()==0:
            messages.error(request,'No Offer')

    else:
        all_product=ProductModel.objects.filter(is_delete=False,is_availble=True).order_by('?')

    print(category)
    # print(all_product)
    return render(request,'home.html',{'all_product':all_product,'category':category,'old':True,'new':True,'profile':profile,'trend_msg':trend_msg,'no_product':no_product})

def read(request,pk):
    data=ProductModel.objects.get(id=pk)
    cate=ProductModel.objects.filter(category=data.category).exclude(id=pk).order_by('?')[:3]
    print(cate)
    print(data)
    return render(request,'read.html',{'data':data,'cate':cate,})

def about(request):
    return render(request,'about.html',{'new':True})



