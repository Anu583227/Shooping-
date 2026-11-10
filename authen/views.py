from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import ProfileModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def pro(request):
    profile = get_object_or_404(ProfileModel,user_id = request.user)
    return profile

def login_(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        pasw=request.POST['pasw']
        user=authenticate(username=uname,password=pasw)
        if user:
            login(request,user)
            messages.success(request,'Login Sucuessful ...!')
            return redirect('home')
        else:
            messages.error(request,'Username and password wronge')
            return redirect('login_')


    return render(request,'login_.html',{'new':True})

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
    return render(request,'register.html',{'new':True})

def logout_(request):
    logout(request)
    messages.success(request,'Logout Successfull')
    return redirect('login_')

@login_required
def profile(request):
    data = request.user
    return render(request, 'profile.html', {'data': data,'new':True})

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
        'profile': profile,
        'new':True
    })

# def forgot(request):
#     if request.method=='POST':
#         if 'uname' in request.POST:
#             uname=request.POST['uname']
#             if uname:
#                 u=User.objects.get(username=uname)
#                 return render(request,'forgot.html')
#             else:
#                 messages.error(request,'No user found')
#                 return redirect('login_')
#         if 'npasw' in request.POST:
#             npasw=request.POST['npasw']
#             u=User.objects.get(username=uname)
#             u.set_password(npasw)
#             u.save()
#             return redirect('login_')
            
#     return render(request,'forgot.html')

def forgot(request):
    if request.method=='POST':
        global user
        if 'uname' in request.POST:
            user=request.POST['uname']
            try:
                u=User.objects.get(username=user)
                return render(request,'forgot.html')
            except:
                messages.error(request,'no user found')
                return redirect('forgot')
        if 'npasw' in request.POST:
            npasw=request.POST['npasw']
            u=User.objects.get(username=user)
            u.set_password(npasw)
            u.save()
            messages.success(request,'Password reset succussful...!')
            return redirect('login_')
    return render(request,'forgot.html',{'new':True})

def reset(request):
    if request.method=='POST':
        if 'opasw' in request.POST:
            opasw=request.POST['opasw']
            user=authenticate(username=request.user,password=opasw)
            if user:
                messages.success(request,'Enter new password')
                return render(request,'reset.html',{'new':True})
            else:
                messages.error(request,'Enter old password wrong')
                return redirect('reset')
        if 'npasw' in request.POST:
            npasw=request.POST['npasw']
            cpasw=request.POST['cpasw']
            if npasw != cpasw:
                messages.error(request,'Enter new an confirm password is wrong')
                return redirect('reset')
            else:
                user=User.objects.get(username=request.user)
                user.set_password(npasw)
                user.save()
                return redirect('login_')
    return render(request,'reset.html')




