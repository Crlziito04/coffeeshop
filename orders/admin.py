from django.contrib import admin
from .models import Orders, OrderProduct

# Register your models here.

class OrderProductInLine(admin.TabularInline):
  model = OrderProduct
  extra = 0



class OrderAdmin(admin.ModelAdmin):
  model=Orders
  inlines =[OrderProductInLine]

admin.site.register(Orders,OrderAdmin)
