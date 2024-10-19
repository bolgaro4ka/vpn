from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import views, status
from rest_framework.response import Response
from django.utils import timezone
from wg.functions import create_wg_config 
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes


from .models import Tariff, Payment
from .serializers import TariffSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Отключить CSRF
# Create your views here.

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
@authentication_classes([CsrfExemptSessionAuthentication, 
                         BasicAuthentication])
def getTariffs(request):
    tariffs = Tariff.objects.all()
    serializer = TariffSerializer(tariffs, many=True)
    return Response(serializer.data)


@permission_classes([permissions.IsAuthenticated])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
@api_view(['POST'])
def changeTariff(request):
    tariff = request.data.get('tariff')
    mof = request.data.get('number_of_files')
    user = request.user

    if user.paid:
        return Response({'message': 'Вы уже оплатили подписку на другой тариф'}, status=status.HTTP_400_BAD_REQUEST)
    user.tariff = Tariff.objects.get(pk=tariff)
    user.number_of_files = mof
    user.save()
    return Response({'message': 'Тариф успешно изменен'})

@permission_classes([permissions.IsAuthenticated])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
@api_view(['GET'])
def pay(request):
    user = request.user
    tariff = user.tariff

    if (user.wallet < tariff.ppm*user.number_of_files):
        return Response({'message': 'Недостаточно средств'})

    user.wallet -= tariff.ppm*user.number_of_files
    user.paid = True
    user.paid_date = timezone.now()
    user.file_path = ''

    for iteration in range(user.number_of_files):
        user.file_path += create_wg_config(user.id, iteration) + ';'

    user.save()
    return Response({'message': 'Подписка успешно оплачена'})


@permission_classes([permissions.IsAuthenticated])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
@api_view(['POST'])
def create_payment_req(request):
    user = request.user

    if Payment.objects.filter(user=user).exists():
        return Response({'error': 'Платеж для данного пользователя уже существует.'}, status=status.HTTP_400_BAD_REQUEST)

    payment = Payment.objects.create(user=user)
    return Response({'payment_id': payment.id})


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
def get_all_payments(request):

    payments = Payment.objects.all()
    res = []

    for item in payments:
        res.append({
            'payment_id': item.id,
            'user_id': item.user.id,
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        })

    return Response(res)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
def delete_payment(request):

    payment_id = request.data.get('payment_id')

    if not Payment.objects.filter(id=payment_id).exists():
        return Response({'error': 'Платеж не найден.'}, status=status.HTTP_404_NOT_FOUND)

    payment = Payment.objects.get(id=payment_id)
    payment.delete()

    Payment.save()

    res = {'message': 'Платеж успешно удален.'}
    return Response(res)

