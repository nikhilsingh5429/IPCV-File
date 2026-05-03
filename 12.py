import cv2
import numpy as np

img = cv2.imread('C:/Users/ASUS/OneDrive/Desktop/download.jpeg', 0)
_, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

cv2.imshow('Threshold Segmentation', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
