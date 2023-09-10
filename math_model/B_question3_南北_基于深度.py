# 导入模块
import math

# 定义常量
PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3
nautical_mile = 1852


# 通过左侧h的值计算下一个x的值
def Next_x(h):
    x = h / (math.tan(alpha) + math.cos(theta / 2 + alpha) / (math.cos(alpha) * math.sin(theta / 2)))
    return x


# 通过计算得到最大深度和最小深度
h_max = 207.0
h_min = 13.0
eta = 0.9


# 主函数
def main():
    # 初始化变量
    h = h_max
    n = 0
    x = 0
    # 当深度大于最小深度时，继续循环
    while h - x * (1 - eta) * math.tan(alpha) > h_min:
        n += 1
        x = Next_x(h)
        x = x / math.cos(theta / 2 - alpha) * (math.cos(theta / 2 + alpha) + math.cos(theta / 2 - alpha))
        h = h - (x * eta * math.tan(alpha))
    # 答应输出结果
    print(n)
    print(n * nautical_mile * 2)


# 运行主函数
if __name__ == "__main__":
    main()
