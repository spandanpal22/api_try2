from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model=Stock

        """
        Whatever field we declare here those fields are only shown  
        """
        #fields=('ticker','volume')
        fields='__all__'