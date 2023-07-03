from django.urls import path, include

from .views import MainView, RefreshCrypto, RegistrationView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('cryptocurrencies/refresh', RefreshCrypto.as_view(), name='refresh-crypto'),
    path('auth/', include('django.contrib.auth.urls')),
    path('register/', RegistrationView.as_view(), name='register'),
]
