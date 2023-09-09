import math

PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3
haili = 1852

x = -2 * haili
length = 0
times = 0
w, w1, w2 = 0, 0, 0
w_before, w1_before, w2_before = 0, 0, 0
while x + w2 <= 0.5*haili:
    d = 110 - math.tan(alpha) * x
    D = d / math.cos(alpha)
    w1 = D * math.sin(theta / 2) * 1 / math.cos(theta / 2 + alpha)
    w2 = D * math.sin(theta / 2) * 1 / math.cos(theta / 2 - alpha)
    w = w1 + w2
    x += w * 0.8

    if w2_before:
        eta = 1 - w_before * 0.8 / (w2 + w1)
    else:
        eta = 0

    w1_before, w2_before = w1, w2
    w_before = w
    print(eta)
    times += 1
    length += 2 * haili
print(length, times)
