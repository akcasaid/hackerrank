'''

İki tane liste veriliyor, A ve B.
Görev, bu iki listenin Kartezyen çarpımını (Cartesian product) hesaplamak.
 Kartezyen çarpım, bir listenin her elemanının diğer liste ile eşleştirilmesiyle oluşan tüm çiftlerin (tuple) listesidir.
A ve B listeleri sıralı ve tekrarlayan öğe içermeyen listeler olarak veriliyor.
Kartezyen çarpımın sonuçları, oluşturulan tuple'lar sıralı bir şekilde çıktı olarak verilmeli.
İki liste de kullanıcıdan alınacak ve çıktı, boşlukla ayrılmış tuple'lar olarak sunulacak.
Örneğin, A = [1, 2] ve B = [3, 4] listeleri için çıktı şu şekilde olmalıdır:

(1, 3) (1, 4) (2, 3) (2, 4)

Burada, her ikili (tuple), A listesinden bir eleman ile B listesinden bir elemanın tüm mümkün kombinasyonlarını temsil eder.


'''

from itertools import product

# İki listeyi al ve Kartezyen çarpımını hesapla
def cartesian_product(A, B):
    return list(product(A, B))

# Kullanıcıdan girdileri al
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Kartezyen çarpımı hesapla ve yazdır
result = cartesian_product(A, B)
for item in result:
    print(item, end=' ')
