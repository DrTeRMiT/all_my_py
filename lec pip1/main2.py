import matplotlib.pyplot as plt
import numpy as np
import random


n = 15
list = []

for i in range(n):
    list.append(random.randint(1, 10))

plt.plot(list)

plt.show()