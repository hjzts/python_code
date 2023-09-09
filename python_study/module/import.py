# Author hugo
# Time 2023/7/26 17:35
# 模块
'''
Modules
函数与模块的关系
    一个模块中可以包含N多个函数
在Python中一个拓展名为.py的文件就是一个模块
使用模块的好处
    方便其他程序和脚本的导入并使用
    避免函数名和变量名冲突
    提高代码的可维护性
    提高代码的可重用性
'''
def fun():
    pass
def fun2():
    pass

class Student:
    native_place = '吉林' # 类属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def cm(cls):
        pass
    @staticmethod
    def sm():
        pass
# 自定义模块
'''
创建模块
    新建一个.py文件，名称尽量不要与Python自带的标准模块名称相同
导入模块
import 模块名称 [as 别名]
form 模块名称 import 函数/变量/类
'''
from math import pi
import math
print(pi)
print(pow(2,3))
print(math.pow(2,3))

# 在import模块导入calc自定义模块使用
import calc
print(calc.add(10,20))
print(calc.div(10,20))

from calc import add
print(add(10,20))