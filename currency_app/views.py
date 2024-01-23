from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta, timezone

from .models import CurrencyRate
from .serializers import CurrencyRateSerializer
from .services import get_course


class GetCurrentUSDView(APIView):
    """
    Запрос актуального курса доллара к рублю
    """

    def get(self, request, *args, **kwargs):

        """
        Вывод словаря с актуальным курсом и списком последних 10ти запросов.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        last_request_time = CurrencyRate.objects.last()

        if last_request_time:
            current_time = datetime.now(timezone.utc)
            time_difference = current_time - last_request_time.timestamp

            # Если прошло менее 10 секунд с последнего запроса, возвращаем ошибку
            if time_difference < timedelta(seconds=10):
                return Response({'error': 'Too many requests. Please try again later.'},
                                status=status.HTTP_429_TOO_MANY_REQUESTS)

        get_currency_rate = get_course()

        if get_currency_rate:
            rate_rub = get_currency_rate['Value']

            CurrencyRate.objects.create(rate=rate_rub)

            last_10_rates = CurrencyRate.objects.all()[:10]
            serializer_t = CurrencyRateSerializer(last_10_rates, many=True)

            result = {
                'topical': rate_rub,
                'last_10_rates': serializer_t.data,
            }

            return Response(result)

        return Response({'error': 'Failed to retrieve USD to RUB rate'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
