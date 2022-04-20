import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

mtcars = pd.read_csv('mtcars.csv')

#print(mtcars.sort_values(by=['mpg']).head(5).car)

#print(mtcars[mtcars.cyl == 8].sort_values(by=['mpg']).tail(3))

#print(mtcars[mtcars.cyl == 6].mpg.mean())

#print(mtcars[(mtcars.cyl == 4) & (mtcars.wt > 2) & (mtcars.wt <2.2)].mpg.mean())

#print(mtcars.value_counts('am'))

#print(len(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)]))

#mtcars['kg'] = mtcars.wt*1000/2.05

#print(mtcars[['car','kg']])