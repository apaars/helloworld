import os
import math
import numpy as np
import time

print(os.getcwd())
print(math.isnan(5.50000))  # Taking change from main branch.
print(math.isnan(np.nan))
start = time.time()
for _ in range(1000):
  _ = list(range(10000))
print(time.time() - start)
# Some pointless comment.

# Timing yet another loop.
start = time.time()
for _ in range(1000):
  _ = list(range(1000))
print(time.time() - start)
