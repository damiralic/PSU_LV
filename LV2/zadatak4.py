import matplotlib.pyplot as plt
import numpy as np
import skimage.io

img = skimage.io.imread('tiger.png', as_gray=True)
brightness_img = img.copy()
rows, cols = img.shape
black_img = np.zeros((rows, cols))
resize_img = np.zeros((int(rows/10), int(cols/10)))
turn_img = np.zeros((cols, rows))
mirror_img = np.zeros((rows, cols))
check = cols/4

for i in range(rows):
    for j in range(cols):
        turn_img[j][rows-1-i]=img[i][j]

for i in range(rows):
    for j in range(cols):
        if(img[i,j] > 205):
            brightness_img[i,j] = 255
        else:
            brightness_img[i,j] += 50

for i in range(cols):
    mirror_img[:,i]=img[:,cols-1-i]


for i in range(0,rows,10):
    for j in range(0,cols,10):
        resize_img[int(i/10),int(j/10)] = img[i,j]

for i in range(cols):
    if i>(check-1) and i<((2*check)-1):
        black_img[:,i] = img[:,i]

plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.figure(2)
plt.imshow(brightness_img, cmap='gray', vmin=0, vmax=255)
plt.figure(3)
plt.imshow(turn_img, cmap='gray', vmin=0, vmax=255)
plt.figure(4)
plt.imshow(mirror_img, cmap='gray', vmin=0, vmax=255)
plt.figure(5)
plt.imshow(resize_img, cmap='gray', vmin=0, vmax=255)
plt.figure(6)
plt.imshow(black_img, cmap='gray', vmin=0, vmax=255)
plt.show()