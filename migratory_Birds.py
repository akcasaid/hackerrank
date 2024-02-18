import math
import os
import random
import re
import sys

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