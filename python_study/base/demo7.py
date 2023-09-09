# Author hugo
# Time 2023/6/30 16:52
# 列表

# 变量可以存储一个元素，而列表可以存储N多个元素，程序可以方便地对这些数据进行整体操作
# 列表相当于其他语言的数组

lst = ['hello', 'world', 98]
print(id(lst))
print(type(lst))
print(lst)
print(lst[0], lst[-3])
# 列表的创建方式
'''
使用中括号[]
调用内置函数list()
'''
lst1 = ['hello', 'world', 98]
lst2 = list(['hello', 'world', 98])
# 　列表的特点
'''
列表元素按顺序有序排序
索引映射唯一一个数据
列表可以储存重复数据
任意数据类型混存
根据需要动态分配和回收内存
'''
# 列表的查询操作
'''
获取列表中指定元素的索引
index()
    如查列表中存在N个相同的元素，只返回相同元素中的第一个元素的索引
    如果查询的元素在列表中不存在，则会抛出ValueError
    还可以在指定的start和stop之间进行查找
获取列表中的单个元素
正向索引从0到N-1,
逆向索引从-N到-1
指定索引不存在，抛出ValueError
'''
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))
print(lst.index('hello', 1, 4))

lst = ['hello', 'world', 98, 'hello', 'world', 2344]
print(lst[2])

# 获取列表中的多个元素
'''
切片
语法格式
    列表名[start : stop : step]
切片的结果是原列表片段的拷贝
切片的范围是[start,stop)
step默认为1，简写为[start : stop]
step为正数
    [:stop:step]，切片的第一个元素默认是列表的第一个元素
    [start::step]，切片的最后一个元素默认是列表的最后一个元素
    从start开始往后计算切片
step为负数
    [:stop:step]，切片的第一个元素默认是列表的最后一个元素
    [start::step]，切片的最后一个元素默认是列表的第一个元素
    从stop开始往前计算切片
'''
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print('原列表', id(lst))
lst2 = lst[1:6:1]
print('切的片段', id(lst2))
print(lst[1:6])
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])
print(lst[::-1])
print(lst[7::-1])
print(lst[6::-2])

# 判断指定元素在列表中是否存在
'''
元素 in 列表名
元素 not in 列表名
列表元素的遍历
for 迭代变量 in 列表名d:
    # do something
'''
for item in lst:
    print(item)

# 列表元素的增加操作
'''
append()    在列表的末尾添加一个元素
extend()    在列表的末尾至少添加一个元素
insert()    在列表的任意位置添加一个元素
切片         在列表的任意位置添加至少一个元素
'''
lst = [10, 20, 30]
print('添加元素之前', id(lst), lst)
lst.append(100)
print('添加元素之后', id(lst), lst)
lst2 = ['hello', 'world']
lst.append(lst2)
print(lst)
lst.extend(lst2)
print(lst)
lst.insert(1, 90)
print(lst)
lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)

# 列表元素的删除操作
'''
remove()
    依次删除一个元素
    重复元素只删除第一个
    元素不存在抛出ValueError
pop()
    删除指定索引位置上的元素
    删除索引不存在抛出IndexError
    不指定索引，删除列表中最后一个元素
切片
    会产生一个新的列表对象
    一次至少删除一个元素
clear()
    清空列表
del
    删除列表
'''
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)
print(lst)
lst.pop(1)
print(lst)
lst.pop()
print(lst)
new_lst = lst[1:3]
print(id(lst), '原列表', lst)
print(id(new_lst), '切片后的列表', new_lst)

'''
不产生新的列表对象，而是删除原列表的内容
'''
lst[1:3] = []
print(lst)

lst.clear()
print(lst)

del lst
# name 'lst' is not defined
# print(lst)

# 列表元素的修改操作
'''
为指定索引的元素赋予一个新值
为指定的切片赋予一个新值
'''
lst = [10, 20, 30, 40]
lst[2] = 100
print(lst)
lst[1:3] = [300, 400, 500, 600]
print(lst)

# 列表元素的排序操作
'''
调用sort()方法，列表中所有的元素默认按照从小到大的顺序进行排序，
可以指定reverse = true 来进行降序排序

调用内置函数sorted()，可以指定reverse = True ，进行降序排序，原列表不发生改变
'''
lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, end='\t')
print(id(lst))
lst.sort()
print('排序后的列表', lst, end='\t')
print(id(lst))
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)

lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, end='\t')
print(id(lst))
new_lst = sorted(lst)
print('排序后的列表', new_lst, end='\t')
print(id(new_lst))
desc_lst = sorted(lst, reverse=True)
print(desc_lst)

# 列表生成式
'''
[i * i for i in range(1, 10)]
i * i 表示列表元素的表达式
i 自定义变量
range(1,10) 可迭代变量
表示列表元素的表达式中通常包含自定义变量
'''
lst = [i * i * i * i * i for i in range(1, 10)]
print(lst)
