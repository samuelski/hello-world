import numpy as np
import time

v1 = np.random.rand(1000000)
v2 = np.random.rand(1000000)
v = 0

tic = time.time()
for i in range(1000000):
    v += v1[i] * v2[i]
toc = time.time()
print ("none vector - calculation time" + str((toc - tic)*1000)+"ms"+"\n")

tic = time.time()
v = np.dot(v1, v2)
toc = time.time()

print ("vector-calculation time" + str((toc-tic)*1000)+"ms")

