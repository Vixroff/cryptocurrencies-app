from django.urls import path

from .views import MainView, RefreshCrypto

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('cryptocurrencies/refresh', RefreshCrypto.as_view(), name='refresh-crypto')
]
