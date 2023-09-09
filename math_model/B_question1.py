import math

# 定义相关常量
PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3

# 定义变量
w1, w2 = 0, 0
w1_before, w2_before = 0, 0

# 定义距离列表, 单位: 米，为测线距离中心点的距离
distances = [-800, -600, -400, -200, 0, 200, 400, 600, 800]

# 利用for循环，计算并输出结果
for x in distances:
    d = 70 - math.tan(alpha) * x
    D = d / math.cos(alpha)
    w1 = D * math.sin(theta / 2) * 1 / math.cos(theta / 2 + alpha)
    w2 = D * math.sin(theta / 2) * 1 / math.cos(theta / 2 - alpha)
    w = w1 + w2

    # eta为间距除以当前x位置的覆盖范围
    # 若eta为负，则表示漏测
    if w2_before:
        eta = 1 - (200/math.cos(alpha)) / (w2 + w1)
    else:
        eta = 0
    w1_before, w2_before = w1, w2
    print("{:15.6f}".format(D), "{:15.6f}".format(w), "{:15.6f}".format(eta))
