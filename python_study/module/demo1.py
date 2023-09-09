# Author hugo
# Time 2023/7/30 23:30
# 在demo1的模块中导入package1包
import package1.moduleA as ma  # 别名

# print(package1.moduleA.a)
print(ma.a)
# 导入带有包的模块是的注意事项
import package1
import calc
# 使用import方式进行导入是，只能跟包名或模块名

from package1 import moduleA
from package1.moduleA import a
# 使用from ... import 可以导入包，模块，函数，变量