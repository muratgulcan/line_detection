import cv2

# imread -> image read
# 0 -> görseli gray scale olarak import edilmesini sağlar
img = cv2.imread('./public/images/image.jpeg') 

# görseli görselleştirilir ve klavyeden bir tuşa basmadan pencereyi kapama
# imshow -> image show
cv2.imshow("First Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)