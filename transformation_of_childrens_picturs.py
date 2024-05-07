import cv2
import numpy as np

baby_picture = cv2.imread('images/baby_picture.jpg')
mask_baby_picture = np.zeros(baby_picture.shape, np.uint8)

baby_picture = cv2.GaussianBlur(baby_picture, (9, 9), 0)
baby_picture = cv2.cvtColor(baby_picture, cv2.COLOR_BGR2GRAY)
baby_picture = cv2.Canny(baby_picture, 10, 20)
kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(baby_picture, kernel, iterations=1)
img = cv2.erode(baby_picture, kernel, iterations=1)
con, hir = cv2.findContours(baby_picture, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(con))
cv2.drawContours(mask_baby_picture, con[:225], -1, (255, 0, 0), 1)
cv2.drawContours(mask_baby_picture, con[226:535], -1, (0, 255, 0), 1)
cv2.drawContours(mask_baby_picture, con[536:743], -1, (0, 0, 255), 1)


cv2.imshow('baby picture', mask_baby_picture)
cv2.waitKey(0)
