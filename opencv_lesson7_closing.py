import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('./public/images/image2.jpeg', cv2.IMREAD_GRAYSCALE)

# Kernel (structuring element) belirle
kernel = np.ones((5, 5), np.uint8)

# Kapanma işlemi uygula
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Görüntüleri göster
cv2.imshow("Orijinal Görüntü", image)
cv2.imshow("Kapama Sonrası", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()