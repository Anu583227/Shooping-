from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import ProfileModel
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        pasw=request.POST['pasw']
        user=authenticate(username=uname,password=pasw)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login_')


    return render(request,'login_.html')

def register(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pasw=request.POST['pasw']
        pic=request.FILES.get('pic')
        print(request.FILES)

        user=User.objects.create_user(
            username=uname,
            email=email,
            first_name=fname,
            last_name=lname,
            password=pasw,
            
        )
        pic_img=ProfileModel.objects.create(
            user=user,
            profile_img=pic
        )
        print(pic_img.profile_img)
        print(pic_img.profile_img.name)
    return render(request,'register.html')

def logout_(request):
    logout(request)
    return redirect('login_')

@login_required
def profile(request):
    data = request.user
    return render(request, 'profile.html', {'data': data})

@login_required
def update(request):
    data = request.user
    profile = ProfileModel.objects.filter(user=request.user).first()

    if request.method == 'POST':
        data.username = request.POST['uname']
        data.first_name = request.POST['fname']
        data.last_name = request.POST['lname']
        data.email = request.POST['email']

        if request.FILES.get('pic'):
            if profile:
                profile.profile_img = request.FILES['pic']
                profile.save()
            else:
                ProfileModel.objects.create(
                    user=request.user,
                    profile_img=request.FILES['pic']
                )

        data.save()

        return redirect('profile')

    return render(request, 'update.html', {
        'data': data,
        'profile': profile
    })



