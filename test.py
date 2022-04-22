x = [43, 21, 25, 42, 57, 59, 247]  # assuming last value to be test set
y = [99, 65, 79, 75, 87, 81, 486]  # assuming last value to be test set
xi = 247
sigmaxy = 0
for i in range(0, len(x) - 1):
    sigmaxy = sigmaxy + (x[i] * y[i])
f = len(x) - 1
sigmax = sum(x[:-1])
sigmay = sum(y[:-1])
sigmax2 = sum([i*i for i in x[:-1]])
sigmay2 = sum([i*i for i in x[:-1]])
a = ((sigmay*sigmax2) - (sigmax * sigmaxy)) / \
    (f * (sigmax2) - (sigmax * sigmax))
b = ((f * sigmaxy) - (sigmax * sigmay)) / ((f * sigmax2) - (sigmax * sigmax))
print(b)
print(a)
yi = a + (b*xi)

print(yi)
print(sigmax2)
