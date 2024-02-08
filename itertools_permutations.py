

# itertools modülünden permutations fonksiyonunu içe aktarıyoruz
from itertools import permutations

# Verilen string ve k boyutu için tüm olası permütasyonları yazdıran fonksiyon
def print_permutations(x, y):
    # permutations fonksiyonu ile x string'inin y uzunluğundaki tüm permütasyonlarını hesaplıyoruz
    # sorted fonksiyonu ile bu permütasyonları leksikografik sıraya göre sıralıyoruz
    permuts = sorted(permutations(x, y))
    
    # Sıralı permütasyonların her birini döngü ile gezip yazdırıyoruz
    for p in permuts:
        # p permütasyonu bir tuple olduğu için, join ile birleştirerek string haline getiriyoruz
        print(''.join(p))

# Örnek girdi değerleri
x= "HACK"
y = 2

# Fonksiyonu örnek girdilerle çağırıyoruz
print_permutations(x,y)


'''

# Girdi
x,y = input().split()
y = int(y)

# Permutasyonları yazdır
print_permutations(x,y)
'''