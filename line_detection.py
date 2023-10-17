import cv2
import numpy as np

# Resmi oku
img = cv2.imread('./public/images/image.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Kenar algılama
edges = cv2.Canny(gray, 50, 150)

# Hough Çizgi Algılama
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=280, maxLineGap=5)

# Çizgileri orijinal resme çiz
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Sonuçları göster
cv2.imshow('Hough Çizgi Algılama', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
