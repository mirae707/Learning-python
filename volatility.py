import pyupbit
import time
import datetime

#ticker = "KRW-TRX"
tickers = pyupbit.get_tickers("KRW")

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
op_mode = False
#hold = False

while True:
    for ticker in tickers:
        target = cal_target(ticker)  # 목표가격
        coin_balance = upbit.get_balance(ticker)  # 코인 잔고
        my_balance = upbit.get_balance("KRW")  # 원화 잔고
        price = pyupbit.get_current_price(ticker)  # 코인 현재가
        ma = get_yesterday_ma5(ticker)  # 코인 5일 이동평균선
        limit = target * 0.9  # 손절 가격

        # 지갑에 코인을 보유하고 있는지 조회
        if coin_balance > 0:
            hold = True
        else:
            hold = False

        # 5만원 이상인 경우 코인 잔고가 0으로 나오므로 제외
        if price > 50000 or my_balance < 50000:  # 코인가격이 5만원 초과이거나 내 계좌 잔고가 5만원 미만인 경우
            op_mode = False
        else:
            op_mode = True
        try:
            now = datetime.datetime.now()
            # 매도 시도
            #if now.hour == 8 and now.minute == 59 and 50 <= now.second <= 59:
            if 6 <= now.hour <= 9:
                if op_mode == True and hold == True:
                    #coin_balance = upbit.get_balance(ticker)
                    upbit.sell_market_order(ticker, coin_balance)
                    #hold = False
                #op_mode = False
                #time.sleep(10)

            # 09:00:00 목표가 갱신
            #if now.hour == 9 and now.minute == 0 and (10 <= now.second <= 30):
                #target = cal_target(ticker)
                #time.sleep(10)
                #op_mode = True

            # 조건을 확인한 후 매수 시도
            elif op_mode == True and price >= target and hold == False and ma < price:
                # 매수
                #krw_balance = upbit.get_balance("KRW")
                upbit.buy_market_order(ticker, 50000)
                #hold = True

            # 매수가에서 10% 이상 하락하면 손절
            elif hold == True and price < limit:
                #coin_balance = upbit.get_balance(ticker)
                upbit.sell_market_order(ticker, coin_balance)
                #hold = False

            # 상태 출력
            print(f"현재시간: {now} 코인: {ticker}목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")

        except:
            pass
        time.sleep(5)
