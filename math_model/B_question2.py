import math

PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3


def depth(i):
    return 70 - i * math.tan(alpha)


def get_gamma(beta):
    return math.atan(math.tan(alpha) * math.sin(beta))

angle = [0, PI / 4, PI / 2, 3 * PI / 4, PI, 5 * PI / 4, 3 * PI / 2, 7 * PI / 4]
distance = [0.3 * 1852, 0.6 * 1852, 0.9 * 1852, 1.2 * 1852, 1.5 * 1852, 1.8 * 1852, 2.1 * 1852]
for beta in angle:
    print('\n',beta,':',end='\t')
    for i in distance:
        gamma = get_gamma(beta)
        d = 110 + math.tan(gamma) * i
        w1 = d * math.sin(theta / 2) * 1 / math.cos(theta / 2 + gamma)
        w2 = d * math.sin(theta / 2) * 1 / math.cos(theta / 2 - gamma)
        w = w1 + w2
        # print(w1, w2)
        print(w,end='\t')