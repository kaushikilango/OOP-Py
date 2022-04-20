def movezeroes(x):
    m = 0
    while(m < len(x)):
        if(x[m] == 0):
            x.append(x.pop(m))
    return x
