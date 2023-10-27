import cv2
import numpy as np

img = cv2.imread('./public/images/image.jpeg') 

mean_blur = cv2.blur(img, (5, 5))

cv2.imshow('Orginal Image', img)
cv2.imshow('Image with Mean Blur', mean_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
