# myapp/serializers.py
from rest_framework import serializers
from .models import Tariff
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'tel', 'middle_name', 'wallet', 'paid', 'tariff' ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tel=validated_data['tel'],
            middle_name=validated_data['middle_name'],
            wallet=validated_data['wallet'],
            paid=validated_data['paid']
        )
        return user




class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'  # Or specify the fields you need
