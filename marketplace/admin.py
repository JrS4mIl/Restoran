from django.contrib import admin
from .models import Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('user','fooditem','quantity','update_at')

admin.site.register(Cart,CartAdmin)