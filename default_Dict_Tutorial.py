from collections import defaultdict

# n ve m'yi al
n, m = map(int, input().split())

# Bir defaultdict oluştur
d = defaultdict(list)

# n kere döngüye gir
for i in range(n):

    # Bir kelime al
    word = input()

    # Kelimeyi defaultdict'e ekle
    d[word].append(i+1)

# m kere döngüye gir
for j in range(m):

    # Bir kelime al
    s = input()

    # Kelime defaultdict'te varsa
    if s in d:

        # Kelimenin tüm dizinlerini yazdır
        print(*d[s])

    # Kelime defaultdict'te yoksa
    else:

        # -1 yazdır
        print(-1)
