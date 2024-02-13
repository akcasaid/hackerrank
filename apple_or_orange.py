def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Sam'in evinin üzerine düşen elma ve portakal sayısını hesaplar.
    
    Parametreler:
    s (int): Sam'in evinin başlangıç noktası.
    t (int): Sam'in evinin bitiş noktası.
    a (int): Elma ağacının konumu.
    b (int): Portakal ağacının konumu.
    apples (int listesi): Her bir elmanın ağaçtan düştüğü mesafeler.
    oranges (int listesi): Her bir portakalın ağaçtan düştüğü mesafeler.
    """
    # Elma ve portakal sayılarını saklayacak değişkenler.
    apple_count = 0
    orange_count = 0

    # Elmaların düştüğü noktaları hesapla ve evin üzerine düşenleri say.
    for d in apples:
        if a + d >= s and a + d <= t:
            apple_count += 1

    # Portakalların düştüğü noktaları hesapla ve evin üzerine düşenleri say.
    for d in oranges:
        if b + d >= s and b + d <= t:
            orange_count += 1

    # Sonuçları yazdır.
    print(apple_count)
    print(orange_count)

# Ana program
if __name__ == '__main__':
    # Sam'in evinin başlangıç ve bitiş noktalarını al.
    s, t = map(int, input().split())
    # Elma ve portakal ağaçlarının konumlarını al.
    a, b = map(int, input().split())
    # Elma ve portakal sayılarını al.
    m, n = map(int, input().split())
    # Elmaların ağaçtan düştüğü mesafeleri al.
    apples = list(map(int, input().split()))
    # Portakalların ağaçtan düştüğü mesafeleri al.
    oranges = list(map(int, input().split()))

    # Hesaplama fonksiyonunu çağır.
    countApplesAndOranges(s, t, a, b, apples, oranges)
