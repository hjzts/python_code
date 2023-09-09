import math

PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3


def depth(i):
    return 70 - i * math.tan(alpha)


def get_gamma(beta):
    return math.atan(math.tan(alpha) * math.sin(beta))


beta = 0
while beta <= 7 * PI / 4:
    i = 0
    while i <= 2.1 * 1852:
        gamma = get_gamma(beta)
        d = 110 + math.tan(gamma) * i
        w1 = d * math.sin(theta / 2) * 1 / math.cos(theta / 2 + gamma)
        w2 = d * math.sin(theta / 2) * 1 / math.cos(theta / 2 - gamma)
        w = w1 + w2
        print(w1, w2)
        print(w)
        print('-----------------')
        i = i + 0.3 * 1852
    beta = beta + PI / 4