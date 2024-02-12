
import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    # Mumların en yüksek olanının boyunu bul.
    tallest = max(candles)
    # Yorum satırı: En yüksek mumun kaç kez tekrar ettiğini say.
    count = candles.count(tallest)
    # En yüksek mumun tekrar sayısını döndür.
    return count

    




    '''
    
Bir çocuğun doğum günü pastasında, çocuğun yaşına denk gelecek şekilde belli sayıda mum bulunmaktadır.
Bu mumlardan sadece en yüksek olanları üfleyebileceklerdir. Fonksiyon, verilen mumların yüksekliklerini içeren bir listeden, en yüksek olan mumların sayısını bulup döndürmelidir.
Örneğin, [4, 4, 1, 3] listesi için en yüksek mumlar 4 birim yüksekliğinde ve 2 adettir, bu yüzden fonksiyon 2 değerini döndürecektir. ​​


'''

# Kullanıcıdan alınan input yerine örnek bir input ([3, 2, 1, 3]) ile fonksiyonu test edelim.
candles = [3, 2, 1, 3]
result = birthdayCakeCandles(candles)
print( result )

