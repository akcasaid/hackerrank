

def divisibleSumPairs(n, k, ar):
    # Fonksiyonun açıklaması: Bu fonksiyon, bir dizi içindeki tüm (i, j) indis çiftlerini kontrol eder,
    # ve ar[i] + ar[j]'nin k'ya tam bölünüp bölünmediğine bakar.
    # Parametreler:
    # n: Dizinin uzunluğu
    # k: Bölünebilirlik için kullanılacak sayı
    # ar: Kontrol edilecek sayıların dizisi
    
    # Çift sayısını saklayacak bir değişken tanımlıyoruz.
    count = 0
    
    # Tüm (i, j) çiftleri için döngü başlatıyoruz, burada i < j.
    for i in range(n):
        for j in range(i+1, n):  # j her zaman i'den büyük olmalı.
            # Eğer i ve j indislerindeki elemanların toplamı k'ya tam bölünüyorsa
            if (ar[i] + ar[j]) % k == 0:
                # Çift sayısını bir arttırıyoruz.
                count += 1
    
    # Bulunan çift sayısını döndürüyoruz.
    return count

# Örnek kullanım:
n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]

# Fonksiyonu çağırıp sonucu yazdıralım.
result = divisibleSumPairs(n, k, ar)
print (result)

'''

Bu fonksiyon, bir dizi içerisindeki (i, j) indeks çiftleri için ar[i] + ar[j] toplamlarının verilen bir k sayısına tam bölünüp bölünmediğini kontrol eder. 
Böyle bir bölünme durumu varsa, bu çiftleri sayar. Sonuç olarak, verilen örnekte k = 3 için toplamları 3'e tam bölünebilen 5 adet çift bulunmaktadır'''