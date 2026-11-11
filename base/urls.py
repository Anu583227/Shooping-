from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('read/<int:pk>',read,name='read')
]