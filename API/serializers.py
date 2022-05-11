from rest_framework import serializers
from Authentication.models import CustomUser
from Complaint.models import Complaints


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'phone', 'nsu_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'phone', 'nsu_id', 'password']


class AgainstUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']


class ReviewerUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = '__all__'
