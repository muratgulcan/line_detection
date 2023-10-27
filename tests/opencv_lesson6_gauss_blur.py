import cv2
import numpy as np

img = cv2.imread('./public/images/image.jpeg') 

gaussian_blur = cv2.GaussianBlur(img, (11, 11), 0)

cv2.imshow('Orginal Image', img)
cv2.imshow('Image with Gauss Blur', gaussian_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
