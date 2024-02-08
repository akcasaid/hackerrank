def average(array):
    # Set kullanarak dizideki tekrar eden öğeleri kaldır ve benzersiz yükseklikleri elde et
    distinct_heights = set(array)
    
    # Benzersiz yüksekliklerin ortalamasını hesapla
    # sum() fonksiyonu ile benzersiz yüksekliklerin toplamını al
    # len() fonksiyonu ile benzersiz yüksekliklerin sayısını bul
    # Sonucu 3 ondalık basamağa yuvarla
    average_height = sum(distinct_heights) / len(distinct_heights)
    
    # Ortalama yüksekliği döndür
    return average_height

# Ana fonksiyon testi
if __name__ == '__main__':
    # Örnek girdilerle fonksiyonu test etmek için yorum satırlarını kaldırabilirsiniz:
    # n = 10
    # arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
    # result = average(arr)
    # print(f"{result:.3f}")  # Formatı 3 ondalık basamağa yuvarla ve yazdır
