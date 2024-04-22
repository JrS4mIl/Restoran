from django.contrib import admin
from .models import Payment,Order,OrderedFood

class OrderedFoodItem(admin.TabularInline):
    model = OrderedFood
    readonly_fields = ('order','payment','user','fooditem','quantity','amount')
    extra =0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number','name','phone','email','total','payment_method','status','is_ordered')
    inlines = [OrderedFoodItem]

admin.site.register(Payment)
admin.site.register(OrderedFood)
admin.site.register(Order,OrderAdmin)

# Register your models here.
