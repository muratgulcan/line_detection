import cv2 
import numpy as np

# görsel oluştur
img = np.zeros((512,512,3), np.uint8)

# çizgi
# line(görsel, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (0,0),(512,512),(0,255,0), 3) 

# dikdörtgen 
# rectangle(görsel, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.rectangle(img, (100,100),(256,256),(255,0,0),3)

# metin
# putText(görsel, metin, başlangıç noktası, yazı tipi(font), yazı kalınlığı, renk)
cv2.putText(img,"Example", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

