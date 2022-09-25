import numpy as np
import random

def rand_ints_nodup(a, b, k):
  ns = []
  while len(ns) < k:
    n = random.randint(a, b)
    if not n in ns:
      ns.append(n)
  return ns

rand_num = rand_ints_nodup(0, 24*24-1, 400)

test = np.zeros(24*24, dtype=int)

for i in range(len(test)):
    print(i)
    if i in rand_num:
        test[i] = 1

test2 = test.reshape(24, 24)

for line in test2:
    for dot in line:
        if dot == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()