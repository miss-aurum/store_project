from django.contrib import admin

from .models import OrderProduct,OrderModel



@admin.register(OrderProduct)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id')
    search_fields = ('  date_created ',)

@admin.register(OrderModel)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id_order', 'id_product', 'quantity',)
    search_fields = ('id_product',)


