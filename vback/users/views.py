from django.contrib.auth import authenticate, login
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes

from .models import Tariff

from .serializers import TariffSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Отключить CSRF


class LoginView(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, 
                              BasicAuthentication)
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'username': user.username,
                'email': user.email,
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'tel': user.tel,
                'middle_name': user.middle_name,
                'wallet': user.wallet,
                'paid': user.paid,
                'tariff': user.tariff
            })
        else:
            return Response({'error': 'Invalid credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)


class UserCreate(CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication,
                              BasicAuthentication
                              )
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer.data['refresh'] = str(refresh)
            serializer.data['access'] = str(refresh.access_token)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


@permission_classes([IsAuthenticated])
@authentication_classes([CsrfExemptSessionAuthentication, JWTAuthentication, 
                         BasicAuthentication])
@api_view(['GET'])
def views_auth_need(request):
    user = request.user
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        # Добавьте любые другие поля, которые вам нужны
    }
    return Response({'message': 'This is a protected view.',
                     'user': user_data})


@permission_classes([IsAuthenticated])
@authentication_classes([CsrfExemptSessionAuthentication, JWTAuthentication,
                         BasicAuthentication])
@api_view(['GET'])
def getMe(request):
    user = request.user
    tariff_data = TariffSerializer(user.tariff).data if user.tariff else None
    return Response({'username': user.username,
                     'email': user.email,
                     'id': user.id,
                     'first_name': user.first_name,
                     'last_name': user.last_name,
                     'tel': user.tel,
                     'middle_name': user.middle_name,
                     'wallet': user.wallet,
                     'paid': user.paid,
                     'tariff': tariff_data
                     })


@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication,
                         BasicAuthentication])
@api_view(['GET'])
def isIAuth(request):
    return Response({'isAuth': True})

