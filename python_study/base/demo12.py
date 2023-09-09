# Author hugo
# Time 2023/7/5 19:02
# 函数
def fun0():
    print('这就是函数！')


'''
函数就是执行特定任务以完成特定功能的一段 代码
为什么需要函数
    复用代码
    隐藏实现细节
    提高可维护性
    提高可读性便于调试
函数的创建
    def 函数名 ([输入参数]):
        函数体
        [return xxx]
'''


def calc(a, b):  # a和b称为形式参数，简称形参，形参的位置是在函数的定义处
    print('a:', a)
    print('b:', b)
    c = a + b
    return c


'''
1.跳到定义函数的函数体内
2.执行函数体
3.跳到函数的调用处
4.继续执行下一条语句
'''
'''
函数调用的参数传递
    位置实参
        根据形参对应的位置进行实参传递
        def calc(a,b)   
        calc(10,20) 10对应a,20对应b
    关键字实参
        calc(b = 10,a = 20)     b是形参名称，10是实参值
        那么a就是20，b就是10
'''
fun0()
fun0()
result = calc(10, 20)  # 10,20称为实际参数的值，简称实参，实参的位置是函数的调用处
print(result)
res = calc(b=10, a=20)  # =左侧的变量名称称为关键字参数
print(res)
'''
函数调用的参数传递内存分析图
'''


def fun(arg1, arg2):
    print('arg1=', arg1)
    print('arg2=', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)


n1 = 11
n2 = [22, 33, 44]
print(n1, id(n1))
print(n2, id(n2))
print('----------------------')
fun(n1, n2)  # 形参名称与实参名称可以不同
print(n1, id(n1))  # 不变
print(n2, id(n2))  # 变了，但是id不变
'''
在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值
如果是可变对象，在函数体的修改会影响到实参的值
'''
# 函数的返回值
'''
函数返回多个值时，结果为元组
    如果函数没有返回值[函数执行完毕后，不需要给调用处提供数据]，return可以省略不写
    函数的返回值如果是1个，直接返回原类型
    函数的返回值如果是多个，返回的结果是元组
'''


def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


lst = [10, 29, 34, 23, 44, 53, 55]
print(fun(lst))


def fun1():
    print('hello')


fun1()


def fun2():
    return 'hello'


res = fun2()
print(res)


def fun3():
    return 'hello', 'world'


print(fun3())
'''
函数在定义时，是否需要返回值，视情况而定
'''
'''
函数定义默认值参数
    函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
'''


def fun4(a, b=10):  # b称为默认值参数
    print(a, b)


fun4(100)  # 只传一个参数，b采用默认值
fun4(20, 30)  # 30将默认值10进行替换

'''
函数的参数定义
    个数可变的位置参数
        定义函数时，可能无法事先确定传递的位置参数的个数时，使用可变的位置参数
        使用*定义个数可变的位置形参
        结果为一个元组
    个数可变的关键字参数
        定义函数时，无法事先确定传递的关键字参数的个数时，使用可变的关键字形参
        使用**定义个数可变的关键字形参
        结果为一个字典
'''


def fun5(*args):
    print(args)
    print(args[0])


fun5(10)
fun5(10, 30)
fun5(30, 405, )


def fun6(**args):
    print(args)


fun6(a=10)
fun6(a=20, b=30, c=40)

'''
可变的位置参数和可变的关键字参数都只能有一个
在一个函数的定义过程中，既有个数可变的关键字形参，又有个数可变的位置形参，要求个数可变的位置形参放在个数可变的关键字形参之前
'''


def fun7(*args1, **args2):
    pass


# def fun8(**args2,*args1):
#     pass
# 报错

def fun8(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun8(10, 20, 30)  # 函数调用时的参数传递，称为位置传参
lst = [11, 22, 33]
fun8(*lst)  # 在函数调用时，将列表的每个元素都转换为位置实参传入

fun8(a=100, c=300, b=200)  # 函数的调用，所以是关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
fun8(**dic)  # 在函数调用时，将字典中的键值对都转换为关键字实参传入


def fun9(a, b=10):
    print('a=', a)
    print('b=', b)


def fun10(*args):  # 个数可变的位置形参
    print(args)


def fun11(**args2):  # 个数可变的关键字形参
    print(args2)


fun10(10, 20, 30, 40)
fun11(a=11, b=22, c=33, d=44, e=55)


def fun12(a, b, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# 调用fun12函数
fun12(10, 20, 30, 40)  # 位置实参传递
fun12(a=10, b=20, c=30, d=40)  # 关键字实参传递
fun12(10, 20, c=30, d=40)  # 前两个参数，采用的是位置实参传递，而c,d采用的是关键字实参传递
'''
需求，c,d只能采用关键字实参传递
'''


def fun13(a, b, *, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# fun13(10, 20, 30, 40)  # 位置实参传递  报错
fun13(a=10, b=20, c=30, d=40)  # 关键字实参传递
fun13(10, 20, c=30, d=40)  # 前两个参数，采用的是位置实参传递，而c,d采用的是关键字实参传递

'''
函数定义时的形参的顺序问题
'''


def fun14(a, b, *, c, d, **args):
    pass


def fun15(*args, **args2):
    pass


def fun16(a, b=10, *args, **args2):
    pass


# 变量的作用域
'''
变量的作用域
    程序代码能访问该变量的区域
    根据变量的有效范围可分为
        局部变量
            在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会变成全局变量
        全局变量
            函数体外定义的变量，可作用于函数内外
'''


def fun17(a, b):
    c = a + b  # c称为局部变量，因为c是在函数体内进行定义的变量,a,b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)


# print(c)
# print(a)  报错，因为a,b超出了作用的范围（超出了作用域）
name = 'hugo'
print(name)


def fun18():
    print(name)


# 　调用函数
fun18()


def fun19():
    global age  # 函数内部定义的变量，局部变量使用global声明，这个变量就变成了全局变量
    age = 20


fun19()
print(age)
# 递归函数
'''
什么是递归函数
    如果在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数
递归的组成部分
    递归调用与递归终止条件
递归的调用过程
    每递归调用一次函数，都会在栈内分配一个栈帧
    每执行完一次函数，都会释放相应的空间
递归的优缺点
    缺点  占用内存多，效率低下
    优点  思路和代码简单
'''


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(6))
def fib(n):
    if n==1 or n==2:
        return 1
    else :
        return fib(n-1)+fib(n-2)
print(fib(6))
for i in range(1,7):
    print(fib(i))
