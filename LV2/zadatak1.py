import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,3,3,2,1], float)
b = np.array([1,1,2,2,1], float)
plt.xlim(0,4)
plt.ylim(0,4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Zadatak 1')
plt.plot(a,b, 'b-', linewidth=2, marker='o')
plt.show()