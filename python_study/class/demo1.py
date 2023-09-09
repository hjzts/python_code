# Author hugo
# Time 2023/7/9 8:56
# 类的创建
class Student1:  # Student1为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    pass


# Python中一切皆对象，Student1时对象吗，内存有开空间吗
print(id(Student1))  # 2070772205648
print(type(Student1))  # <class 'type'>
print(Student1)  # <class '__main__.Student1'>
'''
创建类的语法
class Student:
    pass
类的组成
    类属性
    实例方法
    静态方法
    类方法
'''


class Student:
    native_place = '吉林'  # 类属性,直接写在类里的对象

    def __init__(self, name, age):  # name,age为实例属性
        self.name = name  # 赋值操作，self.name称为实例属性，将局部变量的name的值赋给实体属性
        self.age = age

    # 　实例方法 在类之外定义的称为函数，在类之内定义的称为方法
    def info(self):
        print('我的名字叫：', self.name, '年龄是', self.age)

    def eat(self):
        print(self.name, '在吃饭')

    # 类方法
    @classmethod
    def cm(cls):
        print('使用了classmethod进行修饰类方法')

    # 静态方法
    @staticmethod
    def sm():  # 在静态方法中规定里面不允许写self
        print('使用了staticmethod进行修饰，是静态方法')


# 对象的创建
'''
对象的创建又称为类的实例化
语法
    实例名 = 类名()
有了实例就可以调用类中的内容
'''
# 创建Student类的实例对象
stu1 = Student('Jack', 20)
print(stu1.name)  # 实例属性
print(stu1.age)  # 实例属性
stu1.info()
# 实例方法  对象名.方法名()
Student.info(stu1)
# 与上一行代码功能相同，都是调用Student类中的info方法  类名.方法名(类的对象)
print(id(stu1))
print(type(stu1))
print(stu1)
# 　类属性，类方法，静态方法
'''
类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
'''
# 　类属性的使用方式
print(Student.native_place)  # 访问类属性
stu2 = Student('张三', 20)
stu3 = Student('李四', 30)
print(stu2.native_place)
print(stu3.native_place)

Student.native_place = '天津'
print(stu2.native_place)
print(stu3.native_place)

Student.cm()  # 调用类方法
Student.sm()  # 调用静态方法


# 动态绑定属性和方法
'''
Python是动态语言，在创建对象后，可以动态地绑定属性和方法
'''
def show():
    print('我是一函数')


'''
一个Student类可以创建多个Student类的实例对象，每个实例对象的属性值不同
'''
print('-----------为stu2动态绑定性别属性-----------------')
stu2.gender = '女'  # 动态绑定性别
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

print(stu1.info())
print(stu2.info())
stu2.show = show  # 动态绑定方法
stu2.show()

