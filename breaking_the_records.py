'''
Maria kolej basketbolu oynamaktadır ve profesyonel olmayı hedeflemektedir. 
Her sezon oynadığı oyunlardaki puanları kaydederek, sezon içindeki en yüksek ve en düşük puanlarını kaç kere geçtiğini takip eder. 
İlk oyunun puanı başlangıç rekorları olarak kabul edilir ve Maria sezon boyunca bu rekorları geçtiği her oyun için sayım yapar. 
Görevimiz, verilen bir puan listesi için Maria'nın sezon boyunca en yüksek ve en düşük puan rekorlarını kaç kere kırdığını belirleyen bir fonksiyon yazmaktır.
'''

def breakingRecords(scores):
    # Başlangıçta en yüksek ve en düşük skor ilk oyunun skoru olarak ayarlanır
    highest = scores[0]
    lowest = scores[0]
    # En yüksek ve en düşük skor kırılma sayıları başlangıçta 0 olarak ayarlanır
    highest_break_count = 0
    lowest_break_count = 0
    
    # Skor listesindeki her skoru dön ve rekor kırılıp kırılmadığını kontrol et
    for s in scores[1:]:  # İlk oyun zaten başlangıç değerleri olarak ayarlandığı için dikkate alınmaz
        if s > highest:
            # Eğer skor en yüksek skordan daha büyükse, en yüksek skoru güncelle ve sayacı artır
            highest = s
            highest_break_count += 1
        elif s < lowest:
            # Eğer skor en düşük skordan daha küçükse, en düşük skoru güncelle ve sayacı artır
            lowest = s
            lowest_break_count += 1
    
    # Rekor kırma sayılarını bir liste olarak dön
    return [highest_break_count, lowest_break_count]

# Test the function with a sample input
sample_scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
breakingRecords(sample_scores)  # Beklenen çıktı problemde belirtildiği üzere [2, 4] olmalı.

sample_scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print (breakingRecords(sample_scores))

'''
Fonksiyon, verilen skor listesi üzerinde iterasyon yaparak Maria'nın her oyun sonrası en yüksek ve en düşük skor rekorlarını kaç kere kırdığını sayar. 
İlk oyunun skoru başlangıç rekoru olarak kabul edilir ve sonraki oyunlar bu rekorlarla karşılaştırılarak rekor kırılıp kırılmadığına bakılır. 
Her bir skor için, eğer o anki skor şimdiye kadarki en yüksek skordan yüksekse veya en düşük skordan düşükse, ilgili rekor kırma sayacı artırılır. 
Fonksiyon sonunda, en yüksek ve en düşük skor rekorlarının kaç kere kırıldığını içeren bir liste döndürür.
'''