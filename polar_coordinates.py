import cmath

# Verilen kompleks sayıyı kutupsal koordinatlara dönüştürme
def convert_to_polar(complex_number):
    # Modülüsü (r) hesapla
    r = abs(complex_number)
    # Faz açısını (phi) hesapla
    phi = cmath.phase(complex_number)
    return r, phi

# Örnek girdi
complex_number = complex(1+2j)

# Kutupsal koordinatlara dönüştür ve yazdır
r, phi = convert_to_polar(complex_number)
print(f"{r:.3f}")
print(f"{phi:.3f}")
