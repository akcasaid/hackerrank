"her kelimenin ilk harfini büyük yapmanız ve geri kalanını olduğu gibi bırakmanız gerekiyor."


def solve(s):
    # Her kelimenin ilk harfini büyük yapmak için bir liste anlayışı kullanıyoruz
    return ' '.join(word.capitalize() for word in s.split(' '))

# Test amaçlı main bloğunu kullanabiliriz.
if __name__ == '__main__':
    s = input("Please enter the full name to capitalize: ")

    result = solve(s)

    print(result)
