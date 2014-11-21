import math
def numbers(n):
    a = int(n)
    num = (3 + math.sqrt(5))** a
    b = int(num// 1)
    c = list(str(b))
    while len(c) < 3:
        c.insert(0,'0')
    print (c[-3], c[-2], c[-1])
numbers(2)
numbers(5)
numbers(1)
