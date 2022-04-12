# Array manipulation changing cells

import numpy as np

x = np.arange(0, 9)
print(x)
print("  ")
b = x.reshape(3, 3)
print(b)
print(b.flatten())
print(b)


z = np.arange(12).reshape(4, 3)
print(z)
print(z.transpose())


y = np.arange(8).reshape(2, 4)
print(y)

print(y.reshape(2, 2, 2))


# numpy arithemetic ops

x1 = np.arange(9).reshape(3, 3)

x2 = np.array([10, 10, 10])

print(x2.shape)
print(np.divide(x1, x2))

# slicing
h = np.arange(20)
print(h[:4:1])


a = np.arange(0, 45, 5)
print(a)
a = a.reshape(3, 3)
for x in np.nditer(a):
    print(x)
