def compareTriplets(a, b):
    # Alice'in ve Bob'un puanları
    alice_points = 0
    bob_points = 0
    
    # Alice ve Bob'un puanlarını karşılaştırıyoruz.
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
        # Eğer puanlar eşitse, hiçbirine puan verilmiyor ve döngü devam ediyor.

    # Alice'in ve Bob'un toplam puanlarını bir liste olarak döndürüyoruz.
    return [alice_points, bob_points]


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
