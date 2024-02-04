if __name__ == '__main__':
    N = int(input())
    listem=[]
    
    for _ in range(N):
        command = input ().split()
        
        if command[0] == 'insert':
            i = int(command[1])
            e = int(command[2])
            listem.insert(i,e)
        elif command[0] =='print':
            print (listem)
        elif command[0] == 'remove':
            e=int(command[1])
            listem.remove(e)
        elif command[0] =='append':
            e=int(command[1])
            listem.append(e)
        elif command[0] == 'sort':
            listem.sort()
        elif command[0] == 'pop':
            listem.pop()
        elif command[0] =='reverse':
            listem.reverse()