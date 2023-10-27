# OpenCV Notları

## İçindekiler

1. [Temel Özellikler](#temel-ozellikler)
2. [Resmi İçeri Aktarma](#resmi-iceri-aktarma)
3. [Şekiller ve Metin](#sekiller-metin)
4. [Renk Uzayları ve Kanallar](#renk-uzaylari-kanallar)
5. [Perspektif Çarpıtma](#perspektif-carpitma)
5. [Görüntüleri Birleştirmek](#goruntuleri-birlestirmek)
6. [Görüntü Eşikleme](#image-thresholding)
7. [Görüntü Bulanıklaştırma](#goruntu-bulaniklastirma)
8. [Morfolojik Operasyonlar](#morfolojik-operasyonlar)
9. [Histogram Analizi](#histogram-analysis)
9. [Kenar Tespiti ve İzleme](#edge-detection)

OpenCV (Open Source Computer Vision Library), açık kaynaklı bir bilgisayar görüntü işleme kütüphanesidir. OpenCV, özellikle bilgisayar görüşü ve makine öğrenimi uygulamaları için kullanılan bir dizi araç, algoritma ve işlevi içeren bir yazılım kütüphanesidir. Bu kütüphane, bilgisayarlar tarafından işlenen ve anlaşılan görüntülerle ilgilenen birçok projede kullanılır. 

<a id="temel-ozellikler"></a>

## Temel Özellikler

1. **Görüntü İşleme:** OpenCV, görüntüler üzerinde birçok temel işlemi gerçekleştirmenizi sağlar, örneğin yeniden boyutlandırma, dönme, filtreleme, kesme ve daha fazlası.

2. **Nesne Tanıma ve İzleme:** OpenCV, nesneleri tanıma ve izleme yetenekleri sunar. Bu, nesneleri belirleme, takip etme ve sınıflandırma için kullanılır.

3. **Kamera Kalibrasyonu:** OpenCV, kamera parametrelerini ve konumunu belirlemek için kullanılan araçları içerir. Bu, 3B modellemeye, hareket izleme ve artırılmış gerçeklik uygulamarına katkı sağlar.

4. **Derin Öğrenme ve Makine Öğrenme Entegrasyonu:** OpenCV, özellikle derin öğrenme ve makine öğrenme alanlarında kullanılan bir dizi algoritma ve işlevi içerir. Bu, görüntü sınıflandırma, nesne tespiti, yüz tanıma ve diğer yapay zeka uygulamalarını destekler.

5. **Görüntü Analizi:** OpenCV, görüntüden çıkarılan özellikleri analiz etmek ve nesneleri tanımak için kullanabileceğiniz birçok araç sunar.

6. **Kamera ve Video İşleme:** Kameradan veya video akışından gelen görüntülerle çalışmak için OpenCV işlevleri içerir.

OpenCV, C++, Python, Java ve daha birçok programlama dilinde kullanılabilir ve bu, geliştiricilere farklı platformlarda ve projelerde kolayca kullanma esnekeliği sağlar. OpenCV, araştırma, endüstriyel uygulamalar, otonom araçlar, medikal görüntüleme ve daha birçok alanda yaygın olarak kullanılmaktadır.

<a id="resmi-iceri-aktarma"></a>

## Resmi İçeri Aktarma

Adı üzerinde bir görüntüyü işlemek için görüntüyü Python’a aktarılmasıdır. Bir veri tipi içerisinde depolanması anlamına gelmektedir. Biz bu depolamayı yaptıktan sonra resim ile istediğimiz işlevi yapabilir hale getirilir. `cv2.imread()`, işlevi ilgili fotoğrafın yolunu (path) yazarak konumu belirlenir. Resimler, iki boyuttan oluşan matrislerdir. 

<a id="sekiller-metin"></a>

## Şekiller ve Metin

OpenCV’nin bize sunmuş olduğu bir diğer özellik ise görseller üzerine şekiller veya metin eklemektir. Görsellerin üzerine kutucuk şeklinde geometrik çizimler yapılabilir, istenilen boyutlarda istenilen koordinatlara metin eklenebilir. Python’da yapılan örneği ele almak gerekirse:

- `img = np.zeros((512,512,3), np.uint8)`: NumPy kütüphanesi kullanılarak 512x512 boyutunda 3 kanallı (RGB) bir siyah görüntü oluşturur. Sonuç olarak, her pikselin R,G ve B bileşenlerinin sıfır olduğu, siyah bir görüntü oluşturur.
- `cv2.line(img, (0,0),(512,512),(0,255,0), 3)`: Line işlevi ile görsel üzerine bir çizgi çizilebilir. İlk parametresi görselin kendisi, diğerleri sırasıyla başlangıç noktası, bitiş noktası, renk ve kalınlık olmak üzere ilgili değerler verilebilir.
- `cv2.putText(img,"Example", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))`: putText, adından da anlaşılacağı üzere görselin üzerine metin eklememize yardımcı olur. İlgili parametreler sırasıyla ilk olarak görsel, metin, başlangıç noktası, font, kalınlık ve renktir.

<a id="renk-uzaylari-kanallar"></a>

## Renk Uzayları ve Kanallar

Renk uzayları ve kanallar, görüntülerin renklerini temsil etmek için kullanılan matematiksel modellerdir. Her bir renk uzayı, renk bilgisini farklı şekillerde temsil eder ve belirli uygulamalarda faydalı olabilmektedir.

**1. RGB (Red, Green, Blue):** RGB renk uzayı, en yaygın olarak kullanılan renk uzaylarından biridir. Her piksel, kırmızı, yeşil ve mavi bileşenlerin bir kombinasyonuyla temsil edilir. Kırmızı (R), Yeşil (G) ve Mavi (B) kanallar, her birinin 0 ile 255 arasında değer alabileceği bir renk bileşenini temsil eder.

**2. HSV (Hue, Saturation, Value):** HSV renk uzayı, rengin, doygunluğun ve parlaklığın ayrı ayrı temsil edildiği bir renk uzayıdır. Hue (H), rengi temsil eder ve 0 ila 360 arasında bir değere sahip olabilir. (Genellikle açısal bir ölçekle ifade edilir.) Saturation (S), rengin doygunluğunu temsil eder ve 0 ila 1 arasında bir değere sahip olabilir. Value (V), rengin parlaklığını temsil eder ve yine 0 ila 1 arasında bir değere sahip olabilir.

**3. Lab (CIE 1976 Lab):** Lab renk uzayı, insan gözünün renk algısını daha iyi temsil etmek üzere tasarlanmıştır. L*, a*, b* kanalları vardır. L* (luma) değeri parlaklığı temsil ederken, a* ve b* değerleri renklerin yeşil-kırmızı ve mavi-sarı arasındaki renk değişimini temsil eder.

**4. CMY ve CMYK:** CMY renk modeli, Siyah (Black) kanalını eklemeksizin Sian, Magenta ve Yellow renklerini karıştırarak diğer renkleri üretmeye çalışır. CMYK modeli ise Siyah (Black) kanalını ekler.

Bu renk uzayları ve kanalları, farklı renk manipülasyonları, renk analizi ve renk tabanlı işlemler için kullanılır. Örneğin, renk filtreleme, nesne tespiti, görüntü eşitleme gibi birçok uygulamada faydalı olabilirler.

<a id="perspektif-carpitma"></a>

## Perspektif Çarpıtma

Bir nesneye belli bir açıda baktığımızda onun ne olduğunu kavrayabiliriz. Aynı nesnenin açısı biraz döndürüldüğünde gördüğümüz nesnenin ufak bir açıyla döndürüldüğünü gözlemleyebiliriz ve bu durumu yadırgamayız çünkü aynı nesne olduğunun bilincinde olmuş oluruz. Söz konusu makineler olunca bu durum biraz farklı işliyor. Makineye bir nesne tanıttığımızda makine o nesneyi algılar ve hafızasına kaydeder fakat aynı nesneyi ufak bir açıyla döndürüp makinenin nesneyi tanımasını istediğimizde makine bunu yeni bir nesneymiş gibi algılar ve istemediğimiz sonuçlar elde ederiz. Bu nedenle görsellerin perspektifini değiştirerek verileri çoğaltmalıyız. 

İlk olarak kolay kısımdan başlanarak nihai görselin boyutu belirlenir:

```
width = 400
height = 500
```

Point1 ve point2 belirleyerek ilgili görselimizin dört köşesinin piksel değerleri olacaktır. Point1 olarak belirlediğimiz değer görselin dört köşesidir ve point2 olarak belirlediğimiz noktalar ise görseli getirmek istediğimiz noktalardır.

```
pts1 = np.float32([[25,420],[581,29],[581,418],[24,31]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
```

Dönüştürme matrisleri ile son görünüm elde edilir. Bunun için biraz pratik ve mantıkla koordinatlar belirlenir. Hangi noktanın nereye geleceği hesaplamalar sonucu ilgili koordinatların nihai değerleri bulunur.

```
matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_output = cv2.warpPerspective(image,matrix,(width,height))
```

<a id="goruntuleri-birlestirmek"></a>

## Görüntüleri Birleştirmek

Kimi durumlarda birden fazla görseli tek bir görselde görmek isteyebiliriz. Örneğin; deniz manzaralı bir görselimiz ve çöl manzaralı bir görselimiz var. Bu iki görseli iç içe konumlandırarak tek bir görselde oluşturarak istenilen durumlarda kullanılabilir hale getirilebilir. Yazılıma ilgili fotoğraf dahil edilmesinin ardından görüntüleri birleştirmek için kullanılan ilgili kod alpha, beta ve gamma değerleriyle birlikte şu şekilde yazılır:

```
blended = cv2.addWeighted(src1=img1, alpha=0.9, src2=img2, beta=0.1, gamma = 0)
```

Alpha, beta ve gamma değerleri duruma göre değiştirilebilir.

<a id="image-thresholding"></a>

## Görüntü Eşikleme (Image Thresholding)

OpenCV'de görüntü eşikleme(image thresholding), bir gri tonlu veya renkli görüntüdeki pikselleri belirli bir eşik değeriyle karşılaştırarak, bu değeri geçen pikselleri belirli bir değere ayarlayarak veya belirli bir değere göre işleyerek görüntüyü sadeleştiren bir işlemdir.

Görüntü eşikleme işlemi, nesne algılama, nesne ayırma ve görüntü analizi gibi birçok uygulamada kullanılır. Örneğin, kenar tespiti, nesne tanıma veya nesne sayma gibi işlemlerde yaygın olarak kullanılır.
Görüntü eşikleme işleminin amacı, görüntüdeki önemli özellikleri (örneğin kenarlar veya nesneler) belirginleştirmek veya diğer işlemler için veriyi hazırlamaktır.

Görüntü işlemede görselleri gri tona çevirmenin birkaç sebebi vardır ve bu durumlarla ilgili ufak bir not paylaşmak gerekirse:

* **İşlem Hızı:** Renkli görüntüler daha fazla veri içerir (her piksel için 3 renk kanalı: kırmızı, yeşil, mavi). Gri tonlu görüntüler sadece bir kanala sahiptir. Bu nedenle, gri tonlu görüntülerin işlenmesi genellikle daha hızlıdır.
* **Bellek ve Depolama Verimliliği:** Bir önceki sebebe istinaden, daha az veri demek az depolama alanı demektir. Gri tonlu görüntüler, renkli görüntülere göre daha az bellek ve depolama alanı gerektirir.
* **Yeterli Bilgi:** Birçok durumda, rengin tamamıyla ilgili değil, sadece ışık yoğunluğuyla ilgilenilir. Örneğin, kenar algılama veya görüntü eşikleme gibi birçok temel görüntü işleme tekniği, renk bilgisine ihtiyaç duymaz.
* **Azaltılmış Gürültü:** Renkli görüntüler genellikle daha fazla gürültüye sahiptir. Gri tonlu formata dönüştürmek, bu gürültünün bir kısmını azaltabilir.
* **Sadeleştirme:** Bazı analizler ve algoritmalar için, sadece ışık yoğunluğu bilgisinin kullanılması daha anlamlıdır.

Ancak, renk bilgisinin önemli olduğu durumlarda (örneğin, nesne tanıma veya renk analizi gibi uygulamalarda), renkli görüntü formunu kullanmak gerekebilir. Bu durumda, renk dönüşümü (örneğin, BGR'den RGB'ye veya RGB'den HSV'ye) işlemleri kullanılır.

Örnek kod üzerinden ilerleyecek olursak:
```
img = cv2.imread('./public/images/image.jpeg') 
#cv2.cvtColor fonksiyonunu kullanarak görüntüyü renkli (BGR) formatından gri tonlu formata dönüştürür. Böylece, img değişkenimiz artık bir gri tonlu görüntüdür.
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure()
#img değişkenini gri tonlu görüntüyü matplotlib ile gösterir. cmap="gray" argümanı, görüntünün gri tonlamasının doğru bir şekilde gösterilmesini sağlar.
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

#threshold
_, thresh_img = cv2.threshold(img, thresh=80, maxval=255, type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()
```

`_, thresh_img: cv2.threshold`: döndürdüğü iki değer vardır. Birincisi, kullanılan eşik değeri ve ikincisi eşiklenmiş görüntü (thresh_img). Birinci değeri (_) genellikle kullanılmaz, bu nedenle genellikle alt çizgi (_) ile gösterilir. Eşiklenmiş görüntü, thresh_img değişkenine atanır ve bu işlem sonucu bu görüntüye erişebilirsiniz. 

`thresh=80`: Eşik değeri olarak kullanılacak sayı. Bu değer, piksellerin gri ton seviyelerini temsil eder. Eşik değerinden küçük olan pikseller 0 (siyah) olarak ayarlanır, eşik değerinden büyük olanlar ise maxval değeri olarak ayarlanır.

`maxval=255`: Eşik değerini geçen piksellerin alacağı maksimum değer. Yani, eşik değerini geçen pikseller bu değere ayarlanır. Bu genellikle 255 olarak ayarlanır, çünkü bu değer en parlak değeri temsil eder (beyaz).

`type=cv2.THRESH_BINARY`: Bu, eşikleme türünü belirtir. `cv2.THRESH_BINARY`, eşik değerini geçen pikselleri maxval değerine ayarlar, geçmeyenleri ise 0'a ayarlar. Yani, eşiklemeden sonra sadece siyah ve beyaz pikseller olur.

<a id="goruntu-bulaniklastirma"></a>

## Görüntü Bulanıklaştırma (Image Blurring)

Görüntü bulanıklaştırma, bir görüntünün üzerindeki detayları yumuşatarak ve piksel değerlerini düzenleyerek, görüntüdeki gürültüyü azaltmak veya önemli özellikleri vurgulamak için kullanılan bir işlemdir. Bu işlem, görüntü işleme uygulamalarında yaygın olarak kullanılır.

Görüntü bulanıklaştırma, bir filtre kullanarak gerçekleştirilir. Bu filtre, belirli bir pikselin değerini hesaplamak için çevresindeki piksellerin bilgilerini kullanır. Farklı filtre türleri, farklı bulanıklık etkileri oluşturur.

Görüntü işlemede görüntü bulanıklaştırma türleri şu şekilde sıralanabilir:

### Ortalama Bulanıklaştırma (Mean Blurring)

Ortalama Bulanıklaştırma (Mean Blurring), bir görüntünün her pikselini belirli bir bölge içindeki diğer piksellerin ortalamasıyla değiştirerek görüntüyü yumuşatma işlemidir. Bu işlem, bir pikselin değerini çevresindeki piksellerin ortalaması ile değiştirerek çalışır. Bu bulanıklaştırmanın algoritması şu şekildedir:

1. Görüntünün her pikseli için, belirli bir bölge (örneğin, bir kutu veya bir çekirdek) seçilir.
2. Seçilen bölge içindeki piksellerin değerlerinin toplamı alınır.
3. Bu toplam, bölgenin alanına bölünerek ortalaması hesaplanır.
4. Ortalama değer, pikselin yeni değeri olarak atanır.

Bu işlem, görüntüdeki gürültüyü azaltmak için etkilir çünkü her piksel, çevresindeki piksellerin değerlerinin ortalaması ile temsil edilir. Bu sayede, tek pikselin anormal değerleri veya gürültü, ortalamaya karıştırılır ve sonuçta daha yumuşak bir görüntü elde edilir. Örnek olarak 3x3 bir ortalamaya alma işlemi düşünelim. Bu durumda her piksel, kendisi ve çevresindeki 8 piksel değerlerinin ortalaması ile değişir. Bu işlem, pikselin etrafındaki küçük bir bölgeyi dikkate alarak çalışır. 

### Gauss Bulanıklaştırma (Gauss Blurring)

Gauss bulanıklaştırma, bir görüntünün her pikselini çevresindeki piksellerin ağırlıklı ortalaması ile değiştirerek görüntüyü yumuşatma işlemidir. Bu ağırlıklar, Gauss fonksiyonunun değerleridir ve merkez piksele olan uzaklık ile belirlenir. Bu sayede, daha fazla ağırlık verilen piksellerin, merkez pikselin değerini daha fazla etkilemesi sağlanır. Dolayısıyla her pikselin değerini hesaplamak için bir Gauss fonksiyonu kullanır.

Algoritmanın adımları:

1. Görüntünün her pikseli için, belirli bir bölge (örneğin, bir kutu veya bir çekirdek) seçilir. Bu bölge genellikle simetrik bir şekilde olur.
2. Seçilen bölge içindeki her pikselin değeri, bir Gauss fonksiyonu tarafından belirlenen ağırlıklarla çarpılarak toplanır.
3. Bu toplam, bölgenin alanına bölünerek ağırlıklı ortalaması hesaplanır.
4. Ağırlıklı ortalama değer, pikselin yeni değeri olarak atanır.

### Medyan Bulanıklaştırma (Median Blurring)

Medyan bulanıklaştırma, bir görüntünün her pikselini belirli bir bölge içindeki piksellerin medyan değeri ile değiştirerek görüntüyü yumuşatma işlemidir. Medyan, sıralanmış değerlerin ortasındaki değeri temsil eder. Bu bulanıklaştırmanın algoritması ise şu şekildedir:

1. Görüntünün her pikseli için, belirli bir bölge (örneğin, bir kare veya bir çekirdek) seçilir. Bu bölge genellikle simetrik bir şekildedir.
2. Seçilen bölgedeki piksellerin değerleri sıralanır.
3. Sıralı piksel değerleri arasındaki ortanca (yani, ortadaki değer) seçilir.
4. Ortanca değer, pikselin yeni değeri olarak atanır.

Ortalama, Gauss ve Medyan Bulanıklaştırma yöntemlerinin aralarındaki farkı inceleyecek olursak:
| Özellik | Medyan Bulanıklaştırma | Gauss Bulanıklaştırma | Ortalama Bulanıklaştırma |
| --- | --- | --- | --- |
| Temel İlke | Piksellerin medyanı ile değiştirilir. | Ağırlıklı ortalama ile değiştirilir. | Piksellerin aritmetik ortalaması ile değiştirilir. |
| Gürültü Azaltma | Etkili, gürültüyü azaltmada başarılıdır. | Etkili, gürültüyü azaltır ancak medyan yöntemi kadar etkili değildir. | Düzeltici, ancak gürültüyü tam olarak azaltmada diğerlerine göre daha az etkilidir. |
| Hesaplama Zamanı | Daha yavaş, özellikle büyük bölgelerde daha yavaş olabilir. | Daha hızlıdır, Gauss filtresi için hızlı hesaplama yöntemleri mevcuttur. | Hızlıdır, ortalama işlemi basit bir toplama işlemidir. |
| Hassasiyet | Daha yüksek, aykırı değerlerin etkisini azaltır. | Orta, gürültüyü azaltır ancak medyan yöntemi kadar iyi değil. | Düşük, gürültüyü azaltır ancak diğer yöntemlere göre daha az etkilidir. |
| Kullanım Alanları | Tıbbi görüntüleme, kenar tespiti, gürültü azaltma gibi uygulamalarda yaygın olarak kullanılır. | Doğal görüntü işlemede, yumuşak ve doğal görüntü bulanıklaştırma için tercih edilir. | Gürültü azaltma, keskin kenarları koruma ihtiyacı olmayan genel uygulamalarda yaygın olarak kullanılır. |
| Köşeler ve Detaylar | Köşeleri ve detayları korur, daha iyi kenar algılar. | Kenarlara daha az etki eder, detayları biraz kaybedebilir. | Kenarlara daha az etki eder, detayları daha fazla kaybedebilir. |
| Etki Süresi | Daha kısa, keskin kenarlar korunur. | Orta, gürültü azaltma sağlar. | Daha uzun, keskin kenarlar kaybolabilir. |
| Gauss Ağırlıkları | Gauss fonksiyonunun ağırlıklarını kullanmaz. | Gauss fonksiyonunun ağırlıklarını kullanır. | Eşit ağırlıklar kullanır. |
| Parlak ve Açık Alanlar | Parlak ve açık alanlarda daha etkilidir. | Orta seviyede etkilidir. | Daha etkisiz, parlak alanlarda daha az etkilidir. |
| Büyük Gürültü | Büyük gürültü durumlarında etkili olabilir. | Büyük gürültüyü azaltmakta sınırlıdır. | Büyük gürültüyü azaltmada etkili değildir. |
| Çözünürlük Kaybı | Daha az çözünürlük kaybı yaşanır. | Orta düzeyde çözünürlük kaybı yaşanır. | Daha fazla çözünürlük kaybı yaşanır. |

**Not:** **Kernel boyutu**, görüntü işleme filtrelerinde kullanılan bir matrisin boyutunu belirtir. Bu matris, bir pikselin değerini hesaplamak için çevresindeki piksellerin değerlerini kullanır.

Örneğin, 3x3 boyutunda bir kernel, bir pikselin etrafındaki 3x3 pikselin değerlerini kullanarak işlem yapar. 5x5 boyutunda bir kernel, 5x5 pikselin değerlerini kullanır ve benzer şekilde çalışır.

Kernel boyutu, belirli bir uygulamanın gereksinimlerine ve görüntünün özelliklerine bağlı olarak seçilir. Genellikle, daha büyük bir kernel daha fazla komşu pikselin değerini dikkate alır ve daha yumuşak bir sonuç üretir fakat bu aynı zamanda işlemin daha yavaş çalışmasına neden olabilir.

Bu değerler, uygulamanın gereksinimlerine bağlı olarak değişebilir. Daha büyük kernel boyutları, daha fazla komşu pikselin değerini dikkate alarak daha fazla bulanıklaştırma sağlar fakat işlem süresi artabilir.

**Nesne konturu**, bir görüntüdeki nesnenin sınırlarını belirten çizgidir. Yani nesnenin dış hatlarını oluşturan bir çizgidir. Bu kontu, nesnenin dış yüzeyinin bir özeti olarak düşünülebilir. Örneğin, bir siyah arkaplan üzerinde beyaz bir daire resmi düşünelim. Bu durumda, dairenin dış hatlarının dairenin çevresini çizen çizgidir. 

<a id="morfolojik-operasyonlar"></a>

## Morfolojik Operasyonlar

OpenCV'de morfolojik operasyonlar, görüntüler üzerinde şekil ve yapı değişikliklerini gerçekleştiren temel işlemlerdir. Bu operasyonlar genellikle ikili (siyah-beyaz) görüntüler üzerinde uygulanır.

**1. Erozyon (Erosion):** Erozyon, morfolojik görüntü işleme operasyonlarından biridir. Bu operasyon, bir yapıyı küçültmek veya vurgulamak için kullanılır. Özellikle görüntülerdeki kenarları ve ince detayları belirginlestirmek için kullanılır. Erozyon işlemi şu adımlarla gerçekleştirilir:

1. Bir 'kernel' veya 'structuring element' adı verilen küçük bir matris belirlenir. Bu kernel, görüntü üzerinde kaydırılırken kullanılır. 
2. Kernel, görüntünün her pikseline yerleştirilir ve merkeziyle hizalanır. Bu işlem sırasında kernel, görüntü üzerinde kaydırılır. 
3. Eğer kernelin içindeki tüm pikseller, orjinal görüntünün üzerinde kaplanıyorsa, bu merkez pikselin değeri değiştirilmez. Eğer en az bir piksel, kernelin dışında kalıyorsa, merkez pikselin değeri kernelin içindeki en küçük değere eşitlenir.

Bu işlem, genellikle nesnelerin kenarlarını ve ince yapılarını vurgulamak için kullanılır. Aynı zamanda gürültüyü azaltmak ve nesne konturlarını düzeltebilmek için de kullanışlıdır. 

Örnek bir uygulama, siyah arkaplan üzerinde beyaz nesnelerin olduğu bir görüntüde erozyon işlemi uygulandığında nesnelerin kenarlarının ve ince yapıların daha belirgin hale gelmesidir.

Erozyon, genellikle açma(opening) işlemi ile birlikte kullanılır. Açma işlemi, önce erozyon ve ardından genişleme işleminin uygulanmasıdır. Bu kombinasyon, gürültüyü azaltmak ve nesne konturlarını düzeltebilmek için etkili bir yöntemdir.

**2. Genişleme (Dilation):** Genişleme, morfolojik görüntü işleme operasyonlarından biridir. Bu operasyon, bir yapıyı genişletmek veya belirginleştirmek için kullanılır. Özellikle görüntülerdeki kenarları ve kalın yapıları belirginleştirmek amacıyla kullanılır. Genişleme işlemi şu adımlarla gerçekleştirilir: 

1. Bir 'kernel' veya 'structuring element' adı verilen küçük bir matris belirlenir. Bu kernel, görüntü üzerinde kaydırılırken kullanılır. 
2. Kernel, görüntünün her pikseline yerleştirilir ve merkeziyle hizalanır. Bu işlem sırasında kernel, görüntü üzerinde kaydırılır. 
3. Eğer kernelin içindeki tüm pikseller, orjinal görüntünün üzerinde kaplanıyorsa, bu merkez pikselin değeri değiştirilmez. Eğer en az bir piksel, kernelin dışında kalıyorsa, merkez pikselin değeri kernelin içindeki en küçük değere eşitlenir.

Bu işlem, genellikle nesnelerin kenarlarını ve kalın yapıları belirginleştirmek için kullanılır. Özellikle bir nesnenin kenarlarına ek pikseller eklemek suretiyle nesne konturlarını daha belirgin hale getirmek amacıyla kullanılır.

Genişleme, genellikle kapanma(closing) işlemi ile birlikte kullanılır. Kapanma işlemi, önce genişleme ve ardından erozyon işleminin uygulanmasıdır. Bu kombinasyon, nesne konturlarını düzeltebilmek ve nesneleri vurgulamak için etkili bir yöntemdir. 

**3. Açma (Opening):** Açma, morfolojik görüntü işleme operasyonlarından biridir. Bu operasyon, özellikle gürültüyü azaltmak ve nesne konturlarını düzeltebilmek için kullanılır. 

Açma işlemi şu adımlarla gerçekleştirilir:

1. Erozyon işlemi uygulanır. Erozyon, görüntüdeki küçük detayları, ince yapıları ve gürültüyü azaltır.
2. Ardından, bu erozyon işlemi sonucunda oluşan görüntü üzerinde genişleme işlemi uygulanır. Genişleme, önceli adımda küçülen yapıları ve nesne konturlarını tekrar belirginleştirir.

Açma işlemi genellikle gürültüyü azaltmak ve nesne konturlarını düzeltebilmek için kullanılır. Özellikle siyah noktalar, beyaz zemin üzerinde bulunan küçük detaylar veya ince yapılar gibi durumları düzeltebilmek amacıyla tercih edilir.

Bu işlem, genellikle bir "structuring element" (kernel) belirtilerek gerçekleştirilir. Bu kernel, erozyon ve genişleme işlemlerinde kullanılırken, işlemin ne kadar etkili olacğaını belirler. 

**4. Kapama (Closing):** Kapanma, morfolojik görüntü işleme operasyonlarından biridir. Bu operasyon, nesne konturlarını düzeltmek ve boşlukları doldurmak için kullanılır.

Kapama işlemi şu adımlarla gerçekleştirilir:

1. Genişleme işlemi uygulanır. Bu, özellikle nesne konturlarını düzeltmek ve boşlukları doldurmak için kullanılır.
2. Ardından, bu genişleme işlemi sonucunda oluşan görüntü erozyon işlemi uygulanır. Erozyon, genişlemiş yapıları ve nesne konturlarını tekrar düzelten bir işlemdir.

Kapama işlemi genellikle nesne konturlarını düzeltebilmek ve boşlukları doldurabilmek için kullanılır. Özellikle nesnelerin kenarlarındaki küçük boşlukları kapatmak ve nesne konturlarını düzeltmek amaçlanır.

Bu işlem, genellikle bir kernel belirtilerek gerçekleştirilir. Bu kernel, genişleme ve erozyon işlemlerinde kullanılırken, işlemin ne kadar etkili olacağını belirler. 

**5. Morfolojik Gradyan:** Morfolojik gradyan, bir görüntünün genişleme ve erozyon işlemlerinin farkı olarak hesaplanan bir operatörüdür. Bu işlem sonucunda, görüntünün kenarları veya bölgeler arası geçişler belirginleştirilir. Morfolojik gradyan, genellikle bir görüntünün kenarlarını, dış konturları veya bölgeler arası geçişleri belirlemek için kullanılır. 

Matematiksel olarak, morfolojik gradyan şu şekilde hesaplanır:

**Gradient = Dilation - Erosion**

**Not:** Görüntünün gradyanı, görüntüdeki yoğunluk değişikliklerini temsil eden bir vektördür. Bu vektör, her bir pikselin x ve y yönlerindeki türevlerini ifade eder. Pratikte, gradyan bilgisi, görüntünün kenarları, çizgileri ve diğer önemli özellikleri belirlemek için kullanılır. 

Matematiksel olarak, bir iki boyutlu görüntünün gradyanı şu şekildedir: 
```math
\nabla f(\left.x_{1}, x_{2}, \ldots, x_{n}\right)=\left[\begin{array}{c}
\dfrac{\partial f}{\partial x_1}(\left.x_{1}, x_{2}, \ldots, x_{n}\right)\\
\dfrac{\partial f}{\partial x_2}(\left.x_{1}, x_{2}, \ldots, x_{n}\right) \\
\vdots \\
\dfrac{\partial f}{\partial x_n}(\left.x_{1}, x_{2}, \ldots, x_{n}\right) 
\end{array}\right]
```
<a id="histogram-analysis"></a>

## Histogram Analizi

Histogram analizi, bir görüntünün piksel değerlerinin istatistiksel dağılımını inceleyen bir işlemdir. Görüntünün renk veya yoğunluk dağılımını gösteren bir grafik olarak ifade edilir. Histogram, bir görüntünün her bir piksel değerini (genellikle 0 ile 255 arasında) temsil eden bir çubuk grafiğidir. X ekseni piksel değerlerini, Y ekseni ise bu değerlere sahip piksellerin sayısını gösterir.

Bu analiz, görüntünün kontrastı, parlaklığı ve renk dengesi gibi özelliklerini anlamak için önemlidir. Örneğin; bir görüntünün histogramı, görüntünün genel kontrastının ne kadar iyi olduğunu gösterebilir. Ayrıca, ışık dengesi ayarları yaparken veya belirli bir renk kanalını vurgulamak istendiğinde de kullanışlı olabilir.

Histogram analizi ayrıca görüntü işleme algoritmalarının performansını değerlendirmek ve ayarlamak için de kullanılır. Örneğin; histogram eşitleme, görüntünün kontrastını artırmak için kullanılan bir tekniktir ve bu, histogram analizi temelinde çalışır.

Bu nedenle histogram analizi, görüntü işleme ve analizi alanında önemli bir araçtır ve birçok farklı uygulama için temel bir birleşendir.

<a id="edge-detection"></a>

## Kenar Tespiti ve İzleme

Kenar tespiti, bir görüntünün belirgin kenarlarını veya geçiş bölgelerini belirlemek için kullanılan bir işlemdir. Bu, piksel değerlerinin hızla değiştiği bölgeleri belirlemek anlamına gelmektedir. Kenarlar, nesnelerin sınırları, şekillerin dış hatları veya önemli yapıları temsil eder. Kenar tespiti, görüntü işlemenin önemli bir adımıdır çünkü birçok nesne veya özellik kenarlarını içerir. Örneğin, bir nesnenin sınırlarının belirlenmesi, nesne takibi veya nesne tanıma için kritik bir adımdır. Kenarları tespit etmek için kullanılan algoritmalar şunlardır:

1. **Sobel Operatörü:** Sobel operatörü, bir görüntünün gradyanını hesaplamak ve kenarları tespit etmek için kullanılan bir görüntü işleme operatörüdür. X ve Y yönlerindeki türevleri kullanarak görüntünün gradyanını bulur. Bu, kenarların belirginleştirilmesi için kullanılır. 
Sobel operatörünün temel amacı, bir pikseldeki yoğunluğun hızla değiştiği bölgeleri tespit etmektir. Bu genellikle kenarlar veya geçiş bölgeleri olarak ifade edilir. Operatör, bu değişiklikleri tespit etmek için görüntünün lokal gradyanını hesaplar.

Sobel operatörü, bir Gaussian bulanıklaştırma işlemi ile birleştirilir. Bu, gürültünün etkilerini azaltarak daha doğru kenar tespiti sağlar. Sobel operatörü, x ve y yönlerinde türevleri alarak görüntünün gradyanını hesaplar. X yönündeki türev için \(G_x\), Y yönündeki türev için $`\G_y`$ olarak ifade edilir.

```math
\textit{X yönündeki Sobel operatörü: }
G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}
```
```math
\textit{Y yönündeki Sobel operatörü: }
G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}
```


