import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('C:/Users/ASUS/OneDrive/Desktop/download.jpeg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0, 120, 70])
upper = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
segmented = cv2.bitwise_and(img, img, mask=mask)
plt.subplot(1,2,1); plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); plt.title('Original'); plt.axis('off')
plt.subplot(1,2,2); plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB)); plt.title('Segmented'); plt.axis('off')
plt.show()
