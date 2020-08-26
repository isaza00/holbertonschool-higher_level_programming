#!/usr/bin/env python3
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
import json

key = 'U24ZCUNRMX8O42FJ'

stock_filename = "data_stock.json"
symbol = "TSLA"

ts = TimeSeries(key=key)
data, meta_data = ts.get_quote_endpoint(symbol)

with open(stock_filename, mode="w", encoding='utf-8') as file:
    json.dump(data, file)

currency_filename = "data_currency.json"
up = "EUR"
down = "USD"

cc = ForeignExchange(key=key)
# There is no metadata in this call
data, _ = cc.get_currency_exchange_intraday(up, down, interval='1min', outputsize='compact')
with open(currency_filename, mode="w", encoding='utf-8') as file:
    json.dump(data, file)
