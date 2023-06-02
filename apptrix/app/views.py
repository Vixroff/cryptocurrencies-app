from typing import Any, Dict
from django.views.generic import ListView

from .models import CryptoCurrency


class MainView(ListView):
    model = CryptoCurrency
    template_name = 'cryptos.html'
    context_object_name = 'cryptos'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-market_cap')
