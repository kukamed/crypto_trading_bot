import os
from binance import Client
from binance.enums import *
from abc import ABC, abstractmethod


class Exchange(ABC):

    @abstractmethod
    def get_last_prices(self):
        pass

    @abstractmethod
    def get_close_prices(self, symbol, interval = '1m', limit = 500):
        pass



class Binance(Exchange):

    def check_client_connection(self):
        try:
            self.client.ping()
        except Exception as e:
            self.client = Client()

    def get_last_prices(self):

        self.check_client_connection()

        mark_prices = self.client.futures_mark_price()
        prices = {}

        for mark_price in mark_prices:
            prices[mark_price['symbol']] = float(mark_price['indexPrice'])

        return prices

    def get_prices_time_series(self, symbol, interval='1m', limit=500):

        self.check_client_connection()

        klines = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        close_prices = []
        for k in klines:
            close_prices.append(float(k[4]))

        return close_prices









