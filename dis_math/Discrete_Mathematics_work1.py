# -*- coding:utf-8 -*- 
# 命题逻辑公式类型判断器
# 2017.10.21

#符号声明：
#原子命题用字母表示；
#‘~’表示否定，‘&’表示合取，‘|’表示析取，‘>’表示蕴涵，‘#’表示等价，‘@’表示异或，‘$’表示与非，‘*’表示或非

from tkinter import *
import tkinter.messagebox as messagebox


inputString = '' #输入的命题公式字符串
funcString = '' #c存放符号替换后的公式字符串
nvariable = [] #变量数量
Orstring = [] #主析取范式最小项
Andstring = [] #主合取范式最大项
former = '' #符号前面的部分
latter = '' #符号后面的部分
result = ''



#提取变量，判断输入
def getVariable():
	global inputString, nvariable
	for c in inputString:
		if c >= 'A' and c <= 'Z' or c >= 'a' and c <= 'z': #提取变量
			if c not in nvariable:
				nvariable.append(c)
		elif c != '~' and c != '&' and c != '|' and c != '>' and c != '#' and c != '@' and c != '$' and c != '*' and c != '(' and c != ')': #若非符号非变量，抛出错误
			print('There is something wrong in your input string.')
			#main() #重新输入
	nvariable = sorted(nvariable) #对变量排序

#处理>,#,@,$,*
def func(c):
	global inputString, funcString, former, latter
	slen = len(funcString)
	#遍历字符串
	for i in range(0,slen):
		if funcString[i] is c:
			#找到former
			if funcString[i-1] is not  ')':
				if funcString[i-2] is not '~':
					former = funcString[i-1]
				else:
					former = funcString[i-2:i]
			else:
				flag = 1
				j = i-1-1
				while flag != 0 and j >= 0:
					if funcString[j] is ')':
						flag += 1
						j -= 1
					elif funcString[j] is '(':
						flag -= 1
						j -= 1
					else:
						j -= 1
				former = funcString[j+1:i]

#			print(former)

			#找到latter
			if funcString[i+1] is not  '~':
				if funcString[i+1] is not '(':
					latter = funcString[i+1]
				else:
					flag = 1
					j = i+1+1
					while flag != 0 and j < slen: 
						if funcString[j] is '(':
							flag += 1
							j += 1
						elif funcString[j] is ')':
							flag -= 1
							j += 1
						else:
							j += 1
					latter = funcString[i+1:j]
			else:
				if funcString[i+2] is not '(':
					latter = funcString[i+1:i+3]
				else:
					flag = 1
					j = i+2+1
					while flag != 0 and j < slen:
						if funcString[j] is '(':
							flag += 1
							j += 1
						elif funcString[j] is ')':
							flag -= 1
							j += 1
						else:
							j += 1
					latter = funcString[i+1:j]			#符号替换

#			print(latter)

			if c is '>':
				funcString = funcString.replace(former+'>'+latter, '('+'~'+former+'|'+latter+')')
				print(funcString)
			if c is '#':
				funcString = funcString.replace(former+'#'+latter, '(('+former+'&'+latter+')|('+'~'+former+'&'+'~'+latter+'))')
			if c is '@':
				funcString = funcString.replace(former+'@'+latter, '(('+former+'&'+'~'+latter+')|('+'~'+former+'&'+latter+'))')
			if c is '$':
				funcString = funcString.replace(former+'$'+latter, '~'+'('+former+'&'+latter+')')
			if c is '*':
				funcString = funcString.replace(former+'*'+latter, '~'+'('+former+'|'+latter+')')
			
			func(c)

#		print(i, slen)

#符号替换
def input2func():
	global inputString, funcString
	funcString = inputString
	func('>') #蕴涵
	func('#') #等价
	func('@') #异或
	func('$') #与非
	func('*') #或非

#利用真值表法计算主析取范式和主合取范式
def binaryCal():
	global inputString, funcString, nvariable, Orstring, Andstring
	nlen = len(nvariable) #变量个数
	n = 2 ** nlen #所有情况的个数
	#获取真值表。赋值计算
	for i in range(0,n):
		value = [] #赋值
		nowline = i #当前行数
		for j in range(0,nlen):
			value.append(0) #占位
			value[j] = nowline%2
			nowline = nowline//2
		value.reverse()
		value = list(map(str, value))
		strv = funcString
		for k in range(0,nlen):
			strv = strv.replace(nvariable[k], value[k])
		result = eval(strv)&1
		#判断是最大项还是最小项
		if result == 1:
			Orstring.append(i) #最小项
		else:
			Andstring.append(i) #最大项

#根据最小项和最大项个数判断公式类别
def myoutput():
	global Orstring, Andstring, result
	orlen = len(Orstring)
	andlen = len(Andstring)
	if orlen == 0:
		result = '矛盾式'
	elif orlen > 0:
		if andlen == 0:
			result = '重言式'
		else:
			result = '可满足式'

#主函数
def main():
	global result
	#myinput()
	getVariable()
	input2func()
	#如果输入错误，则在赋值函数中会出错，抛出错误，显示"wrong"
	try:
		binaryCal()
	except Exception as e:
		print('Error:', e)
		result = 'input wrong!'
	else:
		myoutput()
	finally:
		show()


#构建界面
def createWidgets():
	global label1, label2, StringIn, StringO1

	label = Label(text='输入公式').grid(row=0,column=0)

	StringIn = Label(text='输入公式',width=20,height=1,relief="ridge")
	StringIn.grid(row=0,column=1,columnspan=2)

	submitbutton = Button(text='开始计算', bg="green",command=lambda:submit(),width=10,height=1)
	submitbutton.grid(row=1, column=1)

	clearbutton = Button(text='清空', bg="yellow",command=lambda:clear(),width=10,height=1)
	clearbutton.grid(row=1, column=2)

	alertButton = Button(text='?', bg="red",command=help,width=3,height=1)
	alertButton.grid(row=0,column=3)

	button1 = Button(text='~', command=lambda:insert(1),width=10,height=1)
	button1.grid(row=2,column=0)

	button2 = Button(text='&', command=lambda:insert(2),width=10,height=1)
	button2.grid(row=2,column=1)

	button3 = Button(text='|', command=lambda:insert(3),width=10,height=1)
	button3.grid(row=2,column=2)

	buttona = Button(text='a', command=lambda:insert('a'),width=10,height=1)
	buttona.grid(row=2,column=3)

	button4 = Button(text='>', command=lambda:insert(4),width=10,height=1)
	button4.grid(row=3,column=0)

	button5 = Button(text='#', command=lambda:insert(5),width=10,height=1)
	button5.grid(row=3,column=1)

	button6 = Button(text='$', command=lambda:insert(6),width=10,height=1)
	button6.grid(row=3,column=2)

	buttonb = Button(text='b', command=lambda:insert('b'),width=10,height=1)
	buttonb.grid(row=3,column=3)

	button7 = Button(text='@', command=lambda:insert(7),width=10,height=1)
	button7.grid(row=4,column=0)

	button8 = Button(text='*', command=lambda:insert(8),width=10,height=1)
	button8.grid(row=4,column=1)

	button9 = Button(text='(', command=lambda:insert(9),width=10,height=1)
	button9.grid(row=4,column=2)

	buttonc = Button(text='c', command=lambda:insert('c'),width=10,height=1)
	buttonc.grid(row=4,column=3)

	button10 = Button(text=')', command=lambda:insert(10),width=10,height=1)
	button10.grid(row=5,column=0)

	buttonc = Button(text='p', command=lambda:insert('p'),width=10,height=1)
	buttonc.grid(row=5,column=1)

	buttonc = Button(text='q', command=lambda:insert('q'),width=10,height=1)
	buttonc.grid(row=5,column=2)

	buttonc = Button(text='r', command=lambda:insert('r'),width=10,height=1)
	buttonc.grid(row=5,column=3)

	label2 = Label(text='公式类型:',height=4)
	label2.grid(row=6, column=0)
	StringO1 = Label(text='')
	StringO1.grid(row=6,column=1)

#按键插入输入框
def insert(k):
	global inputString,StringIn
	if k is 1:
		inputString = inputString + '~'
	elif k is 2:
		inputString = inputString + '&'
	elif k is 3:
		inputString = inputString + '|'
	elif k is 4:
		inputString = inputString + '>'
	elif k is 5:
		inputString = inputString + '#'
	elif k is 6:
		inputString = inputString + '$'
	elif k is 7:
		inputString = inputString + '@'
	elif k is 8:
		inputString = inputString + '*'
	elif k is 9:
		inputString = inputString + '('
	elif k is 10:
		inputString = inputString + ')'
	elif k is 'a':
		inputString = inputString + 'a'
	elif k is 'b':
		inputString = inputString + 'b'
	elif k is 'c':
		inputString = inputString + 'c'
	elif k is 'p':
		inputString = inputString + 'p'
	elif k is 'r':
		inputString = inputString + 'r'
	elif k is 'q':
		inputString = inputString + 'q'

	StringIn.config(text=inputString)



#开始计算
def submit():
	global inputString,StringIn, StringO1, StringO2
	StringO1.config(text='')
	main()
	#print(inputString)

#清空
def clear():
	global result, inputString, nvariable, funcString, Orstring, Andstring, former, latter
	#清空储存数据，为下一次做准备
	StringIn.config(text='')
	StringO1.config(text='')
	inputString = ''
	funcString = ''
	nvariable = []
	Orstring = []
	Andstring = []
	result = ''
	former = ''
	latter = ''

#帮助界面
def help():
	messagebox.showinfo('Help','原子命题用字母表示\n‘~’表示否定\n‘&’表示合取\n‘|’表示析取\n‘>’表示蕴涵\n‘#’表示等价\n‘@’表示异或\n‘$’表示与非\n‘*’表示或非')

#显示
def show():
	global result, inputString, nvariable, funcString, Orstring, Andstring, former, latter
	StringO1.config(text=result)
	#清空储存数据，为下一次做准备
	inputString = ''
	funcString = ''
	nvariable = []
	Orstring = []
	Andstring = []
	result = ''
	former = ''
	latter = ''

if __name__ == '__main__':
	root = Tk()
	root.title('15031216')
	createWidgets()
	mainloop()