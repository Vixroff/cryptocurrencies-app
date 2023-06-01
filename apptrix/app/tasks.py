import os

import requests

from config import celery_app
from .models import CryptoCurrency


@celery_app.task
def create_or_update_cryptocurrencies():
    """
    Task create new one or update already existed cryptocurrency according to CoinMarketCap API call.
    """

    response = requests.get(
        url=os.getenv('CMC_URL'),
        headers={'X-CMC_PRO_API_KEY': os.getenv('CMC_APIKEY')},
    )
    response.raise_for_status()

    cmc_cryptos = response.json()

    existing_cryptos = {crypto.name: crypto for crypto in CryptoCurrency.objects.all()}

    cryptos_to_update = []
    cryptos_to_create = []

    for cmc_crypto in cmc_cryptos['data']:
        name = cmc_crypto['name']

        if name in existing_cryptos:
            crypto = existing_cryptos.get(name)
            crypto.price = cmc_crypto['quote']['USD']['price']
            crypto.market_cap = cmc_crypto['quote']['USD']['market_cap']
            crypto.volume_24h = cmc_crypto['quote']['USD']['volume_24h']
            crypto.percent_change_1h = cmc_crypto['quote']['USD']['percent_change_1h']
            crypto.percent_change_24h = cmc_crypto['quote']['USD']['percent_change_24h']
            crypto.percent_change_7d = cmc_crypto['quote']['USD']['percent_change_7d']
            cryptos_to_update.append(crypto)
        
        else:
            new_crypto = CryptoCurrency(
                name=name,
                symbol=cmc_crypto['symbol'],
                price=cmc_crypto['quote']['USD']['price'],
                market_cap=cmc_crypto['quote']['USD']['market_cap'],
                volume_24h=cmc_crypto['quote']['USD']['volume_24h'],
                percent_change_1h=cmc_crypto['quote']['USD']['percent_change_1h'],
                percent_change_24h=cmc_crypto['quote']['USD']['percent_change_24h'],
                percent_change_7d=cmc_crypto['quote']['USD']['percent_change_7d'],
            )
            cryptos_to_create.append(new_crypto)
    
    CryptoCurrency.objects.bulk_create(cryptos_to_create)
    CryptoCurrency.objects.bulk_update(
        cryptos_to_update,
        [
            'price',
            'market_cap',
            'volume_24h',
            'percent_change_1h',
            'percent_change_1h',
            'percent_change_24h',
            'percent_change_7d',
        ]
    )
    return True
