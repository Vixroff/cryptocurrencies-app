from django.views.generic import ListView, RedirectView

from .models import CryptoCurrency
from .tasks import create_or_update_cryptocurrencies


class MainView(ListView):
    model = CryptoCurrency
    template_name = 'cryptos.html'
    context_object_name = 'cryptos'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-market_cap')


class RefreshCrypto(RedirectView):
    """
    Refresh cryptocurrencies data by running `create_or_update_cryptocurrencies` task.
    """

    pattern_name = 'main'

    def get(self, request, *args, **kwargs):
        task = create_or_update_cryptocurrencies.delay()
        while not task.ready():
            pass
        return super().get(request, *args, **kwargs)

