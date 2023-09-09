# Author hugo
# Time 2023/7/4 9:26

# 元组
'''
python内置的数据结构之一，是一个不可变序列
不可变序列与可变序列
    不可变序列：字符串，元组
        没有增删改的操作
    可变序列：列表，字典
        可以对序列执行增删改操作，对象地址不发生更改
'''
lst = [10, 20, 45]
print(id(lst))
lst.append(300)
print(id(lst))

s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))

'''
元组
    小括号(元素对象,元素对象)
'''
# 元组的创建方式
'''
直接小括号
    t = ('Python','hello',90)
使用内置函数tuple()
    t = tuple(('Python','hello',90))
只包含一个元组的元素需要使用小括号和逗号
    t = (10,)
'''
t = ('Python', 'hello', 90)
print(t)
print(type(t))
t2 = 'Python', 'hello', 90
print(t2)
print(type(t2))
t = tuple(('Python', 'hello', 90))
print(t)
print(type(t))
t = (10,)
print(t)

# 空元组的创建方式
lst = []
lst1 = list()

d = {}
d1 = dict()

t = ()
t1 = tuple()

print('空列表', lst, lst1)
print('空字典', d, d1)
print('空元组', t, t1)

# 为什么要将元组设计成不可变序列
'''
在多任务环境下，同时操作对象时不需要加锁
因此在程序中尽量使用不可变序列

注意： 
    元组中存储的是对象的引用
    如果元组中的对象本身是不可变对象，则不能再引用其他对象
    如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
'''
t = (10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

# t[1] = 100    元组不允许修改元素
t[1].append(100)
print(t)
print(t[1],type(t[1]),id(t[1]))

# 元组的遍历
'''
第一种获取元组的方式，使用索引
元组是可迭代对象，可以使用for in 进行遍历
for item in t:
    print(item)
'''
t = 'Python','world',98
for item in t:
    print(item)
