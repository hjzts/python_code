
# Author hugo
# Time 2023/9/16 21:31
import random

NAMELENGTH = 40
DATAMAXVALUE = 2147483647
NMAX = 20

s = "abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*(){}[]-_=+|\:';<>,."


def randomName():
    name = ""
    n = randomNameLength()
    for i in range(n):
        name = name + random.choice(s)
    return name


def randomNameLength():
    nameLength = random.randint(1, NAMELENGTH - 1)
    return nameLength


def randomId():
    id = random.randint(1, DATAMAXVALUE)
    return id


class Adventurer:
    def __init__(self, advId, advName, bottleArray, equipmentArray):
        self.advId = advId
        self.advName = advName
        self.bottleArray = bottleArray
        self.equipmentArray = equipmentArray


class Bottle:
    def __init__(self, bottleId, bottleName, capacity):
        self.bottleId = bottleId
        self.bottleName = bottleName
        self.capacity = capacity


class Equipment:
    def __init__(self, equipmentId, equipmentName, star):
        self.equipmentId = equipmentId
        self.equipmentName = equipmentName
        self.star = star

    def upgrade(self, star):
        self.star += 1


n = random.randint(1, NMAX)
print(n)
advArray = []

while n:
    n -= 1
    op = random.randint(1, 6)

    if (op == 1):
        # 生成随机
        advId = randomId()
        advName = randomName()
        # adv类的实例入列
        adv = Adventurer(advId, advName, [], [])
        advArray.append(adv)
        # print
        print(str(op) + " " + str(advId) + " " + advName)
    elif (op == 2):
        # 生成随机，再列表中找已经存在的adv实例对象
        arrayLength = len(advArray)
        if arrayLength == 0:
            n += 1
            continue
        index = random.randint(0, arrayLength - 1)
        adv = advArray[index]
        # 得到bot类入列adv中的bottleArray
        botId = randomId()
        botName = randomName()
        capacity = randomId()
        bot = Bottle(botId, botName, capacity)

        print(str(op) + " " + str(adv.advId) + " " + str(botId) + " " + botName + " " + str(capacity))

        adv.bottleArray.append(bot)

    elif (op == 3):
        # 确定随机adv
        arrayLength = len(advArray)
        if arrayLength == 0:
            n += 1
            continue
        index = random.randint(0, arrayLength - 1)
        adv = advArray[index]
        # 确定随机bottle
        bottleLength = len(adv.bottleArray)
        if bottleLength == 0:
            n += 1
            continue
        bottleIndex = random.randint(0, bottleLength - 1)
        bottle = adv.bottleArray[bottleIndex]

        print(str(op)+" "+str(adv.advId) + " " + str(bottle.bottleId))

        adv.bottleArray.pop(bottleIndex)


    elif (op == 4):
        # 生成随机，再列表中找已经存在的adv实例对象
        arrayLength = len(advArray)
        if arrayLength == 0:
            n += 1
            continue
        index = random.randint(0, arrayLength - 1)
        adv = advArray[index]
        # 得到bot类入列adv中的bottleArray
        equId = randomId()
        equName = randomName()
        star = randomId()
        equ = Equipment(equId, equName, star)

        print(str(op) + " " + str(adv.advId) + " " + str(equId) + " " + equName + " " + str(star))

        adv.equipmentArray.append(equ)

    elif (op == 5):
        # 确定随机adv
        arrayLength = len(advArray)
        if arrayLength == 0:
            n += 1
            continue
        index = random.randint(0, arrayLength - 1)
        adv = advArray[index]
        # 确定随机bottle
        equLength = len(adv.equipmentArray)
        if equLength == 0:
            n += 1
            continue
        equIndex = random.randint(0, equLength - 1)
        equ = adv.equipmentArray[equIndex]

        print(str(op)+" "+str(adv.advId) + " " + str(equ.equipmentId))

        adv.equipmentArray.pop(equIndex)

    elif (op == 6):
        # 确定随机adv
        arrayLength = len(advArray)
        if arrayLength == 0:
            n += 1
            continue
        index = random.randint(0, arrayLength - 1)
        adv = advArray[index]
        # 确定随机bottle
        equLength = len(adv.equipmentArray)
        if equLength == 0:
            n += 1
            continue
        equIndex = random.randint(0, equLength - 1)
        equ = adv.equipmentArray[equIndex]

        print(str(op)+" "+str(adv.advId) + " " + str(equ.equipmentId))

        adv.equipmentArray.pop(equIndex)
        equId = equ.equipmentId
        equName = equ.equipmentName
        star = equ.star
        equ1 = Equipment(equId, equName, star + 1)
        adv.equipmentArray.append(equ)
    else:
        pass
