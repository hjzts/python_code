import math

PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3


def get_gamma(beta):
    return math.atan(math.tan(alpha) * math.sin(beta))


def get_w(d, beta):
    gamma = get_gamma(beta)
    w1 = d * math.sin(theta / 2) * 1 / math.cos(theta / 2 + gamma)
    w2 = d * math.sin(theta / 2) * 1 / math.cos(theta / 2 - gamma)
    w = w1 + w2
    return w


def getline(beta):
    gamma = get_gamma(beta)
    w = get_w(110 + math.tan(alpha) * 1852 * math.sqrt(5), gamma)
    newline = math.ceil(
        math.cos(math.atan(2) - beta + PI / 2) * 2 * math.sqrt(5) * 1852 / w / 0.85 / math.cos(gamma)) * (
                      4 * 1852 / math.sin(beta))
    return newline


beta = PI / 2
min_line = 10000 * 1852
min_beta = 0
while beta <= PI:
    newline = getline(beta)
    if newline < min_line:
        min_line = newline
        min_beta = beta
    beta += PI / 1000
print(min_line, min_beta)
