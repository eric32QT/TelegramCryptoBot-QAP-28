import json
import requests
from crypto.data import keys


class ConretionException(Exception):
    pass


class CryptConveret:
    @staticmethod
    def convert(quot: str, base: str, amount: str):
        if quot == base:
            raise ConretionException('same values')
        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConretionException('failed to process currency')
        try:
            quot_tiker = keys[quot]
        except KeyError:
            raise ConretionException('failed to process currency')

        try:
            amount == float(amount)

        except ValueError:
            raise ConretionException(f'failed to process the amount of currency  {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quot_tiker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
