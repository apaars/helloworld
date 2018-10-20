import os
import math
import numpy as np
import time

print(os.getcwd())
print(math.isnan(5.575875))
print(math.isnan(np.nan))
start = time.time()
for _ in range(1000):
  _ = list(range(10000))
print(time.time() - start)
# Some pointless comment.
