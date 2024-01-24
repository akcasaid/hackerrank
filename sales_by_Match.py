import math
import os
import random
import re
import sys



'''
Bu problem, bir yığın çoraptan eşleşen çiftleri bulma problemidir.
Her çorabın bir renk numarası ile temsil edildiğini ve bu renklerin tam sayılarla ifade edilir. 
Göreviniz, bu tam sayı dizisini alıp, kaç çift eşleşen çorap olduğunu bulmak

'''

# Bu kodu hackerrank'de çalıştırmak isterseniz Türkçe açıklamaları silmeniz gerekiyor. Silinmez ise :
# "Your submission contains non ASCII characters, we dont accept submissions with non ASCII characters for this challenge." hatası ile karşılaşabilirsiniz.




def sockMerchant(n, ar):
    # Her renkten kaç tane çorap olduğunu saklamak için bir sözlük oluşturulur.
    color_count = {}
    # Eşleşen çift sayısını saklamak için bir sayac.
    pair_count = 0
    
    # Her çorap için:
    for sock in ar:
        # Çorabın rengi sözlükte varsa, bir arttır.
        if sock in color_count:
            color_count[sock] += 1
        else:
            color_count[sock] = 1
        
        # Eğer bu renkten 2 veya daha fazla çorap varsa bir çift oluştur ve sayacı arttır.
        if color_count[sock] % 2 == 0:  # Her iki çorapta bir, çift sayısını arttır.
            pair_count += 1
    
    return pair_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


result = sockMerchant(n, ar)
print(result)


'''