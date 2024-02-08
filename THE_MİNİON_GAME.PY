''' "The Minion Game" adlı oyunun amacı, verilen bir kelime için mümkün olan tüm alt kelimeleri (substringleri) oluşturarak oyunu oynamak ve her oyuncunun puanını hesaplamaktır.
Oyunda iki oyuncu var: Kevin ve Stuart. Kevin sadece ünlü harflerle başlayan kelimelerle puan kazanabilirken, Stuart ünsüz harflerle başlayan kelimelerle puan kazanır. 
Bir alt kelime kelime içinde kaç kez geçiyorsa o kadar puan kazandırır. 
İki oyuncu da mümkün olan tüm alt kelimeleri oluşturduğunda oyun sona erer ve en yüksek puana sahip olan oyuncu kazanır.'''

def minion_game(string):
    vowels = 'AEIOU'  # Ünlü harfler
    kevin_score = 0  # Kevin'in puanı
    stuart_score = 0  # Stuart'ın puanı
    
    # Kelimenin her harfi için döngü başlat
    for i in range(len(string)):
        # Eğer harf ünlü ise, Kevin puan kazanır
        if string[i] in vowels:
            kevin_score += (len(string) - i)
        else:
            # Eğer harf ünsüz ise, Stuart puan kazanır
            stuart_score += (len(string) - i)
    
    # Puanları karşılaştır ve kazananı belirle
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")  # Eğer puanlar eşit ise, beraberlik ilan et

# Oyunu test etmek için main bloğu
if __name__ == '__main__':
    s = input("Minion Oyunu için kelime giriniz: ")  # Kullanıcıdan kelime girmesini iste
    minion_game(s)  # Oyun fonksiyonunu çağır ve sonucu yazdır
