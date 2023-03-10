from rest_framework import serializers
from .models import *

class OrderModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'

class OrderProductSerializers(serializers.ModelSerializer):
    class Meta:
        model  = OrderProduct
        fields = '__all__'
