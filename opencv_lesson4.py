import cv2
import matplotlib.pyplot as plt

# imread -> image read
# 0 -> görseli gray scale olarak import edilmesini sağlar
img1 = cv2.imread('./public/images/image.jpeg', 0) 
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('./public/images/image2.jpeg', 0) 
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1,(600,600))
print(img1.shape)

img2 = cv2.resize(img2,(600,600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)
plt.show()







