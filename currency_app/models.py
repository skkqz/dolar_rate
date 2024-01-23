from django.db import models


class CurrencyRate(models.Model):
    """
    Модель курса валют
    """

    currency = models.CharField(max_length=10, default='USD', verbose_name='Валюта')
    rate = models.FloatField(default=0.0, verbose_name='Курс')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата', editable=False)

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курс валют'

    def __str__(self):
        return f'{self.currency}: {self.rate}'
