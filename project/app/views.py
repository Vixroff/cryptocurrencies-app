from django.views.generic import ListView, RedirectView, CreateView
from django.urls import reverse_lazy

from .models import CryptoCurrency
from .tasks import create_or_update_cryptocurrencies
from .forms import CreateUserForm


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


class RegistrationView(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('main')
