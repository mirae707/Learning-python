import pyupbit
import time
import datetime

ticker = "KRW-LUNA"

# 목표가 구하기
def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day")
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * 0.5
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

# 변수 설정
target = cal_target(ticker)
op_mode = False
hold = False

while True:
    try:
        now = datetime.datetime.now()

        # 매도 시도
        if now.hour == 8 and now.minute == 59 and 50 <= now.second <= 59:
            if op_mode is True and hold is True:
                coin_balance = upbit.get_balance(ticker)
                upbit.sell_market_order(ticker, coin_balance)
                hold = False
            op_mode = False
            time.sleep(10)

        # 09:00:00 목표가 갱신
        if now.hour == 9 and now.minute == 0 and (20 <= now.second <= 30):
            target = cal_target(ticker)
            time.sleep(10)
            op_mode = True

        price = pyupbit.get_current_price(ticker)
        ma = get_yesterday_ma5(ticker)

        # 매초마다 조건을 확인한 후 매수 시도
        if op_mode == True and price >= target and hold == False and ma < price:
            # 매수
            krw_balance = upbit.get_balance("KRW")
            upbit.buy_market_order(ticker, 50000)
            hold = True

        # 상태 출력
        print(f"현재시간: {now} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")

    except:
        pass
    time.sleep(10)
