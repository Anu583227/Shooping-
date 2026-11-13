from django.urls import path
from .views import *

urlpatterns=[
    path('checkout/',checkout,name='checkout'),
    path('order_/',order_,name='order_'),
]