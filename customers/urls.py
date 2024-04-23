from django.urls import path
from .views import *
from accounts import views as AccountViews
urlpatterns=[
    path('',AccountViews.custDashboard,name='customer'),
    path('profile/',cprofile,name='cprofile'),
    path('my-orders/',my_orders,name='customer_my_orders'),
    path('order-detail/<int:order_number>/',order_detail,name='order_detail')

]
