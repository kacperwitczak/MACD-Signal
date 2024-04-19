import numpy as np

def MACD(data, N_a, N_b):
    ema_a = np.array([EMA(data, d, N_a) for d, _ in enumerate(data)])
    ema_b = np.array([EMA(data, d, N_b) for d, _ in enumerate(data)])


    macd = ema_a - ema_b

    return macd


def SIGNAL(data, N):
    signal = np.array([EMA(data, d, N) for d, _ in enumerate(data)])

    return signal


def EMA(prices, day, N):
    alpha = (2 / (N + 1))
    numerator = 0
    denominator = 0
    for i in range(N+1):
        if day-i < 0:
            break

        numerator += prices[day - i] * ((1-alpha)**i)
        denominator += (1-alpha)**i

    ema = numerator / denominator

    return ema


def trading_algorithm(stock_shares_, start_day, days, prices, macd, signal):
    if start_day+days > len(prices):
        raise ValueError("Okres, który chcesz sprawdzić wykracza poza zakres danych!")

    balance_history = []
    balance = 0
    stock_shares = stock_shares_
    for day in range(start_day, start_day+days):
        if day == 0:
            macd_prev = macd[day]
            signal_prev = signal[day]
        else:
            macd_prev = macd[day - 1]
            signal_prev = signal[day - 1]

        macd_now = macd[day]
        signal_now = signal[day]
        stock_price = prices[day]

        if balance > 0 and macd_prev < signal_prev and macd_now > signal_now:
            stock_shares += (balance/stock_price)
            balance = 0

        if stock_shares > 0 and macd_prev > signal_prev and macd_now < signal_now:
            balance += stock_shares*stock_price
            stock_shares = 0

        balance_history.append(balance + stock_shares*stock_price)

    return balance_history
