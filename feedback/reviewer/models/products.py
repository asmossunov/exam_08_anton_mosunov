from django.db import models
from django.db.models import TextChoices


class CategoryChoices(TextChoices):
    FOOD = 'food', 'продукты питания'
    GARDEN = 'garden', 'сад и огород'
    ELECTRONICS = 'electronics', 'электроника'


class Product(models.Model):
    product_name = models.CharField(
        verbose_name='Название товара',
        max_length=200,
        null=False,
        blank=False
    )
    product_category = models.CharField(verbose_name='Категория товара', choices=CategoryChoices.choices,
                                        max_length=100, null=True, blank=True)
    description = models.TextField(
        verbose_name='Описание товара',
        max_length=3000,
        null=False,
        blank=False
    )
    image = models.ImageField(
        null=False,
        blank=True,
        verbose_name='Изображение',
        default='default-product-image.jpg'
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f"{self.product_name} {self.product_category} {self.description}"
