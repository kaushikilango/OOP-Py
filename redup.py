def redup(x):
    set = 0
    i = 0
    j = len(x)
    while(i != len(x)):
        if(x[i-1] == x[i] and i != 0):
            x.pop(i)
        else:
            i = i + 1
        print(x)
    x = x + [0]*j
    return x


print(redup([0, 0, 0, 1, 1, 2, 3, 4, 4, 5, 5, 5]))
