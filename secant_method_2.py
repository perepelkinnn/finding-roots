import math


epsilon = 0.5e-05

a = 0
b = 1

x = [None] * 100
x[0] = a
x[1] = b


def f(x):
    return 1.4 * math.cos(x) - math.exp(x)


n = 1

while (abs(f(x[n])) >= epsilon):
    x[n + 1] = x[n] - f(x[n]) / (f(x[n]) - f(x[n - 1])) * (x[n] - x[n - 1])
    n += 1


print("n={}".format(n))
print("x≈{}".format(x[n]))
