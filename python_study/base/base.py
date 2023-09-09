# 标识符
# 即变量、函数、属性、类、模块等可以由程序员制定名称的代码模块
# 变量
# 语句
# 庞大的数据库和胶水语言

# 输出函数print
# 输出数字
print(520)
print(98.5)
# 输出字符串
print("hello world")
# 含有运算符的表达式
print(3+1)
# 将数据输出到文件中 注意点：指定的盘符存在，使用file = fp
fp = open('/python_study/text.txt', 'a+')       #如果文件不存在就创建，存在就在文件内容后面继续追加
print('hello world',file = fp)
fp.close()
# 不换行进行输出(输出内容在同一行当中)
print('hello','world','Python')

