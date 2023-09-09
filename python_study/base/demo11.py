# Author hugo
# Time 2023/7/5 10:58
# 字符串
'''
在python中字符串是基本数据类型，是一个不可变的字符序列
字符串的驻留机制
    仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中
    python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同的字符串时
    不会开辟新空间，而是把该字符串的地址赋给新创建的变量
'''
a = 'python'
b = "python"
c = '''python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))
'''
驻留机制的几种情况（交互模式）
    字符串长度为0或1时
    符合标识符的字符串
    字符串只在编译时进行驻留，而非运行时
    [-5,256]之间的整数数字
sys中的intern方法强制两个字符串指向同一个对象
pycharm对字符串进行了优化处理

优缺点：    
    当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁
    提升效率和节约内存，因此拼接字符串和修改字符串是会比较影响性能的
    在需要进行字符串拼接时建议使用str类型的join方法，而非+，因为join()方法是
    先计算出所有字符串的长度，然后再拷贝，只new一次对象，效率要比'+'效率高
'''
s1 = 'abc%'
s2 = 'abc%'
print(s1 is s2)

# 字符串的常用操作
# 字符串函数的查询操作的方法
'''
查询方法
index()     查找子串substr第一次出现的位置，如果查找的子串不存在时则抛出ValueError
rindex()    查找子串substr最后一次出现的位置，如果查找的子串不存在时则抛出ValueError
find()      查找子串substr第一次出现的位置，如果查找的子串不存在时则返回-1
rfind()     查找子串substr最后一次出现的位置，如果查找的子串不存在时则返回-1
'''
s = 'hello,hello'
print(s.index('lo'))
print(s.rindex('lo'))
print(s.find('lo'))
print(s.rfind('lo'))

# print(s.index('k'))
# print(s.rindex('k'))
print(s.find('k'))
print(s.rfind('k'))

# 大小写转换操作的方法
'''
大小写转换
    upper()         把字符串的所有字符都转成大写字母
    lower()         把字符串的所有字符都转成小写字母
    swapcase()      把字符串的所有大写字母转成小写字母，把所有小写字母都转成大写字母
    capitalize()    把第一个字符转换为大写，把其余字符转换成小写
    title()         把每个单词的第一个字符转换成大写，把每个单词的剩余字符转换成小写
'''
s = 'hello,python'
a = s.upper()  # 转成大写之后回产生一个新的字符串对象
print(a, id(a))
print(s, id(s))
print(s.lower(), id(s.lower()))
b = s.lower()  # 转换之后，会产生一个新的字符串对象
print(b, id(b))
print(s, id(s))
print(b == s)  # True
print(b is s)  # False

s2 = 'hello,Python'
print(s2.swapcase())
print(s2.capitalize())
print(s2.title())

# 　字符串内容对齐操作的方法
'''
字符串对齐
    center()    居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
    ljust()     左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
    rjust()     右对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
    zfill()     右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身
'''
s = 'hello,Python'
print(s.center(20, '*'))
print(s.ljust(20, '*'))
print(s.ljust(10))
print(s.ljust(20))
print(s.rjust(20, '*'))
print(s.rjust(20))
print(s.rjust(10))
print(s.zfill(20))
print(s.zfill(10))

print('-8910'.zfill(8))

# 字符串劈分操作的方法
'''
字符串的劈分
split() 
        从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
        以通过参数sep指定劈分字符串的劈分符
        通过参数maxsplit指定劈分字符串的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
rsplit()
        从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
        以通过参数sep指定劈分字符串的劈分符
        通过参数maxsplit指定劈分字符串的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
'''
s = 'hello world Python'
lst = s.split()
print(lst)

s1 = 'hello|world|Python'
lst = s1.split(sep='|')
print(lst)
print(s1.split(sep='|', maxsplit=1))

print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))

# 判断字符串操作的方法
'''
判断字符串的方法
    isidentifier()      判断指定的字符串是不是合法的标识符
    isspace()           判断指定的字符串是否全部由空白字符组成(回车、换行、水平制表符)
    isalpha()           判断指定的字符串是否全部由字母组成
    isdecimal()         判断指定字符串是否全部由十进制的数字组成
    isnumeric()         判断指定的字符串是否全部由数字组成
    isalnum()           判断指定的字符串是否全部由字母和数字组成
'''
s = 'hello,python'
print('1', s.isidentifier())
print('2', 'hello'.isidentifier())
print('3', '张三_'.isidentifier())
print('4', '张三_123'.isidentifier())
print(s.isspace())
print('5', '\t'.isspace())
print('6', 'abc'.isalpha())
print('7', '张三'.isalpha())  # True
print('8', '张三1'.isalpha())
print(s.isalpha())
print(s.isdecimal())
print('9', '123'.isdecimal())
print('10', '123四'.isdecimal())
print('11', '123四'.isnumeric())
print('12', 'IIIIII'.isnumeric())  # False
print(s.isnumeric())
print(s.isalnum())
print('13', 'abc1'.isalnum())
print('14', 'abc!'.isalnum())

# 字符串操作的其他方法
'''
字符串替换
    replace()   第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的字符串
                替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大替换次数
字符串的合并
    join()      将列表或元组中的字符串合并成一个字符串
'''
s = 'hello,python'
print(s.replace('python', 'java'))
s1 = 'hello,python,python,python'
print(s1.replace('python', 'java', 2))

lst = ['hello', 'java', 'python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'java', 'python')
print(''.join(t))

print('*'.join('python'))

# 　字符串的比较操作
'''
运算符
    >,>=,<,<=,==,!=
比较规则
    首先比价两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，知道两个字符串的字符不相等时
    其比较结果就是两个字符串的比较结果，两个字符串的所有后续字符不再被比较
比较原理
    两上述字符进行比较时，比较的是其ordinal value（原始值），调用内置函数ord可以得到指定字符的ordinal value
    与内置函数对应ord对应的是内置函数chr，调用内置函数chr时指定ordinal value 可以得到其对应的字符
'''
print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord('b'))
print(chr(97), chr(98))
print(ord('杨'))
print(ord('胡'))
print(ord('健'))
'''
==比较的是value
is 比较的是id是否相等
'''
'''
字符串是不可变类型
    不具备增、删、改等操作
    切片操作将产生新的对象
'''
s = 'hello,Python'
s1 = s[:5]  # 由于没有指定起始位置，所以从0开始切
s2 = s[6:]  # 由于没有指定结束位置，所以切到字符串的最后一个元素
print(s1)
print(s2)
s3 = '!'
newstr = s1 + s3 + s2
print(newstr)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))

print(s[1:5:1])  # 从1开始数到5（不包含5），步长为1
print(s[::2])  # 默认从0开始，没有写结束，默认到字符串的最后一个元素，步长为2，两个元素之间的索引之差为2
print(s[::-1])  # 步长为负数，默认从字符串的最后一个元素开始，到字符串的第一个元素开始
print(s[-6::1])
# 格式化字符串
'''
格式化字符串
%作占位符   %s字符串 %i或%d整数 %f浮点数 
{}作占位符  
f-string
'''
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))
print('我叫{0}，今年{1}岁'.format(name, age))
print(f'我叫{name}，今年{age}岁')

print('%10d' % 99)
print('hellohello')
print('%f' % 3.1415926)
print('%.3f' % 3.1415926)
print('%10.3f' % 3.1415926)

print('{}'.format(3.1415926))
print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))  # .3表示一共是3位数
print('{0:.3f}'.format(3.1415926))  # .3f表示是三位小数
print('{:.3f}'.format(3.1415926))
print('{:10.3f}'.format(3.1415926))  # 同时设置宽度和精度，一共是10位，3位是小数

# 字符串的编码转换
'''
为什么需要字符串的编码转换
A计算机    str在内存中Unicode表示 
编码
byte字节传输
解码
B计算机 显示

编码与解码的方式
    编码:将字符串转换为二进制数据(bytes)
    解码:将bytes类型的数据转换成字符串类型
'''
s = '天涯共此时'
print(s.encode(encoding='GBK'))  # 在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编码格式中，一个中文占三个字节

byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
# print(byte.decode(encoding='UTF-8'))  编码与解码的格式要相同
byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
