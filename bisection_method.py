import math


epsilon = 0.5e-05

a = 0
b = 1

a_0 = a
b_0 = b
x_0 = (a_0 + b_0) / 2


def f(x):
    return 1.4 * math.cos(x) - math.exp(x)


n = 1

while (n <= math.log2((b - a) / epsilon)):
    if (f(a_0) * f(x_0) < 0):
        b_0 = x_0
    else:
        a_0 = x_0
    x_0 = (a_0 + b_0) / 2
    n += 1

print("n={}".format(n))
print("x≈{}".format(x_0))
