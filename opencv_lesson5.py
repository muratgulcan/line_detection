import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./public/images/image.jpeg') 
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()
