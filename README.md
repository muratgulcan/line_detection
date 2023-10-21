# OpenCV Notları

OpenCV (Open Source Computer Vision Library), açık kaynaklı bir bilgisayar görüntü işleme kütüphanesidir. OpenCV, özellikle bilgisayar görüşü ve makine öğrenimi uygulamaları için kullanılan bir dizi araç, algoritma ve işlevi içeren bir yazılım kütüphanesidir. Bu kütüphane, bilgisayarlar tarafından işlenen ve anlaşılan görüntülerle ilgilenen birçok projede kullanılır. 

## Temel Özellikler

1. **Görüntü İşleme:** OpenCV, görüntüler üzerinde birçok temel işlemi gerçekleştirmenizi sağlar, örneğin yeniden boyutlandırma, dönme, filtreleme, kesme ve daha fazlası.

2. **Nesne Tanıma ve İzleme:** OpenCV, nesneleri tanıma ve izleme yetenekleri sunar. Bu, nesneleri belirleme, takip etme ve sınıflandırma için kullanılır.

3. **Kamera Kalibrasyonu:** OpenCV, kamera parametrelerini ve konumunu belirlemek için kullanılan araçları içerir. Bu, 3B modellemeye, hareket izleme ve artırılmış gerçeklik uygulamarına katkı sağlar.

4. **Derin Öğrenme ve Makine Öğrenme Entegrasyonu:** OpenCV, özellikle derin öğrenme ve makine öğrenme alanlarında kullanılan bir dizi algoritma ve işlevi içerir. Bu, görüntü sınıflandırma, nesne tespiti, yüz tanıma ve diğer yapay zeka uygulamalarını destekler.

5. **Görüntü Analizi:** OpenCV, görüntüden çıkarılan özellikleri analiz etmek ve nesneleri tanımak için kullanabileceğiniz birçok araç sunar.

6. **Kamera ve Video İşleme:** Kameradan veya video akışından gelen görüntülerle çalışmak için OpenCV işlevleri içerir.

OpenCV, C++, Python, Java ve daha birçok programlama dilinde kullanılabilir ve bu, geliştiricilere farklı platformlarda ve projelerde kolayca kullanma esnekeliği sağlar. OpenCV, araştırma, endüstriyel uygulamalar, otonom araçlar, medikal görüntüleme ve daha birçok alanda yaygın olarak kullanılmaktadır.

## Resmi İçeri Aktarma

Adı üzerinde bir görüntüyü işlemek için görüntüyü Python’a aktarılmasıdır. Bir veri tipi içerisinde depolanması anlamına gelmektedir. Biz bu depolamayı yaptıktan sonra resim ile istediğimiz işlevi yapabilir hale getirilir. `cv2.imread()`, işlevi ilgili fotoğrafın yolunu (path) yazarak konumu belirlenir. Resimler, iki boyuttan oluşan matrislerdir. 

## Şekiller ve Metin

OpenCV’nin bize sunmuş olduğu bir diğer özellik ise görseller üzerine şekiller veya metin eklemektir. Görsellerin üzerine kutucuk şeklinde geometrik çizimler yapılabilir, istenilen boyutlarda istenilen koordinatlara metin eklenebilir. Python’da yapılan örneği ele almak gerekirse:

- `img = np.zeros((512,512,3), np.uint8)`: NumPy kütüphanesi kullanılarak 512x512 boyutunda 3 kanallı (RGB) bir siyah görüntü oluşturur. Sonuç olarak, her pikselin R,G ve B bileşenlerinin sıfır olduğu, siyah bir görüntü oluşturur.
- `cv2.line(img, (0,0),(512,512),(0,255,0), 3)`: Line işlevi ile görsel üzerine bir çizgi çizilebilir. İlk parametresi görselin kendisi, diğerleri sırasıyla başlangıç noktası, bitiş noktası, renk ve kalınlık olmak üzere ilgili değerler verilebilir.
- `cv2.putText(img,"Example", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))`: putText, adından da anlaşılacağı üzere görselin üzerine metin eklememize yardımcı olur. İlgili parametreler sırasıyla ilk olarak görsel, metin, başlangıç noktası, font, kalınlık ve renktir.

## Perspektif Çarpıtma

Bir nesneye belli bir açıda baktığımızda onun ne olduğunu kavrayabiliriz. Aynı nesnenin açısı biraz döndürüldüğünde gördüğümüz nesnenin ufak bir açıyla döndürüldüğünü gözlemleyebiliriz ve bu durumu yadırgamayız çünkü aynı nesne olduğunun bilincinde olmuş oluruz. Söz konusu makineler olunca bu durum biraz farklı işliyor. Makineye bir nesne tanıttığımızda makine o nesneyi algılar ve hafızasına kaydeder fakat aynı nesneyi ufak bir açıyla döndürüp makinenin nesneyi tanımasını istediğimizde makine bunu yeni bir nesneymiş gibi algılar ve istemediğimiz sonuçlar elde ederiz. Bu nedenle görsellerin perspektifini değiştirerek verileri çoğaltmalıyız. 

İlk olarak kolay kısımdan başlanarak nihai görselin boyutu belirlenir:

`width = 400`
`height = 500`

Point1 ve point2 belirleyerek ilgili görselimizin dört köşesinin piksel değerleri olacaktır. Point1 olarak belirlediğimiz değer görselin dört köşesidir ve point2 olarak belirlediğimiz noktalar ise görseli getirmek istediğimiz noktalardır.

`pts1 = np.float32([[25,420],[581,29],[581,418],[24,31]])`
`pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])`

Dönüştürme matrisleri ile son görünüm elde edilir. Bunun için biraz pratik ve mantıkla koordinatlar belirlenir. Hangi noktanın nereye geleceği hesaplamalar sonucu ilgili koordinatların nihai değerleri bulunur.

`matrix = cv2.getPerspectiveTransform(pts1,pts2)`
#nihai görsel
`img_output = cv2.warpPerspective(image,matrix,(width,height))`

## Görüntüleri Birleştirmek

Kimi durumlarda birden fazla görseli tek bir görselde görmek isteyebiliriz. Örneğin; deniz manzaralı bir görselimiz ve çöl manzaralı bir görselimiz var. Bu iki görseli iç içe konumlandırarak tek bir görselde oluşturarak istenilen durumlarda kullanılabilir hale getirilebilir. Yazılıma ilgili fotoğraf dahil edilmesinin ardından görüntüleri birleştirmek için kullanılan ilgili kod alpha, beta ve gamma değerleriyle birlikte şu şekilde yazılır:

`blended = cv2.addWeighted(src1=img1, alpha=0.9, src2=img2, beta=0.1, gamma = 0)`

Alpha, beta ve gamma değerleri duruma göre değiştirilebilir.