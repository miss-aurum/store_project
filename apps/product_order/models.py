from django.db import models
import uuid
from product.models import Product
from user.models import UserModel

class OrderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата заказа')
    # amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Сумма заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f"Заказчик: {self.id_user} "




class OrderProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_order = models.ForeignKey(to=OrderModel,related_name='products', on_delete=models.CASCADE)
    quantity_product = models.IntegerField(verbose_name='Количество товара', default=0)
    date_order = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата заказа')
    # amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Сумма заказа')

    class Meta:
        verbose_name = 'Товар в заказах'
        verbose_name_plural = 'Товары в заказах'

    def __str__(self) -> str:
        return f"{self.id_order}| Количество товара: {self.quantity_product} | Название товара: {self.id_product}"
    
    
    