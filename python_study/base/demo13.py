# Author hugo
# Time 2023/7/8 14:19
# python 异常处理机制
try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    result = a / b
    print('结果为', result)
except ZeroDivisionError:
    print('除数不能为0哦')
print('程序1结束')
'''
try:
    #　可能会出现异常的代码
except xxx(异常类型):
    # 报错后执行的代码
    # 异常处理代码
'''
# 多个except结构
'''
捕获异常的顺序按照先子类后父类的顺序，为了避免一楼可能出现的异常，可以在最后增加BaseException
try:
    #　可能会出现异常的代码
except Exception1:
    # 异常处理代码
except Exception2:
    # 异常处理代码
except BaseException:
    # 异常处理代码
'''
try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    result = a / b
    print('结果为', result)
except ZeroDivisionError:
    print('除数不能为0哦')
except ValueError:
    print('不能将字符串转换为数字')
except BaseException as e:
    print(e)
print('程序2结束')

# try...except...else结构
'''
如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
'''
try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    result = a / b
except BaseException as e:
    print(e)
else :
    print('结果为：',result)
print('程序3结束')
# try...except...else...finally结构
'''
finally块无论是否发生异常都会被执行，能常用来释放try块申请的资源
'''
try:
    a = int(input('请输入一个整数：'))
    b = int(input('请输入另一个整数：'))
    result = a / b
except BaseException as e:
    print(e)
else :
    print('结果为：',result)
finally:
    print('无论是否产生异常，都会被执行的代码')
print('程序4结束')

import traceback

try:
    num = 10/0
except:
    traceback.print_exc()