# Author hugo
# Time 2023/8/3 18:22
print('你好，中国')

# 文件的读写操作
'''
内置函数open()创建文件对象
    通过IO流将磁盘文件中的内容与程序中的对象中的内容进行同步
语法规则
    file          = open(          filename          [,mode,          encoding])
    被创建的文件对象   创建文件对象的函数 要创建或打开的文件名称  打开模式默认为只读  默认文件中字符的编码格式为gbk
'''
file = open('a.txt','r')
print(file.readlines())
file.close()
'''
文件的类型
    按文件中数据的组织形式，文件分为以下两大类
        文本文件 : 存储的是普通字符文本，默认为unicode字符集，可以使用记事本程序打开
        二进制 : 把数据内容用字节进行存储，无法用记事本打开，必须使用专用的软件打开
'''
file2 = open('b.txt','w')
file2.write('helloworld')
file2 = open('b.txt','a')
file2.write('Python')
file2.close()

src_file = open('logo.png','rb')
target_file = open('copylogo.png','wb')

target_file.write(src_file.read())

target_file.close()
src_file.close()

file = open('a.txt','a+')
file.write('\nhello')
s_list = ['\njava','go','python']
file.writelines(s_list)
file.close()

file = open('a.txt','w+')
s_list = ['中国','\n美丽']
file.writelines(s_list)
file.seek(2)
print(file.read())
print(file.tell())
file.close()

file = open('d.txt','a')
file.write('hello')
file.flush()
file.write(' world')
file.close()