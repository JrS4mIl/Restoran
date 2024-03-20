from django.urls import path,include
from .views import *

urlpatterns = [
    path('',marketplace,name='marketplace'),
    path('/<slug:vendor_slug>',vendor_detail,name='vendor_detail')
]