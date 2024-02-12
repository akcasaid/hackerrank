'''
 Verilen bir n sayısı için, n yüksekliğinde ve n genişliğinde, sağa yaslanmış bir "#" işaretlerinden oluşan bir merdiven şekli çizilmesi istenmektedir. 
 Her satır bir önceki satırdan bir "#" işareti daha fazla olacak şekilde ve sol tarafında uygun sayıda boşluk bırakılarak yazdırılmalıdır ki, merdivenin sağa yaslanmış görünümü oluşsun. 
 Son satırda hiç boşluk olmamalı ve tamamen "#" işaretleri ile dolu olmalıdır. 


'''



def staircase(n):
    # Yorum satırı: n kadar yükseklikte bir merdiven oluşturulacak.
    for i in range(1, n + 1):  # Yorum satırı: 1'den n'e kadar döngü başlat (her satır için).
        # Yorum satırı: Her satırda önce boşluklar sonra # işaretleri basılacak.
        print(' ' * (n - i) + '#' * i)  # Yorum satırı: Boşluklar ve # işaretleri ile merdiven çiz.
n = 6
staircase(n)


'''
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
'''

