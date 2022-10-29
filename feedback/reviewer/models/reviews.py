from django.contrib.auth import get_user_model
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='reviews',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='reviewer.Product',
        verbose_name='Товар',
        related_name='reviews',
        on_delete=models.CASCADE
    )
    text = models.CharField(
        verbose_name='Текст отзыва',
        null=False,
        blank=False,
        max_length=200
    )
    score = models.IntegerField(
        verbose_name='Оценка',
        # validators=[MinValueValidator(1), MaxValueValidator(5)])
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
        return f"{self.text} {self.score}"
