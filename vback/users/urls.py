# myapp/urls.py
from django.urls import path
from .views import LoginView, UserCreate, views_auth_need, getMe, isIAuth
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('test/', isIAuth, name='auth_need'),
    path('reg/', UserCreate.as_view(), name='reg'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('getme/', getMe, name='getme'),



]