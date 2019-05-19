from __old import learnnumpy as np

a = np.random.randn(5)
print(a)

expa = np.exp(a)
print(expa)

answer = expa / expa.sum()
print(answer)

ansSum = answer.sum()
print(ansSum)

A = np.random.randn(100, 5)
print(A)

expA = np.exp(A)

answer = expA / expA.sum()
answer.sum()
answer = expA / expA.sum(axis=1, keepdims=True)

print(answer)
