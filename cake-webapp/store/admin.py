from django.contrib import admin
from store.models import Product, OrderItem, Cart

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
