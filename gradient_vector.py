import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fonksiyon tanımı
def f(x, y):
    return x**2 + y**2

# 3D yüzey grafiği
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X Ekseni')
ax.set_ylabel('Y Ekseni')
ax.set_zlabel('Z Ekseni')

plt.show()
