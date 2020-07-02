# Linear programming optimization

- Optimizasyon dersimiz için yapmış olduğum modelleme projesi.
- Optimizasyonu python içindeki Pulp kütüphanesi ile modelledim.
- Linear programming yöntemlerine göre modellemenin amaç ve kısıtlarda aynı değişken kullanılarak yapılması gerekir. İlk etapta farklı değişkenlerin bulunduğu problemdeki değişkenlerin matris yapısına dönüştürerek tek bir değişkene çevirdim. Kısıtlarda kg cinsindeki stok değerini bardak cinsine dönüştürdüm. Kısıtlarda bütün çekirdeklerin kullanılması için kısıt ekledim. Modelin optimize hali için 1. kahvenin aslında hiç üretilmemesi gerektiği çıktı.Böylelikle karı maksimize edicek aksiyomlar alınabilir.
- Linear programming için optimize edilecek olayın optimize edilmeden önce mutlaka doğru ve etkin bir şekilde modellenmesi gerektiğini öğrendim.
-  Bu tarz modelleme algoritmaları maliyet minimizasyonu ile de modellenebilir. 