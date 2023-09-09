# Author ***
# Time 2023/6/2 18:57
# import readline
import time
expression = input("请输入表达式(每个字符用空格隔开):")
expression = expression.split()

def get_Reverse_Polish_Notation(expression):
    '''转化逆波兰式'''
    stack = list()
    result = list()
    symbol = ['(', ')', '+', '-', '*', '/']
    value = {
        '(':1,
        ')':1,
        '+':2,
        '-':2,
        '*':3,
        '/':3,
    }
    for i in expression:
        #如果元素是数字,直接进栈
        if i.isdigit():
            result.append(i)
        #如果元素是符号,进入判断
        if i in symbol:
            #如果栈不为空,则判断符号优先级
            if stack:
                #判断如果符号优先级不高于栈顶符号优先级,则出栈,直至优先级大于栈顶符号
                if value[i] <= value[stack[-1]] and i != '(':
                    #如果符号为右括号,则进行匹配左括号
                    if i == ')':
                        while stack[-1] != '(':
                            result.append(stack.pop())
                        stack.pop()
                    #如果不是右括号,则进行出栈操作,直到大于栈顶符号为止
                    else:
                        while True:
                            result.append(stack.pop())
                            if stack:
                                if value[i] > value[stack[-1]] :
                                    stack.append(i)
                                    break
                            else:
                                    stack.append(i)
                                    break

                #如果大于栈顶符号,直接进栈
                else:
                    stack.append(i)
            #如果初始栈为空,则直接进栈第一个符号
            else:
                stack.append(i)
    #遍历完整个表达式,将栈中剩余的符号出栈
    while stack:
        result.append(stack.pop())
    #返回结果列表
    return result

def count_result(result):
    '''计算逆波兰式'''
    stack = list()
    #遍历逆波兰式,如果是数字,直接进栈,如果是符号,则出栈两个操作数,计算出结果入栈
    for i in result:
        if i.isdigit():
            stack.append(i)
        else:
            if i == '+':
                temp = float(stack[-2]) + float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(temp))
            elif i == '-':
                temp = float(stack[-2]) - float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(temp))
            elif i == '*':
                temp = float(stack[-2]) * float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(temp))
            elif i == '/':
                temp = float(stack[-2]) / float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(temp))
    return float(stack[-1])
