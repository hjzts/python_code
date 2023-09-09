import math

def fun(h):
    x = h / (math.tan(1.5 * math.pi / 180) + math.cos(61.5 * math.pi / 180) / (math.cos(1.5 * math.pi / 180) * math.sin(60 * math.pi / 180)))
    return x

h = 207.0
n = 0
x = 0

while h - x * 0.1 * math.tan(1.5 * math.pi / 180) > 13.0:
    n += 1
    x = fun(h)
    x = x / math.cos(61.5 * math.pi / 180) * (math.cos(61.5 * math.pi / 180) + math.cos(58.5 * math.pi / 180))
    h -= (x * 0.9 * math.tan(1.5 * math.pi / 180))

print(n)
print(n * 1852 * 2)
