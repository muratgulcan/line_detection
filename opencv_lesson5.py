import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./public/images/image.jpeg') 
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

#threshold (eşikleme)
_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()