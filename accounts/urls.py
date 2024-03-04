from django.urls import path
from .views import registerUser,registerVendor,login,logout,vendorDashboard,MyAccount,custDashboard,activate,forgotPassword,resetPassword,reset_password_validate
urlpatterns = [
    path('registerUser/',registerUser,name='registerUser'),
    path('registerVendor/',registerVendor,name='registerVendor'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('MyAccount/',MyAccount,name='MyAccount'),
    path('custDashboard/',custDashboard,name='custDashboard'),
    path('vendorDashboard/',vendorDashboard,name='vendorDashboard'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

    path('forgotPassword/', forgotPassword, name='forgotPassword'),

    path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),
    path('resetPassword/', resetPassword, name='resetPassword'),
]