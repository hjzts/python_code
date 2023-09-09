# Author hugo
# Time 2023/7/9 14:23
# 方法重写
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name, self.age))
# 定义子类
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no
    def info(self):
        super().info()
        print('学号:[0]'.format(self.stu_no))
# 测试
stu = Student('Jack',20,'1001')
stu.info()
'''
方法重写
    如果子类对继承字父类的某个属性或者方法不满意，可以在子类中对其(方法体)进行重新编写
    子类重写后的方法可以通过super().xxx()调用父类中被重写的方法
'''
