from django.urls import path
from .views import *

urlpatterns=[
    path('checkout/',checkout,name='checkout'),
    path('order_/',order_,name='order_'),
    path('add_address/',add_address,name='add_address'),
    path('address/',address,name='address'),
    path('delete_address/<int:pk>',delete_address,name='delete_address'),
    path('update_add/<int:pk>',update_add,name='update_add'),
]