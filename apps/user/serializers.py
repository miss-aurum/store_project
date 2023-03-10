from rest_framework import serializers
from .models import *

class UserManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserManager
        fields = '__all__'

class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'