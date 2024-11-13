from rest_framework import serializers
from .models import Prices, Shows


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ['id', 'type', 'price', 'shows']


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ['id', 'name', 'date']
