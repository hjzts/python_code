# Author hugo
# Time 2023/6/27 23:55
# 顺序结构
# 对象的bool值

'''
python 一切皆对象，所有对象都有一个bool值
以下对象的bool值为False：
False 数值0 None  空字符串 空列表 空元组 空字典 空集合
'''
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))  # 表示一个空列表
print(bool(list()))  # 表示一个空列表
print(bool(()))  # 表示一个空元组
print(bool(tuple()))  # 表示一个空元组
print(bool({}))  # 表示一个空字典
print(bool(dict()))  # 表示一个空字典
print(bool(set()))  # 表示一个空集合
print('-------------------除了这些其他对象的bool值均为True------------')

# 判断结构
# 　单分支结构
money = 1000
s = int(input('请输入取款金额'))
# 判断余额是否充足
if money >= s:
    money = money - s
    print('取款成功，余额为：', money)

# 双分支结构
'''
从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数
'''
num = int(input('请输入一个整数'))

# 条件判断
if num % 2 == 0:
    print(num, '偶数')
else:
    print(num, '奇数')

# 多分支结构
# 多选一执行，最后一个else可以没有
'''
从键盘录入一个整数作为成绩，判断成绩对应的等级
'''
score = int(input('请输入一个成绩：'))
# 判断
# if score >= 90 and score <= 100 :
if 90 <= score <= 100:  # python特色
    print('A级')
# elif score >= 80 and score < 90:
elif 80 <= score < 90:
    print('B级')
# elif score >= 70 and score < 80:
elif 70 <= score < 80:
    print('C级')
# elif score >= 60 and score < 70:
elif 60 <= score < 70:
    print('D级')
# elif score >= 0 and score < 60:
elif 0 <= score < 60:
    print('E级')
else:
    print('对不起，键入成绩有误，不在成绩的有效范围')

# 嵌套if

ans = input('您是会员名？y/n')
money = float(input('请输入您的购物金额：'))
if ans == 'y':
    print('会员')
    if money >= 200:
        print('打8折，付款金额为：', money * 0.8)
    elif money >= 100:
        print('打9折，付款金额为：', money * 0.9)
    else:
        print('不打折，付款金额为：', money)
else:
    print('非会员')
    if money >= 200:
        print('打9.5折，付款金额为：', money * 0.95)
    else:
        print('不打折，付款金额为：', money)

# 条件表达式
# 为if else的简写
'''
从键盘录入两个整数，比较两个整数的大小
'''
num_a = int(input('请输入第一个整数'))
num_b = int(input('请输入第二个整数'))
# 比较大小
if num_a >= num_b:
    print(num_a, '大于等于', num_b)
else:
    print(num_a, '小于', num_b)

print('使用条件表达式进行比较')
print(str(num_a) + '大于等于' + str(num_b) if num_a >= num_b else str(num_a) + '小于' + str(num_b))

# pass语句
# 语句什么都不做，只是一个占位符，用在语法上需要语句的地方
ans = input('您是会员名？y/n')
money = float(input('请输入您的购物金额：'))
if ans == 'y':
    pass
else:
    pass