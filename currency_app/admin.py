from django.contrib import admin
from .models import CurrencyRate


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    """
    Админ панель для модели CurrencyRate.
    """

    list_display = ['id', 'currency', 'rate', 'timestamp', ]
