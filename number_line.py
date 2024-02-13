def kangaroo(x1, v1, x2, v2):
    """
    x1, v1: İlk kangurunun başlangıç pozisyonu ve sıçrama mesafesi
    x2, v2: İkinci kangurunun başlangıç pozisyonu ve sıçrama mesafesi
    İki kangurunun aynı noktada buluşup buluşmayacağını kontrol etmek için fonksiyon.
    """
    
    # İkinci kanguru ilk kangurudan hızlıysa ve önündeyse, ilk kanguru asla ikinciyi yakalayamaz.
    if v2 >= v1 and x2 > x1:
        return "NO"

    # Eğer ilk kanguru daha hızlıysa ve ikinci kanguru ile arasındaki mesafe, 
    # hız farkına tam bölünebiliyorsa, bir noktada buluşabilirler.
    try:
        if (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"
    except ZeroDivisionError: # Hızlar eşitse ve başlangıç pozisyonları farklıysa buluşmaları imkansızdır.
        return "NO"

# Fonksiyonu test edelim:
print(kangaroo(0, 3, 4, 2))  # Beklenen Çıktı: YES
print(kangaroo(0, 2, 5, 3))  # Beklenen Çıktı: NO
