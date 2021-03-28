import pybithumb
import time
import datetime

ticker = "BTC"

# 목표가 구하기
def cal_target(ticker):
    df = pybithumb.get_candlestick(ticker, chart_intervals='30m')
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return target

# 5분치 이동평균선 구하기
def get_yesterday_ma5(ticker):
    df = pybithumb.get_candlestick(ticker, chart_intervals='30m')
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma[-2]

# 객체 생성
f = open("bithumb.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
bithumb = pybithumb.Bithumb(access, secret)

# 변수 설정
op_mode = True
hold = False
print("It's", datetime.datetime.now(), "Start Auto Trading! Hope your succeed Investment!!")

#krw = bithumb.get_balance(ticker)[2]
#orderbook = pybithumb.get_orderbook(ticker)
#asks = orderbook['asks']
#sell_price = asks[0]['price']
#unit = krw/float(sell_price)
#order = bithumb.buy_market_order("BTC", unit)

# 트레이딩 반복
while True:
    target = cal_target(ticker)  # 목표가격
    price = pybithumb.get_current_price(ticker)  # 코인 현재가
    ma = get_yesterday_ma5(ticker)  # 코인 5분 이동평균선
    limit = target * 0.08  # 손절 가격
    profit = target * 1.02

    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    asks = orderbook['asks']
    sell_price = asks[0]['price']
    unit = krw/float(sell_price)

    try:
        # 조건을 확인한 후 매수 시도
        if op_mode == True and price >= target and hold == False and ma < price:
            # 매수
            #krw_balance = bithumb.get_balance("KRW")
            order = bithumb.buy_market_order(ticker, unit)
            hold = True
            op_mode = False
            print("상승장입니다. 매수 하였습니다. 매도할 타이밍을 보고 있습니다...")

        # 목표가에서 2% 이상 하락하면 손절
        if op_mode == False and hold == True and limit > price:
            #coin_balance = bithumb.get_balance(ticker)
            bithumb.sell_market_order(ticker, unit)
            hold = False
            op_mode = True
            print("손해입니다. :( 다른 기회를 찾는 중입니다....")

        # 목표가에서 2% 이상 수익나면 익절
        if op_mode == False and hold == True and profit < price:
            bithumb.sell_market_order(ticker, unit)
            hold = False
            op_mode = True
            print("축하합니다!", (price - target), "원 이익입니다.")

        # 상태 출력
        #print(f"코인: {ticker} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")
    except:
        pass
    time.sleep(1)
