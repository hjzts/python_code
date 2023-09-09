# Author csdn
# Time 2023/7/5 14:09
def gewei1(num):
    if shiweiyushu == 4:
        return 'IV'
    elif shiweiyushu == 9:
        return 'IX'
    elif num < 4:
        return 'I' * num
    else:
        a = num % 5
        return 'V' + 'I' * a


def shiwei1(num):
    if num < 50:
        return 'X' * shiwei + gewei1(shiweiyushu)
    elif shiwei == 4:
        return 'XL' + gewei1(shiweiyushu)
    elif shiwei == 9:
        return 'XC' + gewei1(shiweiyushu)
    else:
        return 'L' + 'X' * (shiwei - 5) + gewei1(shiweiyushu)


def baiwei1(num):
    if num < 500:
        return 'C' * baiwei + shiwei1(baiweiyushu)
    elif baiwei == 4:
        return 'CD' + shiwei1(baiweiyushu)
    elif baiwei == 9:
        return 'CM' + shiwei1(baiweiyushu)
    else:
        return 'D' + 'C' * (baiwei - 5) + shiwei1(baiweiyushu)


def qianwei1():
    return 'M' * qianwei + baiwei1(qianweiyushu)


num = int(input('请输入：'))

qianweiyushu = num % 1000
qianwei = num // 1000

baiweiyushu = qianweiyushu % 100
baiwei = qianweiyushu // 100

shiweiyushu = baiweiyushu % 10
shiwei = baiweiyushu // 10

s = qianwei1()
print(s)
