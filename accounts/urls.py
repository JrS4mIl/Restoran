from django.urls import path
from .views import registerUser,registerVendor,login,logout,vendorDashboard,MyAccount,custDashboard
urlpatterns = [
    path('registerUser/',registerUser,name='registerUser'),
    path('registerVendor/',registerVendor,name='registerVendor'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('MyAccount/',MyAccount,name='MyAccount'),
    path('custDashboard/',custDashboard,name='custDashboard'),
    path('vendorDashboard/',vendorDashboard,name='vendorDashboard')


]