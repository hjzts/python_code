# Author hugo
# Time 2023/8/10 15:24
print(type(open('a.txt','r')))
# with语句（上下文管理器）
'''
with语句可以自动管理上下文资源，不论什么原因跳出with块，都能够确保文件正确的关闭，以此来达到释放资源的目的
实现了__enter__()方法和__exit__()方法，遵守了上下文管理协议
open('a.txt','r') 上下文表达式，结果为上下文管理器，同时创建一个运行时上下文
    自动调用__enter__()方法，并将返回值赋值给src_file
as file 可选项，上下文管理器对象的引用
    离开运行时上下文，自动调用上下文管理器的特殊方法__exit__()
'''
with open('a.txt','r') as file:
    print(file.read())

'''
MyContentMgr实现了特殊方法__enter__(),__exit__()称该类对象遵守了上下文管理器协议
该类对象的实例对象称为上下文管理器
    MyContentMgr()
'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')

with MyContentMgr() as file: # 相当于file = MyContentMgr()
    file.show()

with open('logo.png','rb') as src_file:
    with open('copy2logo.png','wb') as target_file:
        target_file.write(src_file.read()) # 实现文件的复制，不需要手动写关闭
