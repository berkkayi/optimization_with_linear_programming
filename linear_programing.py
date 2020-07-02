#[x11,x12,x13,x14,
#x21,x22,x23,x24,
#x31,x32,x33,x34]

#satırlar sırasıyla 1. satır Tembel Pazar sabahı, 2. satır canlandırıcı , 3. satır bütün gece sınav
# sütunlar sırasıyla 1. kahve çekirdeği , 2. kahve çekirdeği , 3. kahve çekirdeği , 4. kahve çekirdeği
#ij olarak satır sütun olarak tek değişkene indirgedim

#i=1,2,3 (kahveler)
#j = 1,2,3,4 (kahve çekirdekleri)



import pulp as p

Lp_prob = p.LpProblem('Problem', p.LpMaximize)
####DEĞİŞKENLER
# bütün x değişkenleri bilinmediği için hepsine sıfır olarak tanımladım
x11 = p.LpVariable("x11", lowBound = 0)
x12 = p.LpVariable("x12", lowBound = 0)
x13 = p.LpVariable("x13", lowBound = 0)
x14 = p.LpVariable("x14", lowBound = 0)

x21 = p.LpVariable("x21", lowBound = 0)
x22 = p.LpVariable("x22", lowBound = 0)
x23 = p.LpVariable("x23", lowBound = 0)
x24 = p.LpVariable("x24", lowBound = 0)

x31 = p.LpVariable("x31", lowBound = 0)
x32 = p.LpVariable("x32", lowBound = 0)
x33 = p.LpVariable("x33", lowBound = 0)
x34 = p.LpVariable("x34", lowBound = 0)

##### AMAÇ FONKSİYONU
#amaç fonksiyonunda bütün çekirdekleri her ürün için ürünlerin katsayısı ile çarpıp topladım
Lp_prob += 1.25*(x11+x12+x13+x14) + 1.50*(x21+x22+x23+x24) + 1.75 *(x31+x32+x33+x34)

###### KISITLAR
#0.083 bir bardak kahvenin çekirdek fiyatı(maliyeti) (2,5/30)
#15000 (500 kilogram çekirdekten kaç tane kahve çıktığı)(500*30)
# kilogram cinsindeki ölçü birimini bardağa çevirerek kar a etkisini ölçmeyi hedefledim
Lp_prob += 0.083*(x11+x21+x31) <= 15000
Lp_prob += 0.091*(x12+x22+x32) <= 15000
Lp_prob += 0.066*(x13+x23+x33) <= 15000
Lp_prob += 0.116*(x14+x24+x34) <= 9000

#negatif olmaması için 0 dan büyük eşit koşulu koydum
Lp_prob += x11 >= 0.0
Lp_prob += x12 >= 0.0
Lp_prob += x13 >= 0.0
Lp_prob += x14 >= 0.0
Lp_prob += x21 >= 0.0
Lp_prob += x22 >= 0.0
Lp_prob += x23 >= 0.0
Lp_prob += x24 >= 0.0
Lp_prob += x31 >= 0.0
Lp_prob += x32 >= 0.0
Lp_prob += x33 >= 0.0
Lp_prob += x34 >= 0.0

#1. içeçecek için 3. çekirdek ve 4. çekirdekten tüm içecek için %25 e kadar bulunması şartı
#bütün çekirdekleri kapsadım çünkü koşuldan sonraki % açığı diğer çekirdeklerden tamamlaması için
Lp_prob += x13+x14 <= 0.25*(x11+x12+x13+x14) 
Lp_prob += x22+x23 == 0.75*(x21+x22+x23+x24)
Lp_prob += x34 >= 0.60*(x31+x32+x33+x34)

status = Lp_prob.solve()    

#problemi çözüp hangi çekirdekten nekadar kullanılması gerektiğini belirleyip kar nekadar olacağını belirttim
###### ÇÖZÜM VE ÇIKTI
print(p.LpStatus[status]) 
print("kullanılması gereken çekirdekler sırasıyla tembel pazar sabahı ürünü:",p.value(x11), p.value(x12),p.value(x13),p.value(x14))
print("kullanılması gereken çekirdekler sırasıyla canlandırıcı ürünü :",p.value(x21),p.value(x22),p.value(x23),p.value(x24))
print("kullanılması gereken çekirdekler sırasıylabütün gece sınav ürünü:",p.value(x31),p.value(x32),p.value(x33),p.value(x34))
print("maksimum kar:",p.value(Lp_prob.objective))
      
#görüldüğü üzere stoklar dahilinde hiç 1. kahveden üretmemek daha mantıklı olacaktır

