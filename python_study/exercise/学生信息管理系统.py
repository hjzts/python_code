# Author hugo
# Time 2023/8/11 13:02
'''
学生信息管理系统
'''
import os.path

'''
需求分析
系统设计
系统开发必备
主函数设计
学生信息维护模块设计
查询/统计模块设计
排序模块设计
项目打包
'''

# 需求分析
'''
学生管理系统应具备的功能
    添加学生及成绩信息
    将学生信息保存到文件中
    修改和删除学生信息
    查询学生信息
    根据学生成绩进行排序
    统计学生的总分
'''
# 系统设计
'''
系统功能结构
    学生信息管理系统的7大模块
        录入学生信息模块
        查找学生信息模块
        删除学生信息模块
        修改学生信息模块
        学生成绩排名模块
        统计学生总人数模块
        显示全部学生信息模块
系统业务流程
    用户->主界面->功能菜单->y or n
'''
# 系统开发必备
'''
系统开发环境
    操作系统
    Python解释器版本
    开发工具
    Python内置模块
项目目录结构
'''
# 主函数设计
'''
主函数的业务流程
    开始 -> while True -> 显示主菜单 -> 选择菜单项
    0 --- 退出系统
    1 --- 录入学生信息，调用insert()函数
    2 --- 查找学生信息，调用search()函数
    3 --- 删除学生信息，调用delete()函数
    4 --- 修改学生信息，调用modify()函数
    5 --- 对学生成绩进行排序，调用sort()函数
    6 --- 统计学生总人数，调用total()函数
    7 --- 显示所有学生的信息，调用show()函数
'''

filename = 'student.txt'


def main():
    while True:
        menm()
        choice = int(input('请选择'))
        if choice in range(0, 8):
            if choice == 0:
                answer = input('您确定要退出系统吗?y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menm():
    print('==================学生信息管理系统==================')
    print('---------------------功能菜单---------------------')
    print('\t\t\t\t 1.录入学生信息')
    print('\t\t\t\t 2.查找学生信息')
    print('\t\t\t\t 3.删除学生信息')
    print('\t\t\t\t 4.修改学生信息')
    print('\t\t\t\t 5.排序')
    print('\t\t\t\t 6.统计学生总人数')
    print('\t\t\t\t 7.显示所有学生信息')
    print('\t\t\t\t 0.退出')
    print('-------------------------------------------------')


'''
业务流程
    开始 -> while True -> 输入学生姓名或者ID -> 判断是否有输入
    -> 输入成绩 -> 保存到列表中 -> 判断是否继续 -> 结束后保存到文件中
具体实现
save(student) 函数，用于将学生信息保存到文件
insert()函数，用于录入学生信息
'''


def insert():
    student_list = []
    while True:
        id = input('请输入ID(如1001)')
        if not id:
            break
        name = input('请输入姓名')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩'))
            python = int(input('请输入Python成绩'))
            java = int(input('请输入Java成绩'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加学生信息?y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕！！！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


'''
while True -> 判断输入是否为1或2 -> 输入学生ID或姓名
-> 读取学生信息列表 -> 遍历列表并将符合条件的信息保存到新列表 ->显示新列表的内容并显示是否继续
'''


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1,按姓名输入查找请输入2')
            if mode == '1':
                id = input('请输入学生ID')
            elif mode == '2':
                name = input('请输入学生姓名')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否要继续查询?y/n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存该学员信息')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示')
        return
    # 定义标题的显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format((item.get('id')), item.get('name'), item.get('english'), item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))))


'''
实现删除学生信息功能
    从控制台录入学生ID，到磁盘文件中找到对应的学生信息，并将其删除
业务流程
    开始 -> while True -> 输入学生ID -> 判断是否有输入 -> 读取全部学生信息到列表 
    遍历列表并将不删除的信息重新写入文件 -> 希纳是全部学生信息，并选择是否继续 -> over
具体实现
    编写主函数中调用的删除学生信息的函数delete()
    调用了show()函数显示学生信息，该函数的功能将在后面完成
'''


def delete():
    while True:
        student_id = input('请输入要删除的学生的ID')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()
            answer = input('是否继续删除?y/n\n')
            if answer == 'y':
                continue
            else:
                break


'''
判断学生文件是否存在->读取全部学生列表->以写的模式打开文件
->输入学生ID->输入新的学生信息->写入信息到文件->是否继续->
'''


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员ID:\n')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改他的相关信息了')
                while True:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['english'] = input('请输入英语成绩:')
                        d['python'] = input('请输入python成绩')
                        d['java'] = input('请输入java成绩')
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否继续修改其他学生信息?y/n')
        if answer == 'y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('请选择(0.升序,1.降序)')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input('请选择排序方式(0.按总成绩排序,1.按英语成绩排序,2.按python成绩排序,3.按java排序成绩排序')
    if mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)

    else:
        print('您的输入有误,请重新输入')
        sort()
    show_student(student_new)


'''
统计学生总人数
判断学生文件在学生信息文件是否存在->读取全部信息到列表-> 
判断列表是否不为空-> 统计学生人数并输出
'''


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息')


'''
判断学生信息文件是否存在->打开文件->读取全部信息到列表->将学生信息转换为字典并添加到列表中
'''


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存数据信息！！！')


if __name__ == '__main__':
    main()
