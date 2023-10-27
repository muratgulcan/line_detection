import cv2
import matplotlib.pyplot as plt

image = cv2.imread('./public/images/image.jpeg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

plt.figure(figsize=(15,5))
plt.subplot(131), plt.imshow(image, cmap='gray')
plt.title('Orjinal Görüntü'), plt.axis('off')
plt.subplot(132), plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel X'), plt.axis('off')
plt.subplot(133), plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel Y'), plt.axis('off')
plt.show()