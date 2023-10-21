import cv2
import matplotlib.pyplot as plt

# imread -> image read
# 0 -> görseli gray scale olarak import edilmesini sağlar
img1 = cv2.imread('./public/images/image.jpeg', 0) 
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('./public/images/image2.jpeg', 0) 
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

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

# karıştırılmış resim = alpha * img1 + beta * img2
blended = cv2.addWeighted(src1=img1, alpha=0.9, src2=img2, beta=0.1, gamma = 0)
plt.figure()
plt.imshow(blended)

plt.show()







