import cv2

image = cv2.imread('C:/Users/ASUS/OneDrive/Desktop/download.jpeg')


if image is None:
    print("Error: Image not found")
else:
   
    cv2.imshow('Acquired Image', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
