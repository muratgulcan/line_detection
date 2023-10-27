import cv2
import numpy as np

# Mouse tıklama eventini işleyen fonksiyon
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Koordinatlar: ({x}, {y})")

# Boş bir siyah 512x512 görüntü oluştur
image = cv2.imread('./public/images/image2.jpeg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
width = 400
height = 500

pts1 = np.float32([[580,28],[583,408],[25,32],[24,31]])
pts2 = np.float32([[0,0],[width,height],[width,0],[0, height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

#nihai dönüştürülmüş görsel
img_output = cv2.warpPerspective(image,matrix,(width,height))

# Pencereyi aç
cv2.namedWindow('Image')

# Mouse eventini bağla
cv2.setMouseCallback('Image', mouse_callback)

while True:
    cv2.imshow('Image', img_output)

    # Eğer 'q' tuşuna basılırsa döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Pencereyi kapat
cv2.destroyAllWindows()
