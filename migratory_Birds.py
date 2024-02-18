import math
import os
import random
import re
import sys
'''

Bir dizi kuş gözlem verisi verilmiş ve her eleman farklı bir kuş türünü temsil etmekte. 
Görev, en sık görülen kuş türünün ID'sini belirlemek. 
Eğer en sık görülen birden fazla kuş türü varsa, en düşük ID numarasına sahip olan kuş türünün ID'si döndürülmeli.
Örneğin, eğer tip 1 ve tip 2 kuşları aynı sıklıkta görülmüşse ve bu sayı en yüksek sıklık ise, fonksiyon 1 ID'sini döndürmelidir çünkü 1, 2'den daha düşük bir sayıdır.

Girdi şu şekilde olacak:
İlk satırda bir tamsayı n, dizinin boyutunu belirtir.
İkinci satır n adet tamsayı içerir ve her tamsayı bir kuş türünü temsil eder.
Çıktı olarak, en sık görülen kuş türünün ID'sini bir tamsayı olarak döndürmelisiniz.

Sorunun çözümü için bir sözlük yapısı kullanarak her kuş türünün sıklığını hesaplamalı ve en sık görülen türü bulmalısınız. 
Birden fazla tür aynı sıklıkta ise, ID'si en küçük olanı seçmelisiniz.

Sorunun verdiği örnek girdiler ve beklenen çıktılar şöyle:

Örnek girdi 1: arr = [1, 4, 4, 4, 5, 3]

Beklenen çıktı 1: 4

Örnek girdi 2: arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

Beklenen çıktı 2: 3

Verilen hata mesajı, bir NameError göstermekte ve bu genellikle bir değişkenin tanımlı olmadığı durumlarda ortaya çıkar. 
Kodunuzda bird_frequencies adlı bir değişkenin kullanıldığı yerde bu değişkenin tanımlı olmadığı anlamına gelir. 
Bu tür hatalar genellikle yazım hatalarından veya kodun bir kısmının eksik olmasından kaynaklanır.



'''
def migratoryBirds(arr):
    # Gözlem sıklığına göre kuş türlerini sayacak bir sözlük oluşturuyoruz.
    bird_frequencies = {}

    # Dizideki her bir kuş türü için gözlem sayısını hesaplıyoruz.
    for bird in arr:
        if bird in bird_frequencies:
            bird_frequencies[bird] += 1
        else:
            bird_frequencies[bird] = 1

    # En sık gözlemlenen kuş türünü buluyoruz.
    # Eğer birden fazla tür en yüksek sayıya sahipse, en düşük ID'li olanı seçiyoruz.
    most_frequent = min(bird_frequencies, key=lambda x: (-bird_frequencies[x], x))

    # En sık gözlemlenen kuş türünün ID'sini döndürüyoruz.
    return most_frequent

# Test amaçlı ana blok
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Örnek olarak yerel bir dosya yolu verilmiştir.

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)  # Sonucu konsola yazdırıyoruz.
    # fptr.write(str(result) + '\n')  # Dosyaya yazdırma
    # fptr.close()  # Dosyayı kapatma


#PYP3 ile deneyin Python ile hata veiryor
