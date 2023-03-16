from django.contrib import admin
from .models import Product,Category





@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name')
