import cv2 as cv
import sys
import numpy as np
import os
import matplotlib.pyplot as plt

path = r"attack_3\\"
image_list = os.listdir(path)
mse_list = []
mse_list_5 = [] 

def mse(img_1,img_2):
    err = np.sum((img_1.astype("float") - img_2.astype("float")) ** 2)
    err /= float(img_1.shape[0]*img_1.shape[1]*img_1.shape[2])
    return err


for i in range(1,len(image_list)):
    img_1 = cv.imread(path+str(i-1)+".png")
    img_2 = cv.imread(path+str(i)+".png")
    error = mse(img_1,img_2)
    mse_list.append(error)

for i in range(5,len(image_list)):
    img_1 = cv.imread(path+str(i-5)+".png")
    img_2 = cv.imread(path+str(i)+".png")
    error_5 = mse(img_1,img_2)
    mse_list_5.append(error_5)

plt.figure(1)
plt.plot(mse_list,'o-')

plt.figure(2)
plt.plot(mse_list_5,'o-')

plt.show()
