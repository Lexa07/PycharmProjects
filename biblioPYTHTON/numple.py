#задание1

import numpy as np
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
             [3, 10],
             [1, 7]])
print(a)
print(a.mean())
b = (a[0:, 0])
c = (a[0:, 1])
d = b.mean()
r = c.mean()
mean_a = [d, r]

#задание2

a_centered = a - mean_a

#задание3

a_centered_sp = a_centered[0:, 0] @ a_centered[0:, 1]

print(a_centered_sp)

#задание4

N = a.shape[0]
pol = a_centered_sp / (N - 1)
print(pol)

#Остальное не успел...