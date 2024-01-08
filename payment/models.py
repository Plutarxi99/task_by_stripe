from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from config.settings import NULLABLE
from product.models import Item


class Discount(models.Model):
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                           verbose_name='скидка', **NULLABLE)


class Tax(models.Model):
    tax = models.CharField(max_length=30, verbose_name='налог', **NULLABLE)


class Order(models.Model):
    item = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='order', **NULLABLE)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, related_name='order', **NULLABLE)
