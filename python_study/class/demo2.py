# Author hugo
# Time 2023/7/9 10:24
# 面向对象的三大特征
# 封装 继承 多态
# 封装
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动...')


car = Car('宝马X5')
car.start()
print(car.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在类的外部被使用，所以加了两个_

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# 在类的外部使用name与age
print(stu.name)
# print(stu.__age) AttributeError: 'Student' object has no attribute '__age'
print(dir(stu))
print(stu._Student__age)  # 在类的外部可以通过_Student__age进行访问
