# Author hugo
# Time 2023/7/30 18:19
import calc2
print(calc2.add(100,200))
import sys
import time
import urllib.request
import math
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.hugohealthy.top').read())

print(math.pi)
print(math.e)

import schedule

def job():
    print('哈哈------------')
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)