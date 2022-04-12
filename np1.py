import numpy as np

x = np.array([[1, 2, 3, 4],
             [0, 6, 7, 6], [8, 5, 8, 9], [9, 0, 4, 5]])
print(x.shape)
print(np.zeros([5, 5]))
print(np.ones([5, 5]))
l = range(5)
print(np.arange(7))
print(list(l))

# strings


print(np.char.add(['numpy', 'abc'], ['xyz', 'hi']))
