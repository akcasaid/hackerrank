def split_and_join(line):
    words= line.split(" ") # Önce dizeyi boşluklara göre ayırıyoruz.
    join_line = "-".join(words)  # Sonra kelimeleri bir tire ile birleştiriyoruz.
    return join_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)