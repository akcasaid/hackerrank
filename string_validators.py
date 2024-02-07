# Kontrol edilecek olan S stringi
S = input()

# Alfanumerik karakter içerip içermediğini kontrol et
print(any(char.isalnum() for char in S))

# Alfabetik karakter içerip içermediğini kontrol et
print(any(char.isalpha() for char in S))

# Rakam içerip içermediğini kontrol et
print(any(char.isdigit() for char in S))

# Küçük harf içerip içermediğini kontrol et
print(any(char.islower() for char in S))

# Büyük harf içerip içermediğini kontrol et
print(any(char.isupper() for char in S))


'''Soru:
Bir S stringi veriliyor. 
Göreviniz, bu stringin içinde alfanumerik karakterler, alfabetik karakterler, rakamlar, küçük harf ve büyük harf karakterleri olup olmadığını bulmak. '''