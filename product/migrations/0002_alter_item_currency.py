# Generated by Django 5.0 on 2024-01-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'usd'), ('rub', 'rub')], default='rub', max_length=3, verbose_name='валюта оплаты'),
        ),
    ]