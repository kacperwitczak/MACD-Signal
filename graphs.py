import matplotlib.pyplot as plt
import numpy as np


def show_macd_signal(start, data_length, company_name, macd, signal, date):
    if start+data_length > len(macd):
        raise ValueError("Okres, który chcesz sprawdzić wykracza poza zakres danych!")

    x = date[start:start + data_length]

    step = (start+data_length)//10
    x_ticks = x[::step]

    plt.figure(figsize=(15, 6))

    plt.plot(x, macd[start:start+data_length], label="MACD", color="blue", linewidth=0.7)
    plt.plot(x, signal[start:start+data_length], label="SIGNAL", color="red", linewidth=0.7)

    plt.xlabel("Dzień")
    plt.ylabel("Wartość")
    plt.title("MACD & SIGNAL " + company_name)
    plt.xticks(x_ticks, rotation=45)
    plt.legend()
    plt.show()


def show_company(start, data_length, title, date, price):
    if start+data_length > len(date):
        raise ValueError("Okres, który chcesz sprawdzić wykracza poza zakres danych!")

    x = date[start:start+data_length]

    step = (start+data_length)//10
    x_ticks = x[::step]

    plt.figure(figsize=(15, 6))

    plt.plot(x, price[start:start+data_length], label="WIG20", color="blue", linewidth=0.7)

    plt.xlabel("Dzień")
    plt.ylabel("Wartość [zł]")
    plt.title(title)
    plt.xticks(x_ticks, rotation=45)
    plt.legend()
    plt.show()

def show_balance(start, data_length, title, history, date):
    x = date[start:start + data_length]

    step = (start+data_length)//10
    x_ticks = x[::step]

    plt.figure(figsize=(15, 6))

    plt.plot(x, history, label="Wartość", color="blue", linewidth=0.7)

    plt.xlabel("Dzień")
    plt.ylabel("Wartość [zł]")
    plt.title(title)
    plt.xticks(x_ticks, rotation=45)
    plt.legend()
    plt.show()