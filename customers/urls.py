from django.urls import path
from .views import *
from accounts import views as AccountViews
urlpatterns=[
    path('',AccountViews.custDashboard,name='customer'),
    path('profile/',cprofile,name='cprofile')

]
