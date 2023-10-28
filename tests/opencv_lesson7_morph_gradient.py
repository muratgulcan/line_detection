import cv2
import numpy as np

image = cv2.imread('./public/images/image.jpeg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)

dilated = cv2.dilate(image, kernel, iterations=1)

eroded = cv2.erode(image, kernel, iterations=1)

gradient = cv2.absdiff(dilated,eroded)

cv2.imshow("Orginal Image", image)
cv2.imshow("Morfolojik Gradyan", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()