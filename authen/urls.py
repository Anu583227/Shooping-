from django.urls import path
from .views import *

urlpatterns=[
    path('',login_,name='login_'),
    path('register/',register,name='register'),
    path('logout_/',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('update/',update,name='update')
]