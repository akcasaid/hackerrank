import textwrap

def wrap(string, max_width):
    # textwrap modülünün wrap fonksiyonunu kullanarak string'i
    # max_width genişliğinde satırlara böl ve her bir satırı
    # birleştirerek tek bir string haline getir.
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
