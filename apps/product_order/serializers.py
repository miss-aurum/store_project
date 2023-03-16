from rest_framework import serializers
from .models import *

class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = OrderProduct
        fields = '__all__'

