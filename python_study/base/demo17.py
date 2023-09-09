# Author hugo
# Time 2023/8/11 12:28
# 目录操作
'''
os模块是python内置的与操作系统功能和文件系统相关的模块，
    该模块中的语句的执行结果通常与操作系统有关，
    在不同的操作系统上运行，得到的结果可能不一样
os模块与os.path模块用于对目录或文件进行操作
'''
import os
# os.system('notepad.exe') 不可用
# os.system('calc.exe')

# 直接调用可执行文件
# os.startfile('E:\\Software\\WeChat\\WeChat.exe')

print(os.getcwd())
lst = os.listdir('../base')
print(lst)

os.mkdir('newdir2')
os.makedirs('A/B/C')

os.rmdir('newdir2')
os.removedirs('A/B/C')

os.chdir('D:\\python_project\\python_study\\class')
print(os.getcwd())

import os.path
print(os.path.abspath('demo13.py'))
print(os.path.exists('demo13.py'),os.path.exists('demo18.py'))
print(os.path.join('E:\\Python','demo13.py'))
print(os.path.split('D:\\python_project\\python_study\\base\\demo13.py'))
print(os.path.splitext('demo13.py'))

print(os.path.basename('D:\\python_project\\python_study\\base\\demo13.py'))
print(os.path.dirname('D:\\python_project\\python_study\\base\\demo13.py'))

print(os.path.isdir('D:\\python_project\\python_study\\base\\demo13.py'),os.path.isdir('D:\\python_project\\python_study\\base'))


