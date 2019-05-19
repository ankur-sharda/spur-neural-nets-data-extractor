import numpy as np

L = [1, 2, 3]

A = np.array([1, 2, 3])

for e in L:
    print(e)

for e in A:
    print(e)

L.append(4)
print(L)

# numpy arrays allow you to do vector operations

L = L + L
print(L)

A = A + A
print(A)

A = A * A
print(A)
