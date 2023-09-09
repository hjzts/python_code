# Author hugo
# Time 2023/6/2 0:26

# 二进制 与 字符编码
# byte KB MB GB
# ASCII码
# 字符编码 ASCII GB2312 GBK GB18030 其他国家自己的编码 Unicode几乎包含了全世界的字符 UTF-8
print(chr(0b100111001011000))
print(ord('乘'))

# 标识符与保留字
import keyword

print(keyword.kwlist)
# 变量由三部分组成
# 标识:表示对象所存储的内存地址，使用内置函数id(obj)来获取
# 类型:表示的事对象的数据类型，使用内置函数type(obj)来获取
# 值:表示对象所存储的具体数据
name = '胡健'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
# 当多次赋值后，变量会指向新的空间，原先的会变成内存垃圾，相当于开了一个新盒子
name = '胡健大帅哥'
print(name)

# 数据类型
# 整数类型int 浮点数类型float 布尔类型bool 字符串类型str
# integer 正数负数和零
n1 = 90
n2 = -76
n3 = 0
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
# 整数可以表示为二进制，十进制，八进制，十六进制
print('十进制', 118)
print('十进制', 10101111)
print('二进制', 0b10101111)  # 以0b开头
print('八进制', 0o176)  # 以0o开头
print('十六进制', 0x16f6)  # 以0x开头

# float
a = 3014159
print(a, type(a))
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1 + n2)
print(n1 + n3)
# 解决浮点数 存储造成的精度损失 的问题
from decimal import Decimal

print(Decimal(' 1.1') + Decimal(' 2.2'))

# boolean
# True表示真，False代表假
# 可以转成整数计算 True代表1 False代表0
f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))

print(f1 + 1)
print(f2 + 1)

# string
# 被称为不可变的字符序列
# 使用单引号只能在一行显示
str1 = '哈哈哈哈哈'
str2 = "哈哈哈哈哈"
str3 = '''哈哈哈哈哈，
嘿嘿嘿'''
str4 = """哈哈哈哈哈，
嘿嘿嘿"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))

# 数据类型转换，在将不同数据类型进行拼接时需要
name = '胡健'
age = 18
print(type(name),type(age))
# 当将str类型与int类型进行拼接时会报错，解决方案就是进行类型转换
# print('我加'+name + '今年' + age + '岁')
print('我加'+name + '今年' + str(age) + '岁')
print('------------str()将其他类型转为str类型----------------')
a = 10
b = 198.8
c = False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('------------int()将其他类型转为int类型----------------')
s1 = '128'
f1 = 98.7
s2 = '76.77'
ff = False
s3 = 'hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))        #将str转为int类型，字符串为 数字串
print(int(f1),type(int(f1)))        #将float转为int类型，截取整数部分，舍掉小数部分
# print(int(s2),type(int(s2)))      #将str转为int类型，报错，因为字符串为小数串
print(int(ff),type(int(ff)))        #
# print(int(s3),type(int(s3)))      #将str类型转为int类型，字符串必须为数字串，非数字串是不允许的

print('------------float()将其他类型转为float类型----------------')
s1 = '128.98'
f1 = 98
s2 = '76'
ff = False
s3 = 'hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))