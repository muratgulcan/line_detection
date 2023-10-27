import cv2
import numpy as np

image = np.zeros((300,300), dtype="uint8")
cv2.circle(image,(150,150),100,255,-1)

contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
background = np.zeros((300,300,3), dtype="uint8")
cv2.drawContours(background,contours, -1, (0,255,0), thickness=2)

cv2.imshow("Nesne Konturu", background)
cv2.waitKey(0)
cv2.destroyAllWindows()