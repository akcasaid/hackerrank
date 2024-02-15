import os

# 'birthday' fonksiyonu, çikolata barını subarraylere bölmek için kullanılır.
def birthday(s, d, m):
    # 'ways' değişkeni, uygun segment sayısını saklar.
    ways = 0
    # 's' dizisinde dolaşır ve ardışık 'm' uzunluğunda segmentleri kontrol eder.
    for i in range(len(s) - m + 1):
        # Eğer mevcut segmentin toplamı 'd'ye eşitse, bir yol bulunmuştur.
        if sum(s[i:i+m]) == d:
            ways += 1
    # Bulunan uygun segment sayısını döndürür.
    return ways




'''

 Lily'nin çikolata barı üzerindeki sayıları Ron'un doğum günü toplamına (d) ve doğum ayının uzunluğuna (m) eşit olacak şekilde bölmesi gerektiğiyle ilgilidir. 
 Örneğin, eğer Ron'un doğum günü 4 ve doğum ayı 2 ise, 
 Lily'nin [1, 2, 1, 3, 2] dizilimindeki çikolata barını [2, 2] ve [1, 3] şeklinde iki farklı segmente bölebileceği yolları bulması gerekmektedir, 
 çünkü her iki segmentin toplamı 4'e eşit ve uzunlukları 2'dir.
'''