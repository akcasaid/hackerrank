#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # İlk olarak pozitif, negatif ve sıfır sayılarının sayılarını tutacak değişkenleri tanımlayalım.
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    # Dizinin elemanlarını tek tek inceleyerek sayıları güncelleyelim.
    for number in arr:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    # Toplam eleman sayısını bulalım.
    total_count = len(arr)
    
    # Pozitif, negatif ve sıfır oranlarını hesaplayalım ve formatlayarak yazdıralım.
    print(f"{positive_count / total_count:.6f}")
    print(f"{negative_count / total_count:.6f}")
    print(f"{zero_count / total_count:.6f}")

# Programın ana bloğu burasıdır.
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


'''Bu kod bloğu, kullanıcıdan aldığı bir dizi içindeki sayıların pozitif, negatif ve sıfır olma durumlarına göre oranlarını hesaplar ve bu oranları altı ondalık basamak hassasiyetiyle yazdırır.

Özetle, bu problemde sizden bir sayı dizisi verildiğinde dizideki pozitif, negatif ve sıfır sayıların oranını hesaplayıp bu oranları altı ondalık basamağa kadar yazdırmanız istenmektedir.




'''

