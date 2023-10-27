import cv2
import numpy as np

image = cv2.imread('./public/images/image2.jpeg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)
eroded = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Orjinal Görüntü", image)
cv2.imshow("Erozyon Sonrası", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()