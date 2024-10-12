from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import views, status
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes

from .models import Tariff
from .serializers import TariffSerializer


# Create your views here.
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
@api_view(['GET'])
def getTariffs(request):
    tariffs = Tariff.objects.all()
    serializer = TariffSerializer(tariffs, many=True)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
@api_view(['POST'])
def changeTariff(request):
    tariff = request.data.get('tariff').id
    user = request.user
    user.tariff = Tariff.objects.get(pk=tariff)
    user.save()
    return Response({'message': 'Тариф успешно изменен'})

@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
@api_view(['GET'])
def pay(request):
    user = request.user
    tariff = user.tariff

    if (user.wallet < tariff.ppm):
        return Response({'message': 'Недостаточно средств'})

    user.wallet -= tariff.ppm
    user.paid = True
    user.save()
    return Response({'message': 'Подписка успешно оплачена'})