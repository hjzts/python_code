# Author hugo
# Time 2023/6/28 11:21
# 内置函数range()
'''
用于生成一个整数序列
创建range对象的三种方式
range(stop) 创建一个[0,stop)的整数序列，步长为1
range(start,stop) 创建一个[start,stop)的整数序列，步长为1
range(start,stop，step) 创建一个[start,stop)的整数序列，步长为step
'''
r = range(10)
print(r)  # range(0, 10)
print(list(r))  # 用于查看range序列对象中的整数序列  --list是列表的意思

r = range(1, 10)
print(r)
print(list(r))

r = range(1, 10, 2)
print(r)
print(list(r))

'''判断指定的整数在序列中是否存在使用 in , not in'''
print(10 in r)
print(9 in r)

print(10 not in r)
print(9 not in r)
'''
range 类型的优点：
不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的
因为近几年需要存储start stop step
只有当用到range对象时，才会去计算序列中的相关元素
'''

# 循环结构
a = 1
# 判断条件表达式
if a < 10:
    # 执行条件执行体
    print(a)
    a += 1

a = 1
while a < 10:
    print(a)
    a += 1
'''
while 循环的执行程序
四步循环法
    初始化变量
    条件判断
    条件执行体（循环体）
    改变变量
'''

# 计算0-4之间的累加和
a = 0
sum = 0
while a <= 4:
    sum += a
    a += 1
print(sum)

# 计算1到100之间的偶数和
a = 2
sum = 0
while a <= 100:
    sum += a
    a += 2
print('1到100之间的偶数和为:', sum)

sum = 0
for item in range(1, 101):
    if item % 2 == 0:
        sum += item
print(sum)
# for-in循环
'''
in表示从字符串序列等中依次取值，又称为遍历
for-in遍历的对象必须是可迭代对象
for 自定义的变量 in 可迭代对象:
    循环体
循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
'''
for item in 'python':
    print(item)

# range() 产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)

for _ in range(5):
    print('python 好啊!')

# 输出100到999之间的水仙花书
for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print(item)

# 流程控制语句break
'''
从键盘录入密码，最多录入三次，如果不正确就结束循环
'''
# for item in range(3):
a = 0
while a < 3:

    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确，还剩余', 2 - a, '次机会')
        # print('密码不正确，还剩余', 2 - item, '次机会')
    a += 1

'''
输出1-50之间所有5的倍数
'''
for i in range(1, 51):
    if i % 5:
        continue
    print(i)

# else 语句
'''
while和for没有碰到break那么就执行else
也就是循环正常结束执行else
'''
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确，还剩余', 2 - item, '次机会')

else:
    print('对不起，三次密码均输入错误')

# 　嵌套循环
'''
输出一个三行四列的矩阵
'''
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')  # 不换行输出
    print()  # 换行

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', i * j, end='\t')
    print()

# 二重循环中的break和continue放在内层循环只控制内层循环
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()
