import numpy as np
import time
import sys
b = range(1000)
print(sys.getsizeof(5)*len(b))
print(sys.getsizeof(1000))
a = np.arange(0, 100000)
print(a.size * a.itemsize)
print(a.size)
print(a.itemsize)
x1 = [1, 2, 3, 4, 5]
x2 = ['a', 'b', 'c', 'd']
print(list(zip(x1, x2)))

size = 1000000

l1 = range(size)
l2 = range(size)
start = time.time()
result = [(x+y) for x, y in zip(l1, l2)]
print(f'python list took{time.time() - start}')

a1 = np.arange(size)
a2 = np.arange(size)
start = time.time()
result = a1 + a2
print(f'Numpy array{time.time() - start}')
