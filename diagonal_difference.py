def diagonalDifference(arr):
    # Matrisin boyutunu bul (n x n matrisi için)
    n = len(arr)
    
    # Ana köşegen ve ikincil köşegen toplamlarını tutacak değişkenler
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    # Köşegen elemanlarını toplamak için döngü
    for i in range(n):
        # Ana köşegen toplamı: Matrisin [i][i] indeksli elemanları
        primary_diagonal_sum += arr[i][i]
        # İkincil köşegen toplamı: Matrisin [i][n-i-1] indeksli elemanları
        secondary_diagonal_sum += arr[i][n-i-1]
    
    # Köşegenler arasındaki mutlak farkı hesapla ve döndür
    return abs(primary_diagonal_sum - secondary_diagonal_sum)


'''

Bu problemde, bir n x n kare matrisin ana köşegeni ve ikincil köşegeni üzerindeki sayıların toplamları arasındaki mutlak farkı hesaplamamız isteniyor. 
Ana köşegen, sol üstten sağ alta doğru giden köşegendir ve ikincil köşegen ise sağ üstten sol alta doğru giden köşegendir.
 Fonksiyon, bu iki köşegen üzerindeki sayıları toplayıp aradaki farkı abs fonksiyonu ile mutlak değere çevirerek sonucu döndürür. 

'''