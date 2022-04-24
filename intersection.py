def find_unique(x):
    for m in x:
        g[m] = 0
    print(g)
    for i in x:
        g[i] = g[i] + 1
        if g[i] > 1:
            return False
    return True


c = [1, 2, 3, 4, 5, 6]
g = {}
print(find_unique(c))
