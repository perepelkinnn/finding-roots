import math


epsilon = 0.5e-05

a = 0
b = 1

x = [None] * 100
x[1] = a


def f(x):
    return 1.4 * math.cos(x) - math.exp(x)


def df(x):
    return - 1.4 * math.sin(x) - math.exp(x)


def ddf(x):
    return - 1.4 * math.cos(x) - math.exp(x)


M = abs(ddf(1))


n = 1

while (abs(f(x[n])) >= epsilon):
    delta = (-df(x[n]) - math.sqrt(df(x[n]) ** 2 + 2 * M * f(x[n]))) / (-M)
    x[n + 1] = x[n] + delta
    n += 1


print("n={}".format(n))
print("x≈{}".format(x[n]))
