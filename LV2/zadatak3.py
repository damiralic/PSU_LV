from statistics import median
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

mpg=data[:,0]
hp=data[:,3]
wt=data[:,5]
cyl = data[:,1]

print(cyl)

print('Maksimalna potrosnja: ', min(mpg))
print('Minimalna potrosnja: ', max(mpg))
print('Srednja vrijednost', np.mean(mpg))

plt.scatter(mpg,hp,s=wt*80)
plt.xlabel('mpg')
plt.ylabel('hp')
plt.show()