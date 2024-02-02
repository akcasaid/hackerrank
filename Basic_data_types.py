if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # En büyük sayıyı bulup listeden çıkar
    max_score = max(arr)
    while max_score in arr:
        arr.remove(max_score)
    
    # İkinci en büyük sayıyı bul (yani runner-up)
    runner_up_score = max(arr)
    print(runner_up_score)