import os
import math
import time

print(os.getcwd())
print(math.isnan(5.50000))  # This change conflicts with change in the `ponies` branch.
start = time.time()
for _ in range(1000):
  _ = list(range(10000))
print(time.time() - start)
# Timing yet another loop.
start = time.time()
for _ in range(1000):
  _ = list(range(1000))
print(time.time() - start)
