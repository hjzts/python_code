import math
import pandas as pd

excel_file = "result2.xlsx"
result_df = pd.DataFrame(columns=["i", "j", "ans"])

PI = math.pi
alpha = 1.5 * PI / 180
theta = 2 * PI / 3

def get_gamma(beta):
    return math.atan(math.tan(alpha) * math.sin(beta))

angle = [0, PI / 4, PI / 2, 3 * PI / 4, PI, 5 * PI / 4, 3 * PI / 2, 7 * PI / 4]
distance = [0.3 * 1852, 0.6 * 1852, 0.9 * 1852, 1.2 * 1852, 1.5 * 1852, 1.8 * 1852, 2.1 * 1852]

for beta in angle:
    k = angle.index(beta) + 1  # 获取 beta 的索引并加1以作为 "i" 的值
    for i in distance:
        gamma = get_gamma(beta)
        d = 110 + math.tan(gamma) * i
        D = d / math.cos(gamma)
        w1 = D * math.sin(theta / 2) * 1 / math.cos(theta / 2 + gamma)
        w2 = D * math.sin(theta / 2) * 1 / math.cos(theta / 2 - gamma)
        w = w1 + w2
        result_df = result_df.append({"i": k, "j": distance.index(i) + 1, "ans": w})

result_df.to_excel(excel_file, index=False)
