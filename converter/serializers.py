from rest_framework import serializers


class CurrencyConverterSerializer(serializers.Serializer):
    from_currency = serializers.CharField(max_length=3, required=True)
    to_currency = serializers.CharField(max_length=3, required=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)