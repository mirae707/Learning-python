import pybithumb
import datetime
import time

ticker = "ADA"

con_key = ""
sec_key = ""

bithumb = pybithumb.Bithumb(con_key, sec_key)

def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

def buy_crypto_currency(bithumb, ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price) * 0.7
    return bithumb.buy_market_order(ticker, unit)

def sell_crypto_currency(bithumb, ticker):
    unit = bithumb.get_balance(ticker)[0]
    return bithumb.sell_market_order(ticker, unit)

def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]

def run():
    now = datetime.datetime.now()
    mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
    ma5 = get_yesterday_ma5(ticker)
    target_price = get_target_price(ticker)
    wait_flag = False
    print("target price :", target_price)
    while True:
        try:
            now = datetime.datetime.now()
            if (mid < now) and (now < mid + datetime.timedelta(seconds=10)):
                target_price = get_target_price(ticker)
                mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
                ma5 = get_yesterday_ma5(ticker)
                desc = sell_crypto_currency(bithumb, ticker)

                result = bithumb.get_order_completed(desc)
                timestamp = result['data']['order_date']
                dt = datetime.datetime.fromtimestamp( int(int(timestamp)/1000000) )
                tstring = dt.strftime("%Y/%m/%d %H:%M:%S")
                print(tstring, "매도", result['data']['order_qty'])
                wait_flag = False

            if wait_flag == False:
                current_price = pybithumb.get_current_price(ticker)
                if (current_price > target_price) and (current_price > ma5):
                    desc = buy_crypto_currency(bithumb, ticker)
                    result = bithumb.get_order_completed(desc)
                    timestamp = result['data']['order_date']
                    dt = datetime.datetime.fromtimestamp( int(int(timestamp)/1000000) )
                    tstring = dt.strftime("%Y/%m/%d %H:%M:%S")
                    print(tstring, "매수", result['data']['order_qty'])
                    wait_flag = True
        except:
            pass
        time.sleep(1)

run()
