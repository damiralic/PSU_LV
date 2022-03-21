import numpy as np
import matplotlib.pyplot as plt

a = []

for i in range(100):
    a.append(np.random.randint(1,7))

labels, count = np.unique(a, return_counts=True)

plt.bar(labels,count)
print(labels,'\n',count)
plt.show()