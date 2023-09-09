# Author hugo
# Time 2023/7/9 14:37
# 多态
'''
简单地说，多态就是"具有多种形态"，他指的是
即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
'''


class Animal(object):
    def eat(self):
        print('动物要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person():
    def eat(self):
        print('人吃五谷杂粮')


class Chinken(Animal):
    def hh(self):
        print('6')


def fun(animal):
    animal.eat()


fun(Dog())
fun(Cat())
fun(Person())
fun(Chinken())
'''
静态语言和动态语言关于多态的区别
静态语言实现多态的三个必要条件
    继承
    方法重写
    父类引用指向子类对象
动态语言的多态崇尚“鸭子类型”
    当一只鸟在某些方面像鸭子的时候，这只鸟可以被称为鸭子
    在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为
'''
# 特殊方法和特殊属性
'''
特殊属性
    __dict__ 获得类对象或实例对象所绑定的所有属性和方法的字典
特殊方法
    __len__() 通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
    __add__() 通过重写__add__()方法，可使用自定义对象具有'+'功能
    __new__() 用于创建对象
    __init__() 对创建的对象进行初始化
'''
print(dir(object))


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建C类的对象
class D(A):
    pass


x = C('Jack', 20)  # x是C类的一个实例对象
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)

print('-------------')

print(x.__class__)  # <class '__main__.C'>输出了对象所属的类
print(C.__bases__)  # C类的父类类型的元组
print(C.__base__)  # C类的最近的父类

print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # 子类的列表

a = 20
b = 100
c = a + b  # 两个整数类型的对象的相加操作
d = a.__add__(b)
print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('Jack')
stu2 = Student('李四')
s = stu1 + stu2  # 通过改写__add__()函数，实现了自己创建对象的加法操作
print(s)
s = stu1.__add__(stu2)
print(s)

print('-----------------')
lst = [11, 22, 33, 44]
print(len(lst))
print(lst.__len__())

print(len(stu1))
print(len(stu2))


class Person1(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object这个类对象的id为:{0}'.format(id(object)))
print('Person1这个类对象的id为:{0}'.format(id(Person1)))

# 创建Person1类的实例对象
p1 = Person1('张三', 20)
print('p1这个Person1类的实例对象的id:{0}'.format(id(p1)))
