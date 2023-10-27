import cv2
import numpy as np
import matplotlib.pyplot as plt

#Burada 300x400 boyutunda rastgele renkli bir görüntü oluşturarak her bir renk kanalının (mavi, yeşil, kırmızı) histogramını hesaplar ve görselleştirir. Bu örnekte, her renk kanalının histogramı farklı renkte çizdirilmektedir.

# Generate a random color image
random_image = np.random.randint(0, 256, size=(300, 400, 3), dtype=np.uint8)

# Calculate histogram
hist_b = cv2.calcHist([random_image], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([random_image], [1], None, [256], [0, 256])
hist_r = cv2.calcHist([random_image], [2], None, [256], [0, 256])

# Visualize the histogram
plt.figure(figsize=(10,5))
plt.plot(hist_b, color='blue', label='Blue')
plt.plot(hist_g, color='green', label='Green')
plt.plot(hist_r, color='red', label='Red')
plt.title('Renkli Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.xlim([0, 256])
plt.legend(loc='upper right')
plt.show()
