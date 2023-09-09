# 转义字符
# \n \r \t \b
print('hello\n world')
print('hello\tworld')
# \t之前是否占了制表位，如果占了实际上的空格会更少
print('helloooo\tworld')
print('hello\rworld')   #world将hello进行了覆盖
print('hello\bworld')   #\b回退一个格，将o退没了

print('http:\\\\localhost')
print('老师说：\'大家好\'')

#原子符，不希望字符串中的转义字符起作用，就使用原子符，就是在字符串之前加上r或R
print(r'hello\nworld')
#注意最后一个字符不能是反斜杠
# print(r'hello\')