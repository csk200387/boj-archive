for i in range(int(input())) :
    ch, i, j = input().split()
    print(ch[:int(i)] + ch[int(j):])