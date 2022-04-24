def rotate(x):
    f = len(x[0])
    g = [[] for k in range(f)]
    for i in range(0, f):
        for j in range(0, f):
            if (j - (f - 1) < 0):
                m = (j-(f-1)) * -1
            else:
                m = j-(f-1)
            print(i, j)
            g[i].append(x[m][i])
    return g


print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
