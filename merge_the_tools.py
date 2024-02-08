'''

Soru:

Verilen bir string (s) ve bir integer (k) değeri var.
Bu string belirli bir uzunlukta (n) ve integer (k) bu uzunluğun bir böleni.
String n/k adet alt dizeye (substring) bölünüyor, her bir alt dize k uzunluğunda ve string içinde ardışık karakterlerden oluşuyor.
Her alt dizenin (t_i) içinde tekrar eden karakterler siliniyor ve bu işlem sonucu oluşan her bir yeni dizeye (u_i) dönüştürülüyor.
Bu işlem, string içindeki her k karakterlik ardışık bölüm için tekrarlanıyor.
Sonuç olarak, her u_i dizesi, tekrar eden harfler çıkarıldıktan sonra elde edilen benzersiz karakter dizisi oluyor ve her bir u_i yeni satırda yazdırılıyor.
Örnek:

string = 'AABCAADA'
k = 3
Bu durumda, string ['AAB', 'CAA', 'ADA'] şeklinde üç parçaya ayrılır. 
Her parçada tekrar eden harfler çıkarılır ve sonuç olarak ['AB', 'CA', 'AD'] elde edilir. 
Her bir benzersiz dizi yeni bir satırda yazdırılır.
'''


def merge_the_tools(string, k):
    # Her bir t_i parçasını işleyip u_i'yi oluşturacak döngü
    for i in range(0, len(string), k):
        # t_i parçasını al
        t_i = string[i:i+k]
        # u_i'yi oluşturacak boş string
        u_i = ''
        # Her bir karakter için tekrar edip etmediğini kontrol et
        for char in t_i:
            # Eğer karakter u_i'de yoksa ekle
            if char not in u_i:
                u_i += char
        # u_i'yi yazdır
        print(u_i)

# Ana fonksiyon
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
