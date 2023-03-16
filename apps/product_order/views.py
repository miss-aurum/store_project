from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

class OrderModelViewset(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer


class  OrderProductViwset(viewsets.ModelViewSet):
    queryset =  OrderProduct.objects.all()
    serializer_class =  OrderProductSerializer

    
