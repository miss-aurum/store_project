from rest_framework import serializers
from .models import *

class UserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManager
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'