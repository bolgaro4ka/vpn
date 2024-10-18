# myapp/urls.py
from django.urls import path
from .views import getTariffs, pay, changeTariff, create_payment_req


urlpatterns = [
    path('tariffs/', getTariffs, name='tariffs'),  # get all Tariffs
    path('payt/', pay, name='payt'),
    path('changet/', changeTariff, name='changet'),
    path('cpr/', create_payment_req, name='cpr'),
]