#!/usr/bin/python3

import pyupbit
import time
import datetime

tickers = pyupbit.get_tickers("KRW")
#tickers = ["KRW-BTC", "KRW-ETH", "KRW-ADA", "KRW-XRP", "KRW-LTC", "KRW-LINK", "KRW-BCH", "KRW-XLM", "KRW-VET", "KRW-DOGE", "KRW-TRX", "KRW-ATOM", "KRW-THETA", "KRW-DOT", "KRW-CRO", "KRW-EOS", "KRW-BSV", "KRW-BTT", "KRW-XTZ", "KRW-XEM", "KRW-NEO", "KRW-CHZ", "KRW-HBAR", "KRW-TFUEL", "KRW-ENJ", "KRW-NPXS", "KRW-ZIL", "KRW-BAT", "KRW-MANA", "KRW-ETC", "KRW-WAVES", "KRW-ICX", "KRW-ONT", "KRW-ZRX", "KRW-SC", "KRW-ANKR", "KRW-QTUM", "KRW-IOST", "KRW-OMG", "KRW-BTG", "KRW-MVL", "KRW-LSK", "KRW-STORJ"]

# 목표가 구하기
def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day")
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    noise = 1 - abs(yesterday['open'] - yesterday['close']) / (yesterday['high'] - yesterday['low'])
    target = today['open'] + yesterday_range * noise
    return target

# 5일치 이동평균선 구하기
def get_yesterday_ma5(ticker):
    df = pyupbit.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma[-2]

# 객체 생성
f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret)

# 5만원 이상있으면 작동
def op_mode(my_balance):
    if my_balance < 50000:
        return False
    else:
        return True

# 코인 보유 여부
def hold(coin_balance):
    if coin_balance > 0:
        return True
    else:
        return False

print("자동매매를 시작합니다. 꼭 성투하세요!\n적절한 코인을 찾는중입니다....")

while True:
    try:
        now = datetime.datetime.now()
        for ticker in tickers:
            target = cal_target(ticker)  # 목표가격
            coin_balance = upbit.get_balance(ticker)  # 코인 잔고
            my_balance = upbit.get_balance("KRW")  # 원화 잔고
            price = pyupbit.get_current_price(ticker)  # 코인 현재가
            ma = get_yesterday_ma5(ticker)  # 코인 5일 이동평균선

            limit = target * 0.9  # 손절 가격
            profit = target * 1.15 # 익절 가격

            # 매도 시도
            if now.hour == 8 and 50 <= now.minute <= 59: 
                if hold(coin_balance) == True:
                    upbit.sell_market_order(ticker, coin_balance)
                    print(f"현재시간 {now} 하루가 끝났습니다.\n{ticker} 를 매도 하겠습니다. 오늘은 좋은 결과가 있기를!")
                    time.sleep(1)

            # 매일 9시에 코인 리스트 초기화
            elif now.hour == 9 and now.minute == 0 and 0 <= now.second <= 10:
                tickers = pyupbit.get_tickers("KRW")
                time.sleep(5)

            # 조건을 확인한 후 매수 시도
            elif op_mode(my_balance) == True and target <= price <= (target * 1.1) and hold(coin_balance) == False and ma < price:
                # 매수
                upbit.buy_market_order(ticker, 50000)
                print(f"현재시간 {now} 코인 {ticker} 를 찾아서 매수했습니다. 얼마나 오를까요? 5%만 오르길!")
                time.sleep(1)

            # 목표가에서 10% 이상 하락하면 손절
            elif hold(coin_balance) == True and limit > price:
                upbit.sell_market_order(ticker, coin_balance)
                print(f"현재시간 {now} 너무 많이 떨어졌네요. {ticker}를 매도 하겠습니다.")
                tickers.remove(ticker)
                time.sleep(1)

            # 목표가에서 15% 이상 수익나면 익절
            elif hold(coin_balance) == True and profit < price:
                upbit.sell_market_order(ticker, coin_balance)
                print(f"현재시간 {now} 목표치에 도달했습니다! {ticker}를 매도 하겠습니다.")
                tickers.remove(ticker)
                time.sleep(1)
            # 상태 출력
            #print(f"현재시간: {now} 코인: {ticker} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")
    except:
        pass
    time.sleep(1)
