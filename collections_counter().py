'''
Soru:

Raghu'nun bir ayakkabı dükkanı var ve dükkanında çeşitli bedenlerde X sayıda ayakkabı bulunuyor.
Müşteriler, belirli bir ayakkabı bedeni için xi miktarında para ödemeye hazırlar.
Amacımız, her müşterinin istediği bedendeki ayakkabıyı satabilecek miyiz ve eğer satarsak Raghu toplamda ne kadar para kazanacak, bunu hesaplamak.



'''






# Counter sınıfını kullanabilmek için collections modülünden Counter'ı içe aktarıyoruz
from collections import Counter

# Ayakkabı bedenleri ve müşteri isteklerine göre toplam kazancı hesaplayan fonksiyon
def calculate_income(shoe_sizes, customer_requests):
    # Ayakkabı bedenlerini bir Counter nesnesine dönüştürerek her bedenden kaç adet olduğunu sayıyoruz
    inventory = Counter(shoe_sizes)
    income = 0  # Toplam kazancı sıfırlıyoruz
    
    # Müşteri taleplerini tek tek işliyoruz
    for size, price in customer_requests:
        # Eğer istenen bedende ayakkabı varsa (envanterde sayı 0'dan büyükse)
        if inventory[size]:
            income += price  # Kazanca ayakkabının fiyatını ekliyoruz
            inventory[size] -= 1  # Envanterden bir ayakkabı çıkarıyoruz
    
    return income  # Toplam kazancı döndürüyoruz

# Kullanıcıdan girdileri alıyoruz
X = int(input())  # Ayakkabı sayısı
shoe_sizes = list(map(int, input().split()))  # Ayakkabı bedenleri listesi
N = int(input())  # Müşteri sayısı
customer_requests = [tuple(map(int, input().split())) for _ in range(N)]  # Müşteri talepleri

# Toplam kazancı hesaplayıp yazdırıyoruz
total_income = calculate_income(shoe_sizes, customer_requests)
print(total_income)

'''  kod bloğu, önce ayakkabı bedenlerini ve müşteri taleplerini alıyor.
Daha sonra calculate_income fonksiyonu ile her müşterinin talebini karşılayıp karşılayamayacağını kontrol ederek, mümkünse satış yapıyor ve toplam kazancı hesaplıyor.
 En sonunda toplam kazancı ekrana basıyor. '''