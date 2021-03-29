from bollinger import *
from macd import *
from rsi import *
#from stoch_rsi import *
import pyupbit
import numpy as np
import time

ticker = "KRW-TRX"

# 객체 생성
f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret)

start_balance = upbit.get_balance("KRW")
end_balance = upbit.get_balance("KRW")

op_mode = False # False 작동안함 True 작동함
hold = False # 코인 보유 여부

print("자동매매를 시작합니다. 편히 쉬고 계세요 돈은 제가 벌겠습니다 :)")

while True:
    df = pyupbit.get_ohlcv(ticker, interval="minute5", count=10) # 5분봉 데이터 가져오기

    price = pyupbit.get_current_price(ticker) # 현재 코인 가격
    target_volume = np.mean(df.iloc[:10]['volume']) * 1.5 # 목표 거래량
    current_volume = df.iloc[-1]['volume'] # 현재 거래량

    bband_width = bb(ticker)
    rsi_value =  cal_rsi(ticker)
    macd_value = cal_macd(ticker)

    try:
        if current_volume > target_volume and bband_width < 0.02 and rsi_value < 35 and macd_value == 'buy' and op_mode == True and hold == False:
            limit = price * 0.09 # 손절 가격
            profit = price * 1.01 # 익절 가격
            my_balance = upbit.get_balance("KRW") - 1000 # 원화 잔고
            upbit.buy_market_order(ticker, my_balance)
            time.sleep(5)
            hold = True
            print(ticker, "를 매수했습니다.\n 매도할 타이밍을 지켜보는 중입니다....")

        if hold == True and price < limit:
            coin_balance = upbit.get_balance(ticker)  # 코인 잔고
            upbit.sell_market_order(ticker, coin_balance) # 코인 전량 매도
            time.sleep(5)
            end_balance = upbit.get_balance("KRW")
            rate_of_profit = (start_balance - end_balance) / start_balance
            hold = False
            print(f"손절했습니다. 죄송합니다.\n시작금액: {start_balance} 현재잔고: {end_balance} 수익률: {rate_of_profit}")

        if hold == True and price > profit:
            coin_balance = upbit.get_balance(ticker)  # 코인 잔고
            upbit.sell_market_order(ticker, coin_balance) # 코인 전량 매도
            time.sleep(5)
            end_balance = upbit.get_balance("KRW")
            rate_of_profit = (start_balance - end_balance) / start_balance
            hold = False
            print(f"이익봤어요! 축하드려요~\n시작금액: {start_balance} 현재잔고: {end_balance} 수익률: {rate_of_profit}")
    except:
        pass
