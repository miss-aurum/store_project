from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets


class UserManagerViewset(viewsets.ModelViewSet):
    queryset = UserManager.objects.all()
    serializer_class =  UserManagerSerializer


class UserModelViewset(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer