# Author hugo
# Time 2023/8/11 12:53
import os
path = os.getcwd()
lst_files = os.walk(path)
print(lst_files) # 迭代器对象
for dirpath,dirname,filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('-----------------------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))# 子目录
    print('-----------------------------')
    for file in filename:
        print(os.path.join(dirpath,file))
