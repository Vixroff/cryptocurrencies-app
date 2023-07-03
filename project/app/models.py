import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CryptoCurrency(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        verbose_name='Название',
        unique=True,
    )
    symbol = models.CharField(
        verbose_name='Символ'
    )
    price = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        verbose_name='Цена',
    )
    market_cap = models.FloatField(
        verbose_name='Капитализация',
        null=True,
        blank=True,
    )
    volume_24h = models.FloatField(
        verbose_name='Объем торгов за сутки',
        null=True,
        blank=True,
    )
    percent_change_1h = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        verbose_name='Изменение за час',
        null=True,
        blank=True,
    )
    percent_change_24h = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        verbose_name='Изменение за сутки',
        null=True,
        blank=True,
    )
    percent_change_7d = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        verbose_name='Изменение за неделю',
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Криптовалюта'


class User(AbstractUser):
    cryptocurrencies = models.ManyToManyField(CryptoCurrency)
