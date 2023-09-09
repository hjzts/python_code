# Author hugo
# Time 2023/7/9 14:30
# object类
'''
object类是所有类的父类，因此所有类都有object类的属性和方法
内置函数dir()可以查看指定对象所有属性
object有一个__str__()方法，用于返回一个对于"对象的描述"，对应与内置函数str()经常用于print()方法，帮助我们查看对象的信息，所以我们经常会对__str__()进行重写
'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0}，今年{1}岁'.format(self.name, self.age)


stu = Student('张三', 20)
print(dir(stu))
print(stu)  # 直接输出会调用__str__()这样的方法
print(type(stu))
