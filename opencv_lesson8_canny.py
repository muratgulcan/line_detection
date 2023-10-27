import cv2
import matplotlib.pyplot as plt

image = cv2.imread('./public/images/image.jpeg', cv2.IMREAD_GRAYSCALE)

edges_canny = cv2.Canny(image,100,200)

plt.figure(figsize=(10,5))
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Orjinal Görüntü'), plt.axis('off')
plt.subplot(122), plt.imshow(edges_canny, cmap='gray')
plt.title('Canny Kenar Dedektörü'), plt.axis('off')
plt.show()