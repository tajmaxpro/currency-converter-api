from django.urls import path
from .views import CurrencyConverterView

urlpatterns = [
    path('convert/', CurrencyConverterView.as_view(), name='currency-converter')
]