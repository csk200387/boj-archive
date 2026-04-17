for _ in range(int(input())) :
    n = int(input())
    d1 = [1, 0, 1]
    d2 = [0, 1, 1]
    for i in range(2, n) :
        d1.append(d1[i-1] + d1[i])
        d2.append(d2[i-1] + d2[i])
    print(d1[n], d2[n])