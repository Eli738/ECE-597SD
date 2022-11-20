import cv2 as cv
import sys
import numpy as np
import os

image_list = os.listdir(r"sample_set\\")
#fake_img = cv.imread(cv.samples.findFile(r"sample_set\\0.png"))
fake_video = [None]*10
counter = 0

for i in range(len(image_list)):
    img = cv.imread(cv.samples.findFile(r"sample_set\\"+str(i)+".png"))
    if img is None:
        sys.exit("Could not read the image.")

    if i < 10:
        fake_video[i] = img
    # Attack 3
    if (i >=24 and i <30)or(i >=56 and i <66)or(i >=85 and i <100):
        img = fake_video[counter%10]
        counter = counter + 1
        print("fake")

    # Attack 2
    """if ((i in [4,7,13,15,19])or(i >=25 and i <30)or(i >=40 and i <50)or(i >=60 and i <80)):
        img = fake_img
        print("fake")
        """
    # Attack 1
    """if ((i in [4,7,13,15,19])or(i >=25 and i <30)or(i >=40 and i <50)or(i >=60 and i <80)):
        for k in range(312):
            for j in range(412):
                img[k,j] = [255,255,255]
        """

    cv.imwrite(r"attack_3\\"+str(i)+".png", img)
    print("attack_3\\"+str(i)+".png")

