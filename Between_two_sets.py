# Python fonksiyonunu Türkçe yorum satırları ile tamamlıyoruz ve sorunun özetini de ekliyoruz.

def gcd(x, y):
    """İki sayının en büyük ortak bölenini hesapla."""
    while y != 0:
        (x, y) = (y, x % y)
    return x

def lcm(x, y):
    """İki sayının en küçük ortak katını hesapla."""
    return x * y // gcd(x, y)

def getTotalX(a, b):
    """
    İki küme arasında kaç tane tam sayı olduğunu belirle.
    Aradaki set demek:
    1. İlk kümedeki tüm elemanlar, göz önünde bulundurulan sayının bölenleri olmalıdır.
    2. Göz önünde bulundurulan sayı, ikinci kümedeki tüm elemanların bir böleni olmalıdır.
    """
    # En küçük ortak katı (LCM) hesapla
    current_lcm = a[0]
    for i in a[1:]:
        current_lcm = lcm(current_lcm, i)

    # En büyük ortak böleni (GCD) hesapla
    current_gcd = b[0]
    for i in b[1:]:
        current_gcd = gcd(current_gcd, i)

    # LCM'nin katlarının, GCD'nin bölenleri olup olmadığını kontrol et
    count = 0
    multiple_of_lcm = current_lcm
    while multiple_of_lcm <= current_gcd:
        if current_gcd % multiple_of_lcm == 0:
            count += 1
        multiple_of_lcm += current_lcm

    return count

# Fonksiyonun özeti:
# getTotalX fonksiyonu, iki dizi arasında "between" olarak tanımlanan sayıları bulur.
# "Between" sayılar, ilk dizi elemanlarının tümünün böleni ve ikinci dizi elemanlarının tümü tarafından bölünebilen sayılardır.
# Fonksiyon, bu sayıların sayısını döndürür.

# Örnek girdi ve fonksiyonun test edilmesi
a = [2, 6]
b = [24, 36]

# Beklenen çıktı 2 olmalıdır, çünkü setler arasında 6 ve 12 sayıları bulunmaktadır.
getTotalX(a, b)
