import matplotlib.pyplot as plt
import numpy as np
import skimage.io

sq_size = 25;
broj_polja_x = 10

black = np.zeros((sq_size,sq_size))
white = 255*np.ones((sq_size, sq_size))

row1=black
row2=white
for i in range(broj_polja_x-1):
    if i%2==0:
        row1= np.hstack((row1, white))
        row2=np.hstack((row2,black))
    else:
        row1 = np.hstack((row1, black))
        row2 = np.hstack((row2, white))