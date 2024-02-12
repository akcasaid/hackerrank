import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Yorum satırı: Diziyi sıralayarak en küçük ve en büyük değerleri kolayca buluruz.
    arr.sort()
    # Yorum satırı: En küçük toplam için ilk dört elemanı, en büyük toplam için son dört elemanı toplarız.
    min_sum = sum(arr[:4])  # ilk dört elemanın toplamı
    max_sum = sum(arr[-4:])  # son dört elemanın toplamı
    # Yorum satırı: Bulduğumuz minimum ve maksimum toplamları ekrana basarız.
    print(min_sum, max_sum)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

'''

Verilen beş pozitif tam sayıdan oluşan bir dizi için, bu sayıların tam olarak dört tanesini toplayarak elde edilebilecek minimum ve maksimum değerler bulunmalı 
ve bu iki değer tek satırda, aralarında bir boşluk bırakılarak yazdırılmalıdır. 
Örneğin, [1, 2, 3, 4, 5] dizisi için en küçük toplam 1+2+3+4=10 ve en büyük toplam 2+3+4+5=14 olacaktır. 
Bu hesaplamalar sonucunda 10 14 değerlerini yazdırmamız beklenmektedir. ​

'''