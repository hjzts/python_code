# Author hugo
# Time 2023/7/9 11:18
# 继承
class Person(object):  # Person继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name, self.age))


# 定义子类
class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self, name, age, teachOfYear):
        super().__init__(name, age)
        self.teachOfYear = teachOfYear


# 测试
stu = Student('Jack', 20, '1001')
teacher = Teacher('lili', 34, 10)

stu.info()
teacher.info()
'''
语法格式
    class 子类类名(父类1,父类2):
        pass
如果一个类没有继承任何类，则默认继承object
Python支持多继承
定义子类时，必须在构造函数中调用父类的构造函数
'''


# 多继承
class A(object):
    pass


class B(object):
    pass


class C(A, B):
    pass
