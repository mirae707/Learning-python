#!/usr/bin/python3

import pyupbit
import time
import datetime

ticker = "KRW-TRX"

df = pyupbit.get_ohlcv(ticker, "day")
yesterday = df.iloc[-2]
today = df.iloc[-1]
yesterday_range = yesterday['high'] - yesterday['low']
noise = 1 - abs(yesterday['open'] - yesterday['close']) / (yesterday['high'] - yesterday['low'])
target = today['open'] + yesterday_range * noise
print("noise is", noise, "\ntarget is", target, "current price is", pyupbit.get_current_price(ticker))
