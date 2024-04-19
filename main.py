from helpers import *
from data import *
from algorithms import *
from graphs import *


if __name__ == '__main__':
    data_length, data_path, price_column, company_name, date_column = get_config()

    data = get_data(data_length, data_path)
    inspect_data(data)
    prices = data[price_column]
    date = data[date_column]

    macd = MACD(prices, 12, 26)
    signal = SIGNAL(macd, 9)

    start_day = 0
    n_next_days = 1000
    show_company(start_day, n_next_days, company_name, date, prices)
    show_macd_signal(start_day, n_next_days, company_name, macd, signal, date)
    history = trading_algorithm(1000,start_day, n_next_days, prices, macd, signal)
    show_balance(start_day, n_next_days, "Wartość portfela", history, date)

    start_day = 300
    n_next_days = 100
    show_company(start_day, n_next_days, company_name, date, prices)
    show_macd_signal(start_day, n_next_days, company_name, macd, signal, date)
    history = trading_algorithm(1000,start_day, n_next_days, prices, macd, signal)
    show_balance(start_day, n_next_days, "Wartość portfela", history, date)

    start_day = 850
    n_next_days = 100
    show_company(start_day, n_next_days, company_name, date, prices)
    show_macd_signal(start_day, n_next_days, company_name, macd, signal, date)
    history = trading_algorithm(1000,start_day, n_next_days, prices, macd, signal)
    show_balance(start_day, n_next_days, "Wartość portfela", history, date)



