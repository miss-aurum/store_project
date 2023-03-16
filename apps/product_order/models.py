from django.db import models
import uuid
from apps.product.models import *
from apps.user.models import UserModel

class OrderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата заказа')
    amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Сумма заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f"Заказчик: {self.id_user} "




class OrderProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE)
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    order_sum = models.DecimalField( verbose_name='Сумма заказа', max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.id
    