import math
import os
import random
import re
import sys


def timeConversion(s):
    # Yorum satırı: Önce AM/PM'i kontrol etmek için son iki karakteri al.
    am_pm = s[-2:]
    # Yorum satırı: Saati, dakikayı ve saniyeyi almak için ilk 8 karakteri al (AM/PM hariç).
    time = s[:8]
    # Yorum satırı: Saati, dakikayı ve saniyeyi ":" ile ayır.
    hh, mm, ss = time.split(':')
    
    # Yorum satırı: Eğer PM ise ve saat 12'den küçükse saate 12 ekle.
    if am_pm == 'PM' and hh != '12':
        hh = str(int(hh) + 12)
    # Yorum satırı: Eğer AM ise ve saat 12 ise saati '00' yap.
    elif am_pm == 'AM' and hh == '12':
        hh = '00'
    
    # Yorum satırı: Yeni saat, dakika ve saniyeyi birleştir.
    return f"{hh}:{mm}:{ss}"

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


'''
Verilen bir zamanı 12 saatlik AM/PM formatından 24 saatlik formata dönüştürmek. 
Not olarak, '12:00:00AM' 24 saatlik formatta '00:00:00' ve '12:00:00PM' ise '12:00:00' olarak kabul edilir. 
Örneğin, '12:01:00PM' verildiğinde dönüşüm sonucu '12:01:00' olmalıdır; '12:01:00AM' için ise '00:01:00' dönüşümü beklenir. ​


'''