import pyupbit
import time
import datetime

ticker = "KRW-ANKR"

# 목표가 구하기
def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, interval='minute15')
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return target

# 5분치 이동평균선 구하기
def get_yesterday_ma5(ticker):
    df = pyupbit.get_ohlcv(ticker, interval='minute15', count=7)
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
op_mode = True
hold = False
print("It's", datetime.datetime.now(), "Start Auto Trading! Hope your succeed Investment!!")

# 트레이딩 반복
while True:
    target = cal_target(ticker)  # 목표가격
    coin_balance = upbit.get_balance(ticker)  # 코인 잔고
    my_balance = upbit.get_balance("KRW")  # 원화 잔고
    price = pyupbit.get_current_price(ticker)  # 코인 현재가
    ma = get_yesterday_ma5(ticker)  # 코인 5분 이동평균선
    limit = target * 0.08  # 손절 가격
    profit = target * 1.02
    ask_size = pyupbit.get_orderbook(ticker)[0]['total_ask_size'] # 매도 물량
    bid_size = pyupbit.get_orderbook(ticker)[0]['total_bid_size'] # 매수 물량

    try:
        # 조건을 확인한 후 매수 시도
        if op_mode == True and price >= target and hold == False and ma < price and ask_size < bid_size:
            # 매수
            #krw_balance = upbit.get_balance("KRW")
            upbit.buy_market_order(ticker, 10000)
            hold = True
            op_mode = False
            print("상승장입니다. 매수 하였습니다. 매도할 타이밍을 보고 있습니다...")

        # 목표가에서 2% 이상 하락하면 손절
        if op_mode == False and hold == True and limit > price:
            #coin_balance = upbit.get_balance(ticker)
            upbit.sell_market_order(ticker, coin_balance)
            hold = False
            op_mode = True
            print("손해입니다. :( 다른 기회를 찾는 중입니다....")

        # 목표가에서 2% 이상 수익나면 익절
        if op_mode == False and hold == True and profit < price:
            upbit.sell_market_order(ticker, coin_balance)
            hold = False
            op_mode = True
            print("축하합니다!", (price - target), "원 이익입니다.")

        # 상태 출력
        #print(f"코인: {ticker} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")
    except:
        pass
    time.sleep(1)
