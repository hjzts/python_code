# 导入
import math

# 定义常量
PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3

# 根据航迹角beta得到等价的坡度角gamma
def get_gamma(beta):
    return math.atan(math.tan(alpha) * math.sin(beta))

# 求出在距离中心出d，航迹角度为beta的情况下，多波束测线的覆盖范围
def get_w(d, beta):
    gamma = get_gamma(beta)
    w1 = d * math.sin(theta / 2) * 1 / math.cos(theta / 2 + gamma)
    w2 = d * math.sin(theta / 2) * 1 / math.cos(theta / 2 - gamma)
    w = w1 + w2
    return w

# 求出不同航迹角对应的总航迹长
def getline(beta):
    gamma = get_gamma(beta)
    w = get_w(110 + math.tan(alpha) * 1852 * math.sqrt(5), gamma)
    newline = math.ceil(
        math.cos(math.atan(2) - beta + PI / 2) * 2 * math.sqrt(5) * 1852 / w / 0.85 / math.cos(gamma)) * (
                      4 * 1852 / math.sin(beta))
    return newline

# 定义变量的初始值，需要将min_line的初始值设置的足够大
beta = PI / 2
min_line = 10000 * 1852
min_beta = 0
# 循环遍历beta不同值的情况，求出最小的航迹长度
while beta <= PI:
    newline = getline(beta)
    if newline < min_line:
        min_line = newline
        min_beta = beta
    beta += PI / 1000
# 打印输出结果，以及对应的角度beta
print(min_line, min_beta)
# 发现min_beta的结果总为PI/2
