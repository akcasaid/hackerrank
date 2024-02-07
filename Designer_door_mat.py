# Verilen boyutlarda kapı paspası deseni oluşturma
def door_mat_design(N, M):
    # Paspasın ortasında WELCOME yazılacak satır numarası
    welcome_line = N // 2
    
    # Üst kısım için desen oluşturma
    for i in range(welcome_line):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))
    
    # WELCOME yazısını ortaya yerleştirme
    print("WELCOME".center(M, "-"))
    
    # Alt kısım için desen oluşturma (üst kısımın tersi)
    for i in range(welcome_line-1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))

# Ana program
if __name__ == '__main__':
    # Kullanıcıdan N ve M değerlerini alıp integer'a çevirme
    N, M = map(int, input().split())
    
    # Desen fonksiyonunu çağırma ve sonucu yazdırma
    door_mat_design(N, M)
