from .serializers import CurrencyConverterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests




class CurrencyConverterView(APIView):
    def get(self, request):
        # Deserialize and validate the request data
        serializer = CurrencyConverterSerializer(data=request.query_params)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            from_currency = validated_data['from_currency']
            to_currency = validated_data['to_currency']
            amount = validated_data['amount']

            api_url = f"https://api.apilayer.com/exchangerates_data/convert?from={from_currency}&to={to_currency}&amount={amount}"
            headers = {"apikey": "gV3QWy48LLuNyypt5IFw7g82T5cNw72x"}
            
            response = requests.get(api_url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                converted_value = data.get("result")
                return Response({"result": converted_value}, status=status.HTTP_200_OK)

            return Response({"error": "Unable to perform currency conversion"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
