import pyupbit
import numpy as np
#import pandas as pd

ticker = "KRW-TRX"

n = 20 # n분봉 데이터
df = pyupbit.get_ohlcv(ticker, interval="minute1", count=n+1)

target_volume = np.mean(df.iloc[0:n]['volume']) * 1.5 # 목표 거래량
middle_band = np.mean(df.iloc[0:n]['close']) # 볼린저 중간밴드
deviation = np.std(df.iloc[0:n]['close']) # 표준편차
upper_band = middle_band + (deviation * 2) # 볼린저 상단밴드
lower_band = middle_band - (deviation * 2) # 볼린저 하단밴드

def cal_rsi():
    U = np.where(df.diff(1).iloc[-2]['close'] > 0, df.diff(1)[-2]['close'], 0)
    D = np.where(df.diff(1).iloc[-2]['close'] < 0, df.diff(1)[-2]['close'] * (-1), 0)
    
#def target_volume():
#    total = 0
#    for i in range(0, n, 1):
#        total += df.iloc[i]['volume']
#    avg = total / n
#    inc_volume = avg * 1.5
#    return inc_volume

#def middle_band():
#    total = 0
#    for i in range(0, n, 1):
#        total += df.iloc[i]['close']
#    avg = total / n
#    return avg
#

#def standard_deviation():
#    data = []
#    total = 0
#    for i in range(0, n, 1):
#        data[i] = df.iloc[i]['close'] - middle_band
#        data[i] = data[i] * data[i]
#        total += data[i]
#    result = total / (n - 1)
#    return result
