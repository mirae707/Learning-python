def get_min_order(ticker):
    min_order = None
    if ticker == "ETC":
        min_order = 0.1
    elif ticker == "ETH":
        min_order = 0.5
    elif ticker == "BTC":
        min_order = 0.01
    elif ticker == "XRP":
        min_order = 10
    else:
        min_order = 0.005
    return min_order

min_order = get_min_order("BTC")
print(min_order)
