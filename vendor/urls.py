from django.urls import path,include
from .views import *
from accounts import views as AccountViews
urlpatterns = [
    path('',AccountViews.vendorDashboard,name='vendor'),
    path('profile/',vprofile,name='vprofile'),
    path('menu-builder',menu_builder,name='menu_builder'),
    path('menu-builder/category/<int:pk>/',fooditems_by_category,name='fooditems_by_category'),
    path('menu-builder/category/add/', add_category, name='add_category'),
    path('menu-builder/category/edit/<int:pk>/', edit_category, name='edit_category'),
    path('menu-builder/category/delete/<int:pk>/', delete_category, name='delete_category'),

    #FoodItemCrud
    path('menu-builder/food/add',add_food,name='add_food'),
    path('menu-builder/food/edit/<int:pk>/', edit_food, name='edit_food'),
    path('menu-builder/food/delete/<int:pk>/', delete_food, name='delete_food'),

]