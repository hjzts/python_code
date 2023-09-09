import math

PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3

w1_before, w2_before = 0, 0
distances = [-800, -600, -400, -200, 0, 200, 400, 600, 800]
for x in distances:
    d = 70 - math.tan(alpha) * x
    D = d / math.cos(alpha)
    w1 = D * math.sin(theta/2) * 1 / math.cos(theta / 2 + alpha)
    w2 = D * math.sin(theta/2) * 1 / math.cos(theta / 2 - alpha)
    w = w1 + w2
    print(w1,w2)
    if w2_before:
        eta = 1 - 200 / (w2 + w1)
    else:
        eta = 0
    w1_before, w2_before = w1, w2
    print(D, w, '\n',eta)
    print('-------------------------')
