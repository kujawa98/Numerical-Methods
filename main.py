import pandas as pd
from matplotlib import pyplot as plt


def EMA(period, samples, current_sample):
    alpha = 2 / (period + 1)
    base = 1 - alpha
    numerator = 0
    denominator = 0

    for i in range(period):
        if current_sample - i >= 0:
            x = base ** i
            denominator += x
            x *= samples[current_sample - i]
            numerator += x
    return numerator / denominator


def MACD(samples, current_sample):
    EMA_12 = EMA(12, samples, current_sample)
    EMA_26 = EMA(26, samples, current_sample)
    return EMA_12 - EMA_26


def SIGNAL(macd_series, index):
    return EMA(9, macd_series, index)


n = 1000

df = pd.read_csv('wig20_d.csv')

samples = df['Zamkniecie'].values[:n]

macd_series = [0 for i in range(n)]

signal_series = [0 for i in range(n)]

for i in range(n):
    macd_series[i] = MACD(samples, i)

for i in range(n):
    signal_series[i] = SIGNAL(macd_series, i)

x_val = [i for i in range(n)]
y_val = macd_series

plt.plot(x_val, macd_series, color='b', label='MACD')
plt.plot(x_val, signal_series, color='r', label='SIGNAL')

plt.xlabel("Dzień")
plt.ylabel("Wartość")
plt.title("Metody Numeryczne - MACD i SIGNAL")

plt.legend()
plt.show()
