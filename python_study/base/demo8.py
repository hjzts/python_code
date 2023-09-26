# Author hugo
# Time 2023/7/3 17:35

# 字典
'''
python内置的数据结构之一，与列表一样是一个可变序列
以键值对的方式存储数据，字典是一个无序的序列
'''
scores = {'张三': 100, '李四': 98, '夏神': 150, '王五': 45}
'''
字典的实现原理和查字典类似
查字典式根据部首或拼音查找对应的页码，python中的字典式根据key查找value的位置
放在字典中的序列必须是一个不可变序列，也就是字典中的元素不能改变

字典的所有元素都是一个Key-value对
key不允许重复，value可以重复
字典中的元素是无序的
字典中的key必须是不可变对象     list不能作为key，list是一个可变对象
字典也可以根据需要动态地伸缩
字典会浪费较大的内存，是一种使用空间换时间的数据结构
'''
# 字典的创建
'''
最常用的方式：使用方括号{}
使用内置函数dict()
'''
scores = {'张三': 100, '李四': 98, '夏神': 150, '王五': 45}
print(scores)
print(type(scores))
student = dict(name='jack', age=20)
# student = dict('jack',20)
print(student)
# 空字典
d = {}

# 字典元素的获取
'''
[]      eg scores['张三'] 
get()方法     scores.get('张三') 
区别:
    []如果字典不存在指定的key，则抛出keyError异常
    get()方法取值，如果字典不存在指定的key，并不会抛出keyError而是返回None，
    可以通过参数设置默认的value，以便指定的key不存在时返回
'''
scores = {'张三': 100, '李四': 98, '夏神': 150, '王五': 45}
print(scores['张三'])
print(scores.get('张三'))
print(scores.get('陈六'))
print(scores.get('麻七', 99))
# key的判断
''' 
in 指定的key在字典返回True  '张三'in scores
not in 指定的key在字典中不存在返回True  'Marry'not in scores
字典元素的删除     删除指定的key-value对，键值对
    del scores['张三']
字典元素的新增
    scores['Jack'] = 90
'''
scores = {'张三': 100, '李四': 98, '夏神': 150, '王五': 45}
print('张三' in scores)
print('张三' not in scores)
print(scores)
del scores['张三']
print(scores)
'''
清空字典的元素
'''
scores.clear()
print(scores)

scores = {'张三': 100, '李四': 98, '夏神': 150, '王五': 45}
scores['陈六'] = 98
print(scores)
# 修改元素
scores['陈六'] = 100
print(scores)

# 获取字典视图的三个方法
'''
key()       获取字典中所有的key
values()    获取字典的所有value
items()     获取字典中所有的key-value对
'''
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))   # 将所有key组成的视图转成列表

values = scores.values()
print(values)
print(type(values))
print(list(values))

items = scores.items()
print(items)
print(type(items))
print(list(items))  # 元组的列表 转换之后的列表元素是由元组组成的

# 字典元素的遍历
for item in scores:
    print(item,scores[item],scores.get(item))

d = {'name':'张三','name':'李四'}   # key不允许重复
print(d)

d = {'name':'张三','nickname':'张三'}
print(d)

# 字典生成式
'''
内置函数zip()
    用于将可迭代的对象作为参数，将对象中的元素打包成一个元组，然后返回又这些元组组成 的列表
{item:price for item,price in zip(items,prices)}
表示字典key的表达式    item.upper
表示字典value的表达式   price
自定义key的变量   item
自定义value的变量 price
可迭代的对象      zip(items,prices)
'''
items = ['Fruits','Books','Others']
prices = [96,78,85]
lst = zip(items,prices)
print(list(lst))

d = {item.upper():price for item ,price in zip(items,prices)}
print(d)

items = ['Fruits','Books','Others']
prices = [96,78,85,100,34]

d = {item.upper():price for item ,price in zip(items,prices)}
print(d)
# 与上面的相同，zip的时候会以元素少的为基准来进行生成
