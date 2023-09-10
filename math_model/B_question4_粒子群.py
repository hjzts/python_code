# 导入模块
import random
import numpy as np
import pandas as pd
# 引入附件文件
excel_file = "附件.xlsx"
df = pd.read_excel(excel_file, sheet_name="Sheet1")

# 对附件文件信息分析
for i in range(1,252):
    for j in range(2,202):
        pass
        # print(df.iloc[i,j],end='\t')
    # print('\n')

# 参数设置
num_particles = 30
max_iterations = 100
sea_area_width = 4.0
coverage_width = 0.5
overlap_rate_min = 0.1
overlap_rate_max = 0.2

num_lines = 10000
# 定义目标函数
def objective_function(solution):
    # 计算目标函数值，可以是总测线长度、漏测海区百分比和重叠率超过20%部分的总长度的组合
    total_length = np.sum(solution)
    # 其他目标函数计算...
    return total_length


# 初始化粒子群
particles = []
for _ in range(num_particles):
    particle = np.random.uniform(0, sea_area_width, size=num_lines)  # 随机初始化测线设计
    velocity = np.random.uniform(-0.1, 0.1, size=num_lines)  # 随机初始化速度
    best_position = np.copy(particle)  # 初始化粒子的历史最佳位置
    particles.append({
        'position': particle,
        'velocity': velocity,
        'best_position': best_position,
        'best_fitness': objective_function(best_position)
    })

# 初始化全局最佳解
global_best_solution = particles[0]['best_position']
global_best_fitness = particles[0]['best_fitness']

# 开始PSO迭代
for iteration in range(max_iterations):
    for particle in particles:
        # 更新速度和位置
        inertia_weight = 0.7
        cognitive_weight = 1.5
        social_weight = 1.5
        random1 = np.random.rand(len(particle['position']))
        random2 = np.random.rand(len(particle['position']))
        particle['velocity'] = (inertia_weight * particle['velocity'] +
                                cognitive_weight * random1 * (particle['best_position'] - particle['position']) +
                                social_weight * random2 * (global_best_solution - particle['position']))
        particle['position'] += particle['velocity']

        # 限制测线位置在合法范围内
        particle['position'] = np.clip(particle['position'], 0, sea_area_width)

        # 计算适应度
        fitness = objective_function(particle['position'])

        # 更新历史最佳位置和全局最佳位置
        if fitness < particle['best_fitness']:
            particle['best_position'] = np.copy(particle['position'])
            particle['best_fitness'] = fitness

        if fitness < global_best_fitness:
            global_best_solution = np.copy(particle['position'])
            global_best_fitness = fitness

# 输出结果
print("PSO算法完成！")
print("最佳测线设计：", global_best_solution)
print("最佳目标函数值：", global_best_fitness)
