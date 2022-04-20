def remove_int(x, i):
    l = 0
    while(l < len(x)):
        if (x[l] == i):
            x.pop(l)
        else:
            l = l + 1
    return(x, len(x))


print(remove_int([0, 1, 2, 2, 3, 0, 4, 2], 2))
