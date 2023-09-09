# Author hugo
# Time 2023/6/26 23:13

# input()函数
# 作用：接收来自用户的输入
# 返回值类型：输入值的类型为str
# 值的存储：使用=对输入的值进行存储
present = input('大圣想要什么礼物呢')
print(present, type(present))

# 实现加法add功能
# 从键盘录入两个整数，计算两个整数的和
a = int(input('请输入一个加数：'))
# a = int(a)  #将转换之后的值存储到a中
b = int(input('请输入另一个加数'))
# b = int(b)
print(type(a), type(b))
print(a + b)

# python中的运算符
'''
算数运算符｛标准算数运算符（+，-，*，/，//(整除)），取余运算符(%)，幂运算符(**)｝
赋值运算符
比较运算符
布尔运算符
位运算符
'''

print(1 + 1)  # 加饭运算
print(1 - 1)  # 减法运算
print(2 * 4)  # 乘法运算
print(1 / 2)  # 除法运算
print(11 / 2)  # 除法运算
print(11 // 2)  # 整除运算
print(11 % 2)  # 取余运算
print(2 ** 3)  # 表示的是2的3次方

# 一正一负的整除等的问题
print(9 // 4)  # 2
print(-9 // -4)  # 2

print(9 // -4)  # -3
print(-9 // 4)  # -3      一正一负向下取整数

print(9 % -4)  # -3      公式 余数 = 被除数 - 除数 * 商
print(-9 % 4)  # 3

# 赋值运算符
'''
运算顺序是从右到左
支持链式赋值          a = b = c = 20
支持参数赋值          += -= *= /= //= %=
支持系列解包赋值        a,b,c = 20,30,40
'''
a = b = c = 20  # 链式赋值，其实只有一个值，abc只是三个引用
print(a, id(a))
print(b, id(b))
print(c, id(c))

a = 20
a += 30  # 相当于 a = a + 30
print(a)
a -= 10
print(a)
a *= 2
print(a)
print(type(a))
a /= 3
print(a)
print(type(a))
a //= 2
print(a)
print(type(a))
a %= 3
print(a)

a, b, c = 20, 30, 40  # 左右变量的个数和值的个数要相等
print(a, b, c)

print('--------交换两个变量的值------------')
a, b = 10, 20
print('交换之前：', a, b)
# 交换
a, b = b, a
print('交换之后：', a, b)

# 比较运算符 对变量或表达式的结果进行大小、真假等比较
'''
> < >= <= !=
==      对象value的比较
is , is not         对象id的比较
'''
a, b = 10, 20
print('a > b 吗？', a > b)  # False
print('a < b 吗？', a < b)
print('a <= b 吗？', a <= b)
print('a >= b 吗？', a >= b)
print('a == b 吗？', a == b)
print('a != b 吗？', a != b)

'''一个 = 称为赋值运算符， == 称为比较运算符
    一个变量由三部分组成，标识，类型，值
    == 比较的是值
    比较对象的标识使用is
'''
a = 10
b = 10
print(a == b)  # True 说明a,b的value相同
print(a is b)  # True 说明a,b的标识相同

lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # value True
print(lst1 is lst2)  # id False
print(id(lst1))
print(id(lst2))
print(a is not b)  # False
print(lst1 is not lst2)  # True

# 布尔运算符
# and , or , not , in , not in
a, b = 1, 2
print(a == 1 and b == 2)  # True
print(a == 1 and b < 2)
print(a != 1 and b == 2)
print(a != 1 and b != 2)

print(a == 1 or b == 2)  # True
print(a == 1 or b < 2)
print(a != 1 or b == 2)
print(a != 1 or b != 2)

# not 对布尔运算类型的操作数取反
f = True
f2 = False
print(not f)
print(not f2)

s = 'helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)

# 位运算符
'''
按位与 & 对应数位都是1结果才是1
按位或 | 对应数位都是0结果才是0
左移位运算符 << 高位溢出舍弃，低位补0
右移位运算符 >> 低位溢出舍弃，高位补0
'''
print(4 & 8)
print(4 | 8)
print(4 << 1)
print(4 << 2)
print(4 >> 1)
print(4 >> 2)

# 运算符的优先级
'''
算术运算符  **      *,/,//,%     +,-
位运算   << >>     &     |  
比较运算符 
bool运算符  and   or
赋值运算符 =
'''