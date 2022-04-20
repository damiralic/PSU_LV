import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

mtcars = pd.read_csv('mtcars.csv')

# mtcars.groupby('cyl').mpg.mean().plot.bar()
# plt.show()

# mtcars.boxplot(by='cyl', column='wt')
# plt.show()

# mtcars.boxplot(by='am', column='mpg')
# plt.show()

fig = plt.figure()
ac.scatter(mtcars.am == 0).qsec, mtcars[mtcars.am == 0].hp, label='auto'
ac.scatter(mtcars.am == 1).qsec, mtcars[mtcars.am == 1].hp, label='manual'
plt.show()
