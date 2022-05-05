from rest_framework import serializers
from Authentication.models import CustomUser


class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'phone', 'nsu_id']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'phone', 'nsu_id']
        