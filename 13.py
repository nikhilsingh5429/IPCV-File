import cv2

img = cv2.imread('C:/Users/ASUS/OneDrive/Desktop/download.jpeg', 0)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Number of boundary points:", len(contours[0]))
