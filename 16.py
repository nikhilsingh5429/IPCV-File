import cv2
import numpy as np
img = cv2.imread('C:/Users/ASUS/OneDrive/Desktop/download.jpeg', 0)
values, counts = np.unique(img, return_counts=True)
prob = counts / counts.sum()
print("Symbol Probabilities:", prob)
