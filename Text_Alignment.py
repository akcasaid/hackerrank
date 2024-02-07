# Kullanıcının girdiği kalınlık değeri. Bu bir tek sayı olmalıdır.
thickness = int(input())
c = 'H'

# Üst Koni
# Her bir satır için 'H' karakterlerini artırarak ve her iki taraftan uygun boşluk bırakarak üst koni şeklini oluşturur.
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Üst Sütunlar
# Kalınlığın iki katı genişlikte ortalanmış 'H' blokları ve 6 kat genişlikte tekrar ortalanmış 'H' blokları ile üst sütunları oluşturur.
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Orta Kuşak
# Kalınlığın 5 katı genişlikte 'H' blokları ile orta kuşağı oluşturur.
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

# Alt Sütunlar
# Üst sütunlarla aynı mantıkta alt sütunları oluşturur.
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# Alt Koni
# Ters koni şeklini oluşturmak için 'H' karakterlerini azaltarak ve uygun hizalama yaparak alt koniyi çizer.
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



    '''Soru:
    Göreviniz, verilen bir kalınlık değeri için bir HackerRank logosu oluşturmaktı.
      Kalınlık tek bir sayı olmalı ve logo, belirli hizalama kurallarını kullanarak 'H' harflerinden oluşan bir desenle çizilmelidir. 
      Logo, üst koni, üst sütunlar, orta kuşak, alt sütunlar ve alt koniden oluşur.
        Her bölüm için Python'daki string metodları rjust, ljust, ve center kullanılarak uygun hizalamalar gerçekleştirilmelidir.
          Girdi formatı tek bir satırda kalınlık değerini içerir ve çıktı formatı istenen logoyu görsel olarak temsil eder.
    
    
    '''
