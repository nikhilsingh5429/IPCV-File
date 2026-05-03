import cv2
from collections import Counter

img = cv2.imread('C:/Users/ASUS/OneDrive/Desktop/download.jpeg', 0)
freq = Counter(img.flatten())
print("Pixel Frequencies:", freq)

