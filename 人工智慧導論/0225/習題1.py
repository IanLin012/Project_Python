import numpy as np
import matplotlib.pyplot as plt
import cv2

img = plt.imread("Sword Art Online SAO wallpaper 1.jpg")
img_cv = cv2.imread("Sword Art Online SAO wallpaper 1.jpg")

plt.imshow(img)

# original(RGB) -> Grayscale, HSV, CMYK, YUV
cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
plt.imshow(img_cv)