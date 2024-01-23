from rest_framework import serializers
from .models import CurrencyRate


class CurrencyRateSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели курса валют.
    """

    class Meta:
        model = CurrencyRate
        fields = ('currency', 'rate', 'timestamp')
