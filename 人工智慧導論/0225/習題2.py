import numpy as np
import matplotlib.pyplot as plt
import cv2

img = plt.imread("Sword Art Online SAO wallpaper 1.jpg")
img_cv = cv2.imread("Sword Art Online SAO wallpaper 1.jpg")

#plt.imshow(img)

h, w = img_cv.shape[:2]
left_quarter = img_cv[:, :w // 4]
plt.imshow(left_quarter)