import numpy as np
import matplotlib.pyplot as plt

def draw_zebra_pattern(width, height, black_width, white_width):
    # Boş bir resim oluşturun
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    total_width = black_width + white_width -4
    print(black_width)
    num_stripes = width // total_width
    
    # Dikey çizgileri ekleyin
    for i in range(num_stripes):
        if i % 2 == 0:
            image[:, i*total_width : i*total_width + black_width] = [0, 0, 0]
    
    return image

# Kullanıcıdan giriş al
width = 1920
height = 1080
black_width = int(input("Siyah çizgi genişliği: "))
white_width = int(input("Beyaz çizgi genişliği: "))

# Zebra desenini oluştur
zebra_pattern = draw_zebra_pattern(width, height, black_width, white_width)

# Resmi göster
plt.imshow(zebra_pattern)
plt.axis('off')
plt.show()

# Resmi kaydetmek isterseniz aşağıdaki kodu kulla1.5nabilirsiniz
plt.imsave(f'{black_width}B{white_width}W_test.png', zebra_pattern)
