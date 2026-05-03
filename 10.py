import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/ASUS/OneDrive/Desktop/download.jpeg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title('Original'); plt.axis('off')
plt.subplot(1,2,2); plt.imshow(edges, cmap='gray'); plt.title('Edges'); plt.axis('off')
plt.show()
