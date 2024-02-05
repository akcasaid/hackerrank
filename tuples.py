if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))



'''Python 3' de hata veriyor, PYpy 3 olarak denerseniz sonuca ulaşabilirsiniz
It gives error in Python 3, if you try as Python 3, you can reach the result'''