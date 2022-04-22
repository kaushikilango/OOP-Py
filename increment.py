import math


def increment_sig(s):
    x = len(s)
    t = 0
    j = []
    while(x > 0):
        t = t + s[x-1]*math.pow(10, x-1)
        x = x - 1
    t = t + 1
    y = list(str(t))
    for k in y:
        j.append(int(k))
    return j
