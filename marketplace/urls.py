from django.urls import path,include
from .views import *

urlpatterns = [
    path('',marketplace,name='marketplace'),
    path('<slug:vendor_slug>/',vendor_detail,name='vendor_detail'),
    path('add_to_cart/<int:food_id>/',add_to_cart,name='add_to_cart')
]