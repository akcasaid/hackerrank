if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
     
    result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    print(result)
    
    
    
 
 
 '''Python kodu, üç boyutlu bir koordinat uzayında, belirli bir noktanın  (x,y,z)  koordinatlarına sahip bir küpoidin (dikdörtgenler prizmasının genel bir şekli) tüm köşe noktalarının listesini oluşturuyor. 
 Amaç, bu noktaların içinden koordinatlarının toplamı belirli bir 
�
n değerine eşit olmayanları bulmak.  '''