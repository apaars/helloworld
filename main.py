import os
import math
import time

print(os.getcwd())
print(math.isnan(5.5))
start = time.time()
for _ in range(1000):
  _ = list(range(10000))
print(time.time() - start)
