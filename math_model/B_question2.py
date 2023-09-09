# 导入模块
import math
import pandas as pd

# 为了将得到的结果输出到excel表格中，引入excel_file变量
excel_file = "result2.xlsx"
result_df = pd.DataFrame(columns=["i", "j", "ans"])

# 定义常量
PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3


# 用于方便计算gamma，也就是不同beta角度下的等价的坡角
def get_gamma(beta):
    return math.atan(math.tan(alpha) * math.sin(beta))


# 定义角度列表和距离海域中心处的距离列表
angle = [0, PI / 4, PI / 2, 3 * PI / 4, PI, 5 * PI / 4, 3 * PI / 2, 7 * PI / 4]
distance = [0.3 * 1852, 0.6 * 1852, 0.9 * 1852, 1.2 * 1852, 1.5 * 1852, 1.8 * 1852, 2.1 * 1852]

# 利用双重循环计算并得到结果，同时将结果保存到result_df中，并将结果打印出来
for beta in angle:
    k = angle.index(beta) + 1  # 获取 beta 的索引并加1以作为 "i" 的值
    for i in distance:
        # 修正坡度角为gamma
        gamma = get_gamma(beta)
        d = 110 + math.tan(gamma) * i
        D = d / math.cos(gamma)

        w1 = D * math.sin(theta / 2) * 1 / math.cos(theta / 2 + gamma)
        w2 = D * math.sin(theta / 2) * 1 / math.cos(theta / 2 - gamma)
        w = w1 + w2

        # 格式化打印输出
        print({"{:10.6f}".format(w)}, end='\t')
        result_df = result_df.append({"i": k, "j": distance.index(i) + 1, "ans": w}, ignore_index=True)
    print()
# 使用 pivot 方法将数据重新排列为适合的形式
pivot_table = result_df.pivot(index="i", columns="j", values="ans")

# 将生成的表格保存到 Excel 文件
pivot_table.to_excel(excel_file)

print(f"表格已生成并保存到 {excel_file}")
