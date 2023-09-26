import myRandom
import math
import numpy as np

# 参数设置
sea_area_width = 4.0  # 海域宽度（假设为4海里）
coverage_width = 0.5  # 测线覆盖宽度（假设为0.5海里）
overlap_rate_min = 0.1  # 最小重叠率
overlap_rate_max = 0.2  # 最大重叠率
initial_temperature = 1000  # 初始温度
cooling_rate = 0.95  # 冷却率
iterations = 1000  # 迭代次数

# 生成初始解
num_lines = 10  # 假设生成10条测线
initial_solution = np.random.uniform(0, sea_area_width, num_lines)


# 定义适应度函数
def fitness(solution):
    total_length = np.sum(solution)
    overlap = coverage_width - (sea_area_width - total_length) % coverage_width
    overlap_rate = overlap / coverage_width
    if overlap_rate_min <= overlap_rate <= overlap_rate_max:
        return total_length
    else:
        return float('inf')


# 模拟退火算法
current_solution = initial_solution
current_fitness = fitness(current_solution)
best_solution = current_solution
best_fitness = current_fitness
current_temperature = initial_temperature

for _ in range(iterations):
    # 随机扰动当前解
    neighbor_solution = current_solution + np.random.uniform(-1, 1, num_lines)

    # 限制测线位置在合法范围内
    neighbor_solution = np.clip(neighbor_solution, 0, sea_area_width)

    # 计算适应度差异
    delta_fitness = fitness(neighbor_solution) - current_fitness

    # 根据Metropolis准则决定是否接受扰动
    if delta_fitness < 0 or random.random() < math.exp(-delta_fitness / current_temperature):
        current_solution = neighbor_solution
        current_fitness = delta_fitness

        # 更新最佳解
        if current_fitness < best_fitness:
            best_solution = current_solution
            best_fitness = current_fitness

    # 降低温度
    current_temperature *= cooling_rate

# 输出结果
print("模拟退火算法完成！")
print("最佳测线设计：", best_solution)
overlap = coverage_width - (sea_area_width - np.sum(best_solution)) % coverage_width
overlap_rate = overlap / coverage_width
print("最佳重叠率：", overlap_rate)
