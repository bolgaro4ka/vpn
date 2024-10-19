# myapp/urls.py
from django.urls import path
from .views import getTariffs, pay, changeTariff, create_payment_req, get_all_payments, delete_payment, give_money


urlpatterns = [
    path('tariffs/', getTariffs, name='tariffs'),  # get all Tariffs
    path('payt/', pay, name='payt'),
    path('changet/', changeTariff, name='changet'),
    path('cpr/', create_payment_req, name='cpr'),
    path('gpr/', get_all_payments, name='gpr'),
    path('dpr/', delete_payment, name='dpr'),
    path('give_money/', give_money, name='give_money'),
]