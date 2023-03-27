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


def histogram(macd_series, signal_series, n):
    histogram = []
    for i in range(n):
        histogram.append(macd_series[i] - signal_series[i])
    return histogram


def plot_macd_signal(x_val, macd_series, signal_series):
    plt.plot(x_val, macd_series, color='b', label='MACD')
    plt.plot(x_val, signal_series, color='r', label='SIGNAL')

    plt.xlabel("Próbka")
    plt.ylabel("Wartość")
    plt.title("Metody Numeryczne - MACD i SIGNAL")

    plt.legend()
    plt.show()


def plot_wig20(x_val, wig_samples):
    plt.plot(x_val, wig_samples, color='g', label='WIG20')

    plt.xlabel("Próbka")
    plt.ylabel("Wartość")
    plt.title("Metody Numeryczne - WIG20")

    plt.legend()
    plt.show()


def plot_histogram(x_val, histogram):
    plt.bar(x_val, histogram)

    plt.xlabel("Próbka")
    plt.ylabel("Histogram")
    plt.title("Metody Numeryczne - histogram")
    plt.show()


def count_final_fund(starting_fund, epsilon, hist, samples):
    for i in range(n - 1):
        if -epsilon <= hist[i] <= epsilon:
            if hist[i + 1] > epsilon:
                starting_fund -= samples[i]
            elif hist[i + 1] < -epsilon:
                starting_fund += samples[i]
    return starting_fund


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

plot_macd_signal(x_val, macd_series, signal_series)
plot_wig20(x_val, samples)

hist = histogram(macd_series, signal_series, n)
plot_histogram(x_val, hist)

epsilon = 2
starting_found = 1000

final_found = count_final_fund(starting_found, epsilon, hist, samples)
