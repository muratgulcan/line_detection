import cv2
import numpy as np

def median_blur(image, k_size):
    padded_image = cv2.copyMakeBorder(image, k_size//2, k_size//2, k_size//2, k_size//2, cv2.BORDER_CONSTANT)
    result = np.zeros_like(image)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+k_size, j:j+k_size]
            result[i, j] = np.median(region)
            
    return result

# Görüntüyü yükle
img = cv2.imread('./public/images/image.jpeg') 

# Kernel boyutunu belirle
k_size = 50

# Medyan bulanıklaştırma işlemini gerçekleştir
median_blurred_img = median_blur(img, k_size)

# Sonuçları göster
cv2.imshow('Orjinal Görüntü', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Medyan Bulanıklaştırma', median_blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
