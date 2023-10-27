import cv2
import numpy as np

img = cv2.imread('./public/images/image.jpeg') 

median_blur = cv2.medianBlur(img, 15)

cv2.imshow('Orginal Image', img)
cv2.imshow('Image with Median Blur', median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
