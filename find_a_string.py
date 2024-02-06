def count_substring(string, sub_string):
    count = 0  # Bulunan alt dizgi sayısını tutmak için bir sayaç başlatıyoruz.
    # String içinde dolaşmak için bir for döngüsü başlatıyoruz.
    # range fonksiyonu, string'in uzunluğundan, alt dizginin uzunluğu çıkarıldıktan sonraki değere kadar döngü oluşturur.
    for i in range(len(string) - len(sub_string) + 1):
        # Eğer string'in belirli bir kısmı (i'nci indexten itibaren alt dizginin uzunluğuna kadar olan kısım) 
        # aranan alt diziye eşitse sayaç artırılır.
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count  # Sayacın son değeri döndürülür.

# Örnek girdiler
string = "hellohellohello"  # İncelenecek ana dizi
sub_string = "lo"  # Aranan alt dizi

# Fonksiyonu kullanarak alt dizginin kaç kez geçtiğini sayıyoruz.
count = count_substring(string, sub_string)

# Sayacın değerini yazdırıyoruz.
