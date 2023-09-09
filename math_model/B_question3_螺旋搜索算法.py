import math

# 参数设置
sea_area_width = 4  # 海域宽度（假设为4海里）
sea_area_length = 2  # 海域长度（假设为2海里）
coverage_width = 0.5  # 测线覆盖宽度（假设为0.5海里）
overlap_rate_min = 0.1  # 最小重叠率
overlap_rate_max = 0.2  # 最大重叠率

# 初始位置
x = 0.0
y = 0.0

# 初始方向（假设向东）
direction_x = 1.0
direction_y = 0.0

# 存储测线的列表
measurement_lines = []

while y <= sea_area_length:
    # 计算当前测线的起点和终点坐标
    start_x = x - (coverage_width / 2)
    end_x = x + (coverage_width / 2)
    start_y = y
    end_y = y

    # 将测线添加到列表中
    measurement_lines.append((start_x, start_y, end_x, end_y))

    # 更新下一条测线的起点坐标
    x += coverage_width * direction_x

    # 判断是否需要改变方向
    if x > sea_area_width / 2 or x < -sea_area_width / 2:
        direction_x *= -1
        y += coverage_width * direction_y

# 计算重叠率
overlap_rate = (coverage_width - (sea_area_width % coverage_width)) / coverage_width

# 输出结果
print("测线设计完成！")
print("测线总数：", len(measurement_lines))
print("重叠率：", overlap_rate)

# 输出测线坐标
for i, line in enumerate(measurement_lines):
    print(f"测线{i + 1}: 起点({line[0]:.2f}, {line[1]:.2f}), 终点({line[2]:.2f}, {line[3]:.2f})")
