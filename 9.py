import cv2
import numpy as np
from collections import Counter
import heapq

img = cv2.imread('C:/Users/ASUS/OneDrive/Desktop/download.jpeg', 0)
flat = img.flatten()

# Run Length Encoding
rle = []
prev = flat[0]
count = 1
for pixel in flat[1:]:
    if pixel == prev:
        count += 1
    else:
        rle.append((prev, count))
        prev = pixel
        count = 1
rle.append((prev, count))

print("Original size:", len(flat))
print("RLE size:", len(rle))
