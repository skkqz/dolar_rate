from django.urls import path
from .views import GetCurrentUSDView


urlpatterns = [
    path('', GetCurrentUSDView.as_view(), name='get_current_usd'),
]
