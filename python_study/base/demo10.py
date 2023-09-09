# Author hugo
# Time 2023/7/4 14:08

# 集合
'''
Python 语言提供的内置数据结构
与列表、字典一样都属于可变类型的序列
集合是没有value的字典
'''
s = {'Python', 'hello', 90}
print(s)
# 集合的创建方式
'''
直接{}
使用内置函数set()
'''
s = set(range(6))
print(s, type(s))
print(set([3, 4, 53, 56]))  # 列表转集合
print(set((3, 4, 43, 435)))  # 元组转集合
print(set('Python'))  # 字符串序列转集合
print(set({124, 3, 4, 4, 5}))  # 集合转集合
# 空集合
# 不能直接s = {}这样会显示是dict
print(set())

s = {2, 3, 4, 5, 5, 6, 7, 7}  # 集合中的元素不允许重复
print(s)

# 集合的相关操作
'''
集合元素的判断操作
    in 或not in
集合元素的新增操作
    调用add()方法，一次添加一个元素
    调用update()方法，至少添加一个元素
集合元素的删除操作
    调用remove()方法，一次删除一个指定元素，如果指定元素不存在抛出KeyError
    调用discard()方法，一次删除一个指定元素，如果指定元素不存在不抛出异常
    调用pop()方法，一次只删除一个任意元素
    调用clear()方法，清空集合
'''
s = {10, 20, 30, 405, 60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

s.add(80)
print(s)
s.update({200, 300, 400})
print(s)
s.update([100, 99, 8])
s.update((78, 64, 56))
print(s)

s.remove(100)
print(s)
# s.remove(500)
s.discard(300)
s.discard(500)
print(s)
s.pop()
print(s)
s.pop()  # 不能添加参数
print(s)
s.clear()
print(s)

# 集合之间的关系
'''
两个集合是否相等
    元素相同则相等
    可以使用运算符==或!=进行判断
一个集合是否是另一个集合的子集
    可以调用方法issubset进行判断
一个子集是否是另一个集合的超集
    可以调用issuperset进行判断
两个集合是否没有交集
    可以调用方法isdisjoint进行判断
'''
s = {10, 20, 30, 40}
s2 = {30, 40, 20, 10, 10, 10}
print(s == s2)
print(s != s2)

s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))
print(s3.issubset(s1))

print(s1.issuperset(s2))
print(s1.issuperset(s3))

print(s2.isdisjoint(s3))
s4 = {50, 60}
print(s2.isdisjoint(s4))

# 集合的数学操作
'''
交集
'''
s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
'''
intersection()与&等价，交集操作
'''
print(s1.intersection(s2))
print(s1 & s2)
'''
union与|等价，并集操作
'''
print(s1.union(s2))
print(s1 | s2)
'''
差集操作
'''
print(s1.difference(s2))
'''
对称差集
'''
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

print(s1)
print(s2)

# 集合生成式
'''
用于生成集合的公式
    {i*i for i in range(1,10)}
    表示集合元素的表达式 i*i
    自定义变量   i
    可迭代对象   range(1,10)
将{}修改为[]就是列表生成式
没有元组生成式
'''
lst = [i*i for i in range(6)]
print(lst)

s = {i * i for i in range(10)}
print(s)

