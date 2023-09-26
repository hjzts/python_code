# Author hugo
# Time 2023/9/7 22:19
import math
import myRandom


# 定义要优化的目标函数
def objective_function(x):
    return (x - 2) * (x + 5) * (x + 8) * (x - 6)


# 模拟退火算法
def simulated_annealing(obj_func, x_range, initial_temperature, cooling_rate, max_iterations):
    current_solution = random.uniform(x_range[0], x_range[1])
    best_solution = current_solution
    current_energy = obj_func(current_solution)
    best_energy = current_energy

    for i in range(max_iterations):
        # 随机生成一个新的解
        candidate_solution = current_solution + random.uniform(-0.5, 0.5)

        # 确保新解在取值范围内
        candidate_solution = max(x_range[0], min(x_range[1], candidate_solution))

        # 计算新解的能量
        candidate_energy = obj_func(candidate_solution)

        # 计算能量差
        energy_difference = candidate_energy - current_energy

        # 如果新解更优或者按照一定概率接受劣解，则更新当前解
        if energy_difference < 0 or random.random() < math.exp(-energy_difference / initial_temperature):
            current_solution = candidate_solution
            current_energy = candidate_energy

            # 如果当前解更优，则更新最优解
            if current_energy < best_energy:
                best_solution = current_solution
                best_energy = current_energy

        # 降低温度
        initial_temperature *= cooling_rate

    return best_solution, best_energy


# 设置参数并运行模拟退火算法
x_range = (-10, 10)
initial_temperature = 1000
cooling_rate = 0.95
max_iterations = 10000

best_solution, best_energy = simulated_annealing(objective_function, x_range, initial_temperature, cooling_rate,
                                                 max_iterations)
print(f"最优解: x = {best_solution}, 最小值: {best_energy}")
