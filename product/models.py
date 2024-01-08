from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from config.settings import NULLABLE


class Item(models.Model):
    USD = 'usd'
    RUB = 'rub'
    CUR = [
        (USD, 'usd'),
        (RUB, 'rub'),
    ]
    name = models.CharField(max_length=255, verbose_name='наименование товара')
    description = models.CharField(max_length=1000, verbose_name='описание товара', **NULLABLE)
    price = models.IntegerField(verbose_name='цена товара',
                                validators=[MinValueValidator(0.5), MaxValueValidator(999999999)]
                                )
    currency = models.CharField(max_length=3, choices=CUR, default=RUB, verbose_name='валюта оплаты')

    def save(self, *args, **kwargs):
        if self.currency == self.RUB:
            self._get_currency()
        super(Item, self).save(*args, **kwargs)

    def _get_currency(self):
        self.price = self.price * 100

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
