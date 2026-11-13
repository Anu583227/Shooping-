from django.urls import path
from .views import *

urlpatterns=[
    path('cart/',cart,name='cart'),
    path('add_to_cart<int:pk>',add_to_cart,name='add_to_cart'),
    path('remove/<int:pk>',remove,name='remove'),
    path('plus/<int:pk>',plus,name='plus'),
    path('minus/<int:pk>',minus,name='minus')
]