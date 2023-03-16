from django.db import models
import uuid
# from slugify import slugify


class Category(models.Model):
    name  = models.CharField(max_length=20, verbose_name='Имя категории')
    # slug = AutoSlugField(populate_from='name',slugify=set_slugify)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return f"Имя Категории: {self.name}"
    


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, verbose_name='Название товара')
    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=20,decimal_places=2, verbose_name='Цена')
    inStoke = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)

    def __str__(self) -> str:
        return f"Имя продукта: {self.name}"
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    