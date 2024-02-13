# Let's translate the code comments to Turkish for better understanding.

def gradingStudents(grades):
    """
    Belirtilen kurallara göre notları yuvarlar.
    
    Parametreler:
    grades (int listesi): Yuvarlama öncesi notlar listesi.
    
    Döndürür:
    int listesi: Uygun şekilde yuvarlandıktan sonra notlar listesi.
    """
    rounded_grades = []  # Yuvarlanmış notları tutacak.
    
    for grade in grades:
        # Yuvarlamanın uygulanıp uygulanmayacağını kurallara göre kontrol ediyoruz:
        # Eğer not 38'den az ise yuvarlama yapılmıyor.
        if grade < 38:
            rounded_grades.append(grade)
        else:
            # Notun 5'in bir sonraki katını buluyoruz.
            next_multiple_of_5 = ((grade // 5) + 1) * 5
            
            # Eğer not ile 5'in bir sonraki katı arasındaki fark 3'ten az ise,
            # notu 5'in bir sonraki katına yuvarlıyoruz.
            if (next_multiple_of_5 - grade) < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                # Aksi takdirde, notu yuvarlamıyoruz.
                rounded_grades.append(grade)
    
    return rounded_grades

# Test için örnek girdi kullanıyoruz.
sample_input = [73, 67, 38, 33]

# Beklenen Çıktı: [75, 67, 40, 33]

# Fonksiyonu örnek girdi ile çağırıyoruz.
sample_output = gradingStudents(sample_input)

sample_output
