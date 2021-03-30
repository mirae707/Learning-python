#!/usr/bin/python3

import pyupbit
import time
import datetime

#tickers = pyupbit.get_tickers("KRW") # 코인 전체 불러오기
# 시가총액 높은 순서로 35코인
tickers = ["KRW-BTC", "KRW-ETH", "KRW-ADA", "KRW-XRP", "KRW-LTC", "KRW-LINK", "KRW-BCH", "KRW-XLM", "KRW-VET", "KRW-DOGE", "KRW-TRX", "KRW-ATOM", "KRW-THETA", "KRW-DOT", "KRW-CRO", "KRW-EOS", "KRW-BSV", "KRW-BTT", "KRW-XTZ", "KRW-XEM", "KRW-NEO", "KRW-CHZ", "KRW-HBAR", "KRW-TFUEL", "KRW-ENJ", "KRW-NPXS", "KRW-ZIL", "KRW-BAT", "KRW-MANA", "KRW-ETC", "KRW-WAVES", "KRW-ICX", "KRW-ONT", "KRW-ANKR", "KRW-QTUM"]
temp_tickers = []

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

# 지정가 예약 주문 취소
def cancel_order(ticker):
    ret = upbit.get_order(ticker)[0].get('uuid')
    upbit.cancel_order(ret)
    print(f"{ticker}의 미체결된 거래내역을 취소했습니다.")

print("자동매매를 시작합니다. 꼭 성투하세요!\n적절한 코인을 찾는중입니다....")

while True:
    try:
        now = datetime.datetime.now()
        for ticker in tickers:
            target = cal_target(ticker)  # 목표가격
            my_balance = upbit.get_balance("KRW")  # 원화 잔고
            time.sleep(1)
            price = pyupbit.get_current_price(ticker)  # 코인 현재가
            ma = get_yesterday_ma5(ticker)  # 코인 5일 이동평균선
            profit = target * 1.06 # 익절 가격

            # 매일 9시에 코인 리스트 초기화
            if now.hour == 9 and now.minute == 0 and 0 <= now.second <= 10:
                tickers = ["KRW-BTC", "KRW-ETH", "KRW-ADA", "KRW-XRP", "KRW-LTC", "KRW-LINK", "KRW-BCH", "KRW-XLM", "KRW-VET", "KRW-DOGE", "KRW-TRX", "KRW-ATOM", "KRW-THETA", "KRW-DOT", "KRW-CRO", "KRW-EOS", "KRW-BSV", "KRW-BTT", "KRW-XTZ", "KRW-XEM", "KRW-NEO", "KRW-CHZ", "KRW-HBAR", "KRW-TFUEL", "KRW-ENJ", "KRW-NPXS", "KRW-ZIL", "KRW-BAT", "KRW-MANA", "KRW-ETC", "KRW-WAVES", "KRW-ICX", "KRW-ONT", "KRW-ANKR", "KRW-QTUM"]
                time.sleep(9)

            # 조건을 확인한 후 매수 시도
            elif op_mode(my_balance) == True and target <= price <= (target * 1.001) and ma < price:
                # 매수
                unit = 50000 / target
                upbit.buy_limit_order(ticker, target, unit) # 목표가로 지정가 매수
                coin_balance = 0
                while coin_balance <= 0:
                    coin_balance = upbit.get_balance(ticker)  # 코인 잔고
                    time.sleep(1)
                    if coin_balance > 0:
                        upbit.sell_limit_order(ticker, profit, coin_balance) # 목표가로 지정가 예약 매도
                        temp_tickers.append(ticker) # 구매한 코인 임시 저장 -> 손절하기 위한 리스트로 보냄
                        tickers.remove(ticker) # 매수한 코인 리스트에서 삭제
                        time.sleep(1)
                print(f"현재시간 {now} 코인 {ticker} 를 찾아서 매수했습니다. 얼마나 오를까요? 5%만 오르길!")

        for ticker in temp_tickers:
            target = cal_target(ticker)  # 목표가격
            limit = target * 0.98  # 손절 가격
            price = pyupbit.get_current_price(ticker)  # 코인 현재가
            coin_balance = upbit.get_balance(ticker)  # 코인 잔고
            # 하루지나면 전 코인 미련없이 매도
            if now.hour == 8 and 55 <= now.minute <= 59:
                cancel_order(ticker)
                upbit.sell_market_order(ticker, coin_balance)
                print(f"현재시간 {now} 하루가 끝났습니다.\n{ticker} 를 매도 하겠습니다. 오늘은 좋은 결과가 있기를!")
                temp_tickers.remove(ticker)
                time.sleep(1)
            # 목표가에서 3% 이상 하락하면 손절
            elif limit > price:
                cancel_order(ticker)
                upbit.sell_market_order(ticker, coin_balance)
                print(f"현재시간 {now} 너무 많이 떨어졌네요. {ticker}를 매도 하겠습니다.")
                temp_tickers.remove(ticker)
                time.sleep(1)
        time.sleep(1)
    except:
        pass
