def print_formatted(number):
    # İkilik sistemdeki en geniş sayının uzunluğunu buluyoruz
    width = len("{:b}".format(number))
    
    # 1'den başlayarak number'a kadar olan her sayı için döngü başlatıyoruz
    for i in range(1, number+1):
        # Decimal, octal, hexadecimal ve binary formatları sırasıyla alıyoruz
        decimal = str(i)
        octal = "{:o}".format(i)
        hexadecimal = "{:X}".format(i)
        binary = "{:b}".format(i)
        
        # Alınan değerleri, ikilik sistemdeki en geniş sayının uzunluğuna göre hizalıyoruz
        # ve tek bir satırda yazdırıyoruz
        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Her bir değer arasında ekstra bir boşluk bırakmak yerine, rjust ile yeterli boşluk eklenir.